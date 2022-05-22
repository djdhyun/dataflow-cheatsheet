TEMPLATE_NAME=helloworld
TEMPLATE_TAG=1.0.0

JOB_NAME=helloworld-test-run-$(date +%Y%m%dt%H%M%S)
OUTPUT=${GCS_PATH}/out/${JOB_NAME}/output

gcloud dataflow flex-template run ${JOB_NAME} \
    --template-file-gcs-location ${GCS_PATH}/templates/${TEMPLATE_TAG}/${TEMPLATE_NAME} \
    --region ${GCP_REGION} \
    --service-account-email ${GCP_SERVICE_ACCOUNT} \
    --parameters header=another_header,output=${OUTPUT}
