FROM alpine

COPY utils/ /bin

RUN add-pkg python3 py3-pip py3-pillow \
    && pip3 install django==4.0.0 django-multiselectfield django-tables2

ENTRYPOINT [ "python3", "/app/manage.py", "runserver", "0.0.0.0:8000" ]
