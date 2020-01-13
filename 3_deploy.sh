# #!/bin/bash
echo "1) INITIALIZING ENVIRONMENT"
[ -f ./public_env.sh ] && . ./public_env.sh
[ -f ./.private_env.sh ] && . ./.private_env.sh

echo "2) DEPLOYING TO KUBERNETES"
{
  if ! kubectl get ns $NAMESPACE; then
    echo "Creating missing namespace ${NAMESPACE}"
    kubectl create ns ${NAMESPACE}
  fi

  for i in `find ./kube/*.yaml`; 
  do
    cat $i | envsubst > ./temp/temp.yaml
    kubectl apply -f ./temp/temp.yaml
  done
} ||
{
  echo -e "\e[1;5;31mFailed kubernetes deployment"
}

echo "3) CLEANING"
unset DOCKER_IMAGE
# rm temp.yaml
