from hackermatch.email.servicer import EmailServicer
from hackermatch.grpc.stubs import email_pb2_grpc

from concurrent import futures
import grpc
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EmailServer:
    def __init__(self, host="0.0.0.0", port=80):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        email_pb2_grpc.add_EmailServiceServicer_to_server(EmailServicer(), self.server)
        self.server.add_insecure_port(f'{host}:{port}')

    def run(self):
        logger.info("Starting server")
        self.server.start()
        self.server.wait_for_termination()
