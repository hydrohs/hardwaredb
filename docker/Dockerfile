FROM alpine

COPY utils/ /bin
COPY run.sh /bin

RUN add-pkg python3 py3-pip py3-pillow tzdata\
    && pip3 install django==4.0.7 django-multiselectfield django-tables2

ENV TZ=America/Halifax

ENTRYPOINT [ "sh", "/bin/run.sh" ]
