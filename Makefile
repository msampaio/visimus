reset-database:
	rm -f data.db
	./manage.py syncdb --noinput
	./manage.py migrate
	./manage.py loaddata fixtures/adminuser.json
