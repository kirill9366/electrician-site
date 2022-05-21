python site/manage.py makemigrations
python site/manage.py migrate

python site/manage.py loaddata superuser

gunicorn --chdir site --bind :80 electrician_site.wsgi:application
