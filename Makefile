reset-database:
	rm -f data.db
	./manage.py syncdb --noinput
	./manage.py migrate
	./manage.py loaddata fixtures/adminuser.json

server-deploy:
	fab -f deployment/fabfile.py prod deploy
