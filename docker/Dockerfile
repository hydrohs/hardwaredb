FROM alpine

COPY utils/ /bin

RUN add-pkg python3 py3-pip py3-pillow tzdata\
    && pip3 install django==4.0.7 django-multiselectfield django-tables2

ENV TZ=America/Halifax

ENTRYPOINT [ "python3", "/app/manage.py", "runserver", "0.0.0.0:8000" ]
