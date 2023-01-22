FROM hackermatch/libs:latest as base

RUN apt-get -y update \
    && apt-get -y install nginx

COPY ./api/nginx.conf /etc/nginx

WORKDIR /app/hackermatch_api_server
COPY ./api /app/hackermatch_api_server
RUN python3 -m pip install /app/hackermatch_api_server[prod]
RUN chmod +x start.sh

ENTRYPOINT [ "./start.sh" ]
