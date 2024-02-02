FROM python:3.11

COPY ./server /twerkout_backend/server
COPY manage.py /twerkout_backend/
COPY requirements.txt /twerkout_backend/

WORKDIR /twerkout_backend/

RUN pip install -r ./requirements.txt

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000