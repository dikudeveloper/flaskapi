# Python base image - Alpine Linux distribution is optimized for a small image size.
FROM python:3.7.2-alpine

# set working directory in the container
WORKDIR /usr/src/app

# Add and install project requirements into the container.
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Add app on local filesystem to container.
COPY . /usr/src/app

# run server
CMD python manage.py run -h 0.0.0.0
