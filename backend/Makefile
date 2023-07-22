run:
	python manage.py collectstatic --noinput
	python manage.py migrate
	python manage.py csv_import
	gunicorn --bind 0.0.0.0:8000 foodgram.wsgi:application