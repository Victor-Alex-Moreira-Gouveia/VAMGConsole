FROM python:3.13.2

WORKDIR /home
COPY ./index.py .
CMD [ "python", "./index.py" ]