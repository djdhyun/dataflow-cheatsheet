ROOTDIR=../../
VENV=${ROOTDIR}/.venv/bin

venv:
	cd ${ROOTDIR} && make venv

.PHONY: lint
lint: venv
	$(VENV)/isort --diff --check-only helloworld helloworld_test
	$(VENV)/black --diff --check helloworld helloworld_test
	$(VENV)/pylint helloworld helloworld_test

.PHONY: format
format: venv
	$(VENV)/isort helloworld helloworld_test
	$(VENV)/black helloworld helloworld_test

.PHONY: test
test: venv
	$(VENV)/pytest -vvv helloworld_test

.PHONY: docker-test
docker-test: venv
	sh test_docker_image.sh

.PHONY: coverage
coverage: venv
	$(VENV)/pytest \
		--cov-report term-missing:skip-covered \
		--cov-report html \
		--cov=helloworld \
		-vvv \
		helloworld_test \
		| tee pytest-coverage.txt
