FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /app
ADD . /app/
COPY requirement.txt .
RUN pip3 install -r requirement.txt
COPY . .
EXPOSE 8000
CMD python manage.py runserver

ENV DJANGO_SETTINGS_MODULE=himalaya.settings
ENV DB_HOST=localhost
ENV DB_PORT=3306
ENV DB_NAME='Tech__himalaya'
ENV DB_USER=MYSQL
ENV DB_PASSWORD=''
