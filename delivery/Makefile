install:
	pip install -e .['dev']

run:
	FLASK_APP=./delivery/app.py \
	FLASK_ENV=development \
	flask run

clean:
	rm -rf .cache
	rm -rf .build
	rm -rf .dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf docs/_build
	pip install -e .['dev'] --upgrade --no-cache

test:
	pytest tests -v --cov=./delivery
