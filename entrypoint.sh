python site/manage.py makemigrations about_us authentication course_projects demo_exam library main news students
python site/manage.py migrate

python site/manage.py loaddata superuser

gunicorn --chdir site --bind :80 electrician_site.wsgi:application
