FROM python:3.10

COPY ./db /lib/hackermatch_db

WORKDIR /lib/hackermatch_db
RUN python3 -m pip install ".[migrate]"


ENTRYPOINT []
CMD []
