from hackermatch.api.channels import get_submission_channel, get_email_channel
from hackermatch.grpc.stubs import submission_pb2, submission_pb2_grpc, email_pb2, email_pb2_grpc

from flask import Response, request
import logging
import json


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def submit():
    if not request.json or not request.json["hash"] or not request.json["email"]:
        return Response(json.dumps({
            "success": False,
            "message": "Bad request"
        }), 400)
    with get_submission_channel() as submission_channel, get_email_channel() as email_channel:
        submission_stub = submission_pb2_grpc.SubmissionServiceStub(submission_channel)
        email_stub = email_pb2_grpc.EmailServiceStub(email_channel)
        submission_response = submission_stub.AddSubmission(submission_pb2.AddSubmissionRequest(
            hash=request.json["hash"],
            email=request.json["email"],
        ))
        if not submission_response.success:
            return Response(json.dumps({
                "success": False,
                "message": "Failed to add hash"
            }), 500)
        match_response = submission_stub.GetMatches(submission_pb2.GetMatchesRequest(
            hash=request.json["hash"],
        ))
        if not match_response.success:
            return Response(json.dumps({
                "success": False,
                "message": "Failed to query matches",
            }), 500)
        if len(match_response.emails) > 1:
            email_response = email_stub.SendMatchAlert(email_pb2.SendMatchAlertRequest(
                hash=request.json["hash"],
                emails=match_response.emails,
            ))
            if not email_response.success:
                return Response(json.dumps({
                    "success": False,
                    "message": "Failed to send match emails",
                }))
    return Response(json.dumps({
        "success": True,
    }), status=200)
