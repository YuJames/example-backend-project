#!/bin/bash
echo "1) INITIALIZING ENVIRONMENT"
[ -f ./public_env.sh ] && . ./public_env.sh
[ -f ./.private_env.sh ] && . ./.private_env.sh

echo "2) BUILDING DOCKER IMAGE"
DOCKERFILE_FILLED="./temp/filled_dockerfile"
cat Dockerfile | envsubst | > ${DOCKERFILE_FILLED}
docker build . -f="${DOCKERFILE_FILLED}" -t="${DOCKER_IMAGE_NAME}"

echo "3) PUSHING DOCKER IMAGE"
docker push ${DOCKER_IMAGE_NAME}

echo "4) CLEANING"
rm "${DOCKERFILE_FILLED}"
