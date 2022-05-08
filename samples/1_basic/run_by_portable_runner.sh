# Your image here
IMAGE_URL=apache/beam_python3.9_sdk:2.38.0

${PYTHON} -m helloworld \
    --header v1 --output output.txt \
    --runner=PortableRunner \
    --job_endpoint=embed \
    --environment_type="DOCKER" \
    --environment_config="${IMAGE_URL}"
