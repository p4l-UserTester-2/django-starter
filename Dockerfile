FROM django
ADD ./requirements.txt /django_starter/requirements.txt
WORKDIR /django_starter
RUN pip install -r ./requirements.txt
ADD . /django_starter/
EXPOSE 8000
CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]
