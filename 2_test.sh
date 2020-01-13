#!/bin/bash
echo "1) INITIALIZING ENVIRONMENT"
[ -f ./public_env.sh ] && . ./public_env.sh
[ -f ./.private_env.sh ] && . ./.private_env.sh
ENV_FILE="./temp/.env"
printenv > "${ENV_FILE}"

echo "2) RUNNING TESTS"
flake8 src && echo "PASSED LINTING" || echo "FAILED LINTING"

echo "3) RUN APPLICATION"
docker rm "${APP_NAME}"
docker run --name="${APP_NAME}" --env-file="${ENV_FILE}" -p="${APP_PORT}:${APP_PORT}" "${DOCKER_IMAGE_NAME}"

echo "4) CLEANING"
rm ./temp/.env