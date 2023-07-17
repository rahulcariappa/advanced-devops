setup: requirements.txt
	pip install -r requirements.txt
	python redis-server.py
clean:
	pip freeze > requirements.txt
	vagrant destroy redisdev
	rm -rf __pycache__
