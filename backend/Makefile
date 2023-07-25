run:
	python manage.py collectstatic --noinput
	python manage.py makemigrations
	python manage.py migrate
	python manage.py csv_import
	gunicorn --bind 0.0.0.0:$${FOODGRAM_PORT} foodgram.wsgi:application