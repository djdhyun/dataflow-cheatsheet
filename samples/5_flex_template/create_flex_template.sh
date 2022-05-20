TEMPLATE_NAME=helloworld
TEMPLATE_TAG=1.0.5

TEMPLATE_PATH=${GCS_PATH}/templates/${TEMPLATE_NAME}
TEMPLATE_IMAGE=gcr.io/${GCP_PROJECT}/${TEMPLATE_NAME}:${TEMPLATE_TAG}

# build docker image locally
#docker build -t ${TEMPLATE_IMAGE} .

# build & upload image
gcloud builds submit --tag ${TEMPLATE_IMAGE} .

gcloud dataflow flex-template build ${GCS_PATH}/templates/${TEMPLATE_TAG}/${TEMPLATE_NAME} \
    --image ${TEMPLATE_IMAGE} \
    --sdk-language PYTHON \
    --metadata-file ${TEMPLATE_NAME}_metadata
