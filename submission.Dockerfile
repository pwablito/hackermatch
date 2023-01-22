FROM hackermatch/libs:latest

COPY ./submission /app/hackermatch_submission_server
RUN python3 -m pip install /app/hackermatch_submission_server

ENTRYPOINT [ "hackermatch-submission-server" ]
CMD []
