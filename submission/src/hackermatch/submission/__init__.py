from hackermatch.submission.server import SubmissionServer

import os


def main():
    db_url = os.getenv("HACKERMATCH_DB", "postgresql://hackermatch:hackermatch@localhost/hackermatch")
    SubmissionServer(db_url=db_url).run()
