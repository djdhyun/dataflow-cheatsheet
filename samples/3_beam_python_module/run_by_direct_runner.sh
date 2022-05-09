# Try each of these
RUNNER=BundleBasedDirectRunner
#RUNNER=DirectRunner

OUTPUT=output
#OUTPUT=${GCS_PATH}/out/output

${PYTHON} -m helloworld \
    --header v1 \
    --output ${OUTPUT} \
    --runner ${RUNNER}
