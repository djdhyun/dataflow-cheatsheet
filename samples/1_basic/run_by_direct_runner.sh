# Try each of these
#RUNNER=BundleBasedDirectRunner
RUNNER=DirectRunner

${PYTHON} -m helloworld \
    --header v1 --output output.txt \
    --runner ${RUNNER} \
