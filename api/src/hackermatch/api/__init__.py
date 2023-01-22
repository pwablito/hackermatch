from hackermatch.api.endpoints import ENDPOINTS

import logging
from flask import Flask


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = Flask("HackerMatch API")

for endpoint, spec in ENDPOINTS.items():
    app.add_url_rule(f"/api/{endpoint.strip('/')}", spec["name"], spec["func"], methods=spec["methods"])


def main():
    app.run("0.0.0.0", 80)


if __name__ == "__main__":
    main()
