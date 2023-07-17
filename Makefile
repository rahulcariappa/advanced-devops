redis-server:
	python redis-server.py
setup: requirements.txt
	pip install -r requirements.txt
	/usr/local/bin/python redis-server.py
clean:
	pip freeze > requirements.txt
	rm -rf vagrantenv
	rm -rf __pycache__
	find -iname "*.pyc" -delete
