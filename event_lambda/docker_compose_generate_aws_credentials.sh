#!/bin/bash

# Execute esse script para rodar o docker-compose com as credenciais da AWS
# da sua conta. Esse script DEVE ser executado ao invés do docker-compose,
# justamente para que as credenciais da AWS sejam passadas para o container.

export AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id)
export AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key)
export AWS_REGION=$(aws configure get region)

docker-compose up -d