TEMPLATE_NAME=helloworld
TEMPLATE_TAG=1.0.0
TEMPLATE_IMAGE=${TEMPLATE_NAME}:${TEMPLATE_TAG}

# build docker image locally
docker build -t ${TEMPLATE_IMAGE} .

# To explore inside a container
echo "docker run -it --rm --entrypoint /bin/bash ${TEMPLATE_IMAGE}"

# Test if the module is importable 
docker run --rm --entrypoint /bin/bash ${TEMPLATE_IMAGE} -c 'python -c "import helloworld"'

# Run test code within a docker container
TEST_CMD="pytest -vvv helloworld_test"
docker run --rm --entrypoint /bin/bash ${TEMPLATE_IMAGE} -c "${TEST_CMD}"

# Test if the runner script exist
docker run --rm --entrypoint /bin/bash ${TEMPLATE_IMAGE} -c 'test -f ${FLEX_TEMPLATE_PYTHON_PY_FILE} && echo FLEX_TEMPLATE_PYTHON_PY_FILE=${FLEX_TEMPLATE_PYTHON_PY_FILE}'
docker run --rm --entrypoint /bin/bash ${TEMPLATE_IMAGE} -c 'test -f ${FLEX_TEMPLATE_PYTHON_SETUP_FILE} && echo FLEX_TEMPLATE_PYTHON_SETUP_FILE=${FLEX_TEMPLATE_PYTHON_SETUP_FILE}'

# Run the pipeline by DirectRunner within a docker container
TEST_ARGS="--header v1 --output output.txt"
TEST_CMD='python ${FLEX_TEMPLATE_PYTHON_PY_FILE} --runner DirectRunner'
TEST_CMD="${TEST_CMD} ${TEST_ARGS}"
TEST_CMD="${TEST_CMD} && cat output.txt*"
docker run --rm --entrypoint /bin/bash ${TEMPLATE_IMAGE} -c "${TEST_CMD}"
