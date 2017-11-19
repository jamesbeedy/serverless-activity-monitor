.PHONY: test
test:
	@tox

build:
	@charm build -rl DEBUG

push:
	@charm push `echo $(JUJU_REPOSITORY)`/builds/elasticsearch-base cs:~peopledatalabs/elasticsearch-base --resource elasticsearch-deb=/home/bdx/elasticsearch.deb
