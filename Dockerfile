FROM python:3.7
LABEL maintainer="SheiUn <me.sheiun@gmail.com>"
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app/
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY ./ /app
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py migrate --run-syncdb
RUN python manage.py shell -c "exec(open('myscript.py', encoding='utf-8').read())"
CMD [ "gunicorn", "-b", "0.0.0.0:8787", "coper_files.wsgi" ]
