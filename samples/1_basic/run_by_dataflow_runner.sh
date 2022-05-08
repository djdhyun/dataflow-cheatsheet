# To find out more configuration about DataflowRunner,
# check `class GoogleCloudOptions` in `${BEAM_HOME}/options/pipeline_options.py`

JOB_NAME=helloworld-test-run-$(date +%Y%m%dt%H%M%S)
OUTPUT=${GCS_PATH}/out/${JOB_NAME}/output

${PYTHON} -m helloworld \
    --header v1 --output ${OUTPUT} \
    --runner DataflowRunner \
    --job_name ${JOB_NAME} \
    --project ${GCP_PROJECT} \
    --region ${GCP_REGION} \
    --service_account_email ${GCP_SERVICE_ACCOUNT} \
    --temp_location ${GCS_PATH}/temp \
    --staging_location ${GCS_PATH}/staging 

gsutil cp ${OUTPUT}* .
