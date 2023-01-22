FROM python:3.10

COPY ./db /lib/hackermatch_db
COPY ./grpc /lib/hackermatch_grpc_stubs

RUN python3 -m pip install /lib/hackermatch_db /lib/hackermatch_grpc_stubs

CMD echo "This is a library image. Exiting now."
