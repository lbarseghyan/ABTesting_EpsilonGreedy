clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/

lint/flake8: ## check style with flake8
	flake8 ABTesting_EpsilonGreedy tests

test: ## run tests quickly with the default Python
	pytest

release: dist ## package and upload a release
	twine upload dist/*

dist:  ## builds source and wheel package
	python3 setup.py sdist bdist_wheel


