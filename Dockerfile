# FROM tiangolo/uwsgi-nginx-flask:python3.11
# ENV STATIC_URL /static
# ENV STATIC_PATH /var/www/app/static
# COPY ./ ./
# COPY ./requirements.txt ./requirements.txt
# RUN pip install -r ./requirements.txt
FROM python:3.11

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . ./app
WORKDIR /app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]