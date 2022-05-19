TEMPLATE_NAME=helloworld
JOB_NAME=helloworld-test-run-$(date +%Y%m%dt%H%M%S)
OUTPUT=${GCS_PATH}/out/${JOB_NAME}/output

# https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run
gcloud dataflow jobs run ${JOB_NAME} \
    --gcs-location ${GCS_PATH}/templates/${TEMPLATE_NAME} \
    --region ${GCP_REGION} \
    --service-account-email ${GCP_SERVICE_ACCOUNT} \
    --parameters header=another_header,output=${OUTPUT}

gsutil cp ${OUTPUT}* .
