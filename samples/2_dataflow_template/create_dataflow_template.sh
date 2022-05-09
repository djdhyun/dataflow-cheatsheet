TEMPLATE_NAME=helloworld

${PYTHON} -m helloworld \
    --runner DataflowRunner \
    --project ${GCP_PROJECT} \
    --region ${GCP_REGION} \
    --temp_location ${GCS_PATH}/temp \
    --staging_location ${GCS_PATH}/staging \
    --template_location ${GCS_PATH}/templates/${TEMPLATE_NAME}

gsutil cp ./helloworld_metadata ${GCS_PATH}/templates/${TEMPLATE_NAME}_metadata
