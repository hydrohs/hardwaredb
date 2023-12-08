FROM alpine

COPY utils/ /bin
COPY run.sh /bin
COPY ../requirements.txt /app

RUN add-pkg python3 py3-pip py3-pillow tzdata\
    && pip3 install -r /app/requirements.txt

ENV TZ=America/Halifax

ENTRYPOINT [ "sh", "/bin/run.sh" ]
