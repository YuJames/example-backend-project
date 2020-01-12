#!/bin/bash

export BUILD_NUMBER=0.0.0
export ENVIRONMENT="$(git rev-parse --symbolic-full-name --abbrev-ref HEAD)"

export APP_HOST="0.0.0.0"
export APP_PORT="8080"
