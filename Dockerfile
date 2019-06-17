
FROM python:3.7
LABEL maintainer="SheiUn <me.sheiun@gmail.com>"
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app/
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY ./ /app
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD [ "gunicorn", "-b", "0.0.0.0:8787", "coper_files.wsgi" ]
