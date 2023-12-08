FROM alpine

COPY utils/ /bin
COPY run.sh /bin
COPY requirements.txt /

RUN add-pkg python3 py3-pip py3-pillow tzdata\
    && pip3 install -r /requirements.txt --break-system-packages

ENV TZ=America/Halifax

ENTRYPOINT [ "sh", "/bin/run.sh" ]
