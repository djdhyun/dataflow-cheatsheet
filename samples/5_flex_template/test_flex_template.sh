TEMPLATE_NAME=helloworld
TEMPLATE_TAG=1.0.0
TEMPLATE_IMAGE=gcr.io/${GCP_PROJECT}/${TEMPLATE_NAME}:${TEMPLATE_TAG}

# To explore inside a container
echo "docker run -it --rm --entrypoint /bin/bash ${TEMPLATE_IMAGE}"

# Test if the runner script exist
docker run --rm --entrypoint /bin/bash ${TEMPLATE_IMAGE} -c 'test -f ${FLEX_TEMPLATE_PYTHON_PY_FILE} && echo GOOD'
docker run --rm --entrypoint /bin/bash ${TEMPLATE_IMAGE} -c 'test -f ${FLEX_TEMPLATE_PYTHON_SETUP_FILE} && echo GOOD'

# Test module
docker run --rm --entrypoint /bin/bash ${TEMPLATE_IMAGE} -c 'python -c "import helloworld"'

# Test the pipeline by DirectRunner within a container
TEST_ARGS="--header v1 --output output.txt"
TEST_CMD='python ${FLEX_TEMPLATE_PYTHON_PY_FILE} --runner DirectRunner'
TEST_CMD="${TEST_CMD} ${TEST_ARGS}"
TEST_CMD="${TEST_CMD} && cat output.txt*"
docker run --rm --entrypoint /bin/bash ${TEMPLATE_IMAGE} -c "${TEST_CMD}"
