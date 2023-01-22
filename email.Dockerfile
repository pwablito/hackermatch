FROM hackermatch/libs:latest

COPY ./email /app/hackermatch_email_server
RUN python3 -m pip install /app/hackermatch_email_server

ENTRYPOINT [ "hackermatch-email-server" ]
CMD []
