#!/bin/bash

# project settings
BUILD_NUMBER=0.0.0
ENVIRONMENT="$(git rev-parse --symbolic-full-name --abbrev-ref HEAD)"
if [[ $ENVIRONMENT == "production" ]]; then
    NAMESPACE="production"
else
    NAMESPACE="development"
fi
GIT_HASH=$(git log --pretty=format:'%h' -n 1)
DOCKER_BASE_URL="docker.io"
USER_NAME="33ngineer"
APP_NAME="restaurant-rest-api"
DOCKER_URL="${DOCKER_BASE_URL}/${USER_NAME}/${APP_NAME}"
DOCKER_IMAGE_NAME="${DOCKER_URL}:v${BUILD_NUMBER}-${GIT_HASH}"
# app settings
APP_HOST="0.0.0.0"
APP_PORT="8080"

# exports
export BUILD_NUMBER
export ENVIRONMENT
export NAMESPACE
export APP_NAME
export APP_HOST
export APP_PORT
export DOCKER_IMAGE_NAME
