import os
import grpc


def get_email_channel():
    return get_grpc_channel("HACKERMATCH_EMAIL_SERVER")


def get_submission_channel():
    return get_grpc_channel("HACKERMATCH_SUBMISSION_SERVER")


def get_grpc_channel(var_name):
    addr = os.getenv(var_name, "localhost:80")
    return grpc.insecure_channel(addr)
