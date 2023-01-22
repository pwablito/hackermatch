from hackermatch.api import (
    submission
)


ENDPOINTS = {
    "/submission/submit": {
        "name": "submission",
        "func": submission.submit,
        "methods": ["POST"],
    },
}
