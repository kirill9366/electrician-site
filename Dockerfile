# start from an official image
FROM python:3.7

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

# install our dependencies
# we use --system flag because we don't need an extra virtualenv
COPY . /opt/services/djangoapp/src
RUN pip install -r requirements.txt

# copy our project code
EXPOSE 80

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "site", "--bind", ":80", "electrician_site.wsgi:application"]
