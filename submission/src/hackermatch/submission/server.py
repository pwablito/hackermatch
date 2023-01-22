from hackermatch.submission.servicer import SubmissionServicer
from hackermatch.grpc.stubs import submission_pb2_grpc

from concurrent import futures
import grpc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SubmissionServer:
    def __init__(self, db_url, host="0.0.0.0", port=80):
        logger.info(f"Connecting to database at {db_url}")
        engine = create_engine(db_url)
        session_maker = sessionmaker(bind=engine)

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        submission_pb2_grpc.add_SubmissionServiceServicer_to_server(SubmissionServicer(session_maker), self.server)
        self.server.add_insecure_port(f'{host}:{port}')

    def run(self):
        logger.info("Starting server")
        self.server.start()
        self.server.wait_for_termination()
