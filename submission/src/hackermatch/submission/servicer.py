from hackermatch.grpc.stubs import submission_pb2_grpc, submission_pb2
from hackermatch.db.models import Submission

import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SubmissionServicer(submission_pb2_grpc.SubmissionServiceServicer):

    def __init__(self, session_maker):
        self.get_session = session_maker

    def AddSubmission(self, request, context):
        with self.get_session() as session:
            new_submission = Submission(
                hash=request.hash,
                email=request.email,
            )
            session.add(new_submission)
            session.commit()
        return submission_pb2.AddSubmissionResponse(
            success=True,
        )

    def GetMatches(self, request, context):
        matching_emails = []
        with self.get_session() as session:
            submissions = session.query(Submission).filter_by(hash=request.hash).all()
            for submission in submissions:
                matching_emails.append(submission.email)
        return submission_pb2.GetMatchesResponse(
            success=True,
            emails=matching_emails,
        )
