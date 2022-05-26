ARG BASE_IMAGE_TAG=flex_templates_base_image_release_20220516_RC00
#FROM gcr.io/dataflow-templates-base/python3-template-launcher-base
FROM gcr.io/dataflow-templates-base/python39-template-launcher-base:${BASE_IMAGE_TAG}

ARG WORKDIR=/opt/dataflow
RUN mkdir -p ${WORKDIR}/templates
WORKDIR ${WORKDIR}

ARG TEMPLATE_NAME=helloworld
COPY setup.py ${WORKDIR}/setup.py
COPY ${TEMPLATE_NAME} ${WORKDIR}/${TEMPLATE_NAME}
COPY ${TEMPLATE_NAME}_test ${WORKDIR}/${TEMPLATE_NAME}_test
COPY pytest.ini ${WORKDIR}/pytest.ini

ENV FLEX_TEMPLATE_PYTHON_PY_FILE=${WORKDIR}/${TEMPLATE_NAME}/app.py
ENV FLEX_TEMPLATE_PYTHON_SETUP_FILE=${WORKDIR}/setup.py

# Install apache-beam and other dependencies to launch the pipeline
RUN python setup.py install
