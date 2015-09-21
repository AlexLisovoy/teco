# Some simple testing tasks (sorry, UNIX only).

FLAGS=


flake:
	python setup.py check -rm
	flake8 teco

develop:
	python setup.py develop

test: flake develop
	python -m unittest discover

cov cover coverage: flake
	@coverage erase
	@coverage run -m unittest discover
	@coverage report
	@coverage html
	@echo "open file://`pwd`/coverage/index.html"

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '@*' `
	rm -f `find . -type f -name '#*#' `
	rm -f `find . -type f -name '*.orig' `
	rm -f `find . -type f -name '*.rej' `
	python setup.py clean
	rm -f .coverage
	rm -rf coverage

.PHONY: all flake develop test cov clean
