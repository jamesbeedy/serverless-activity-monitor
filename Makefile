.PHONY: lint
lint:
	@tox
test:
	@nosetests3 --verbosity=2
