FLAKE8=flake8

install:
	pip install -r requirements.txt

test:
	py.test .

lint:
	$(FLAKE8) .
