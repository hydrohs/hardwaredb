FROM alpine

COPY utils/ /bin

RUN add-pkg python3 py3-pip py3-pillow \
    && pip3 install django django-multiselectfield

ENTRYPOINT [ "python3", "/app/manage.py", "runserver", "0.0.0.0:8000" ]
