.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	pip install pipenv
	pipenv --python 3.8
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest

test:
	@echo "Starting tests."
	pipenv run pytest tests/tests.py > results.txt

run:
	@echo "Running Python app."
	pipenv run python app.py >> results.txt

deploy:
	@echo "Adding and Committing results.txt to git."
	git add results.txt
	git commit -m "Lab_2: commiting by makefile"
	git push