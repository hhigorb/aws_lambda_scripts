#!/bin/bash

# Before running this script, make sure you created the ECR repository and configured 
# the AWS CLI with the following command:
# aws configure

# You can get the ECR information by entering the ECR console in AWS and clicking on
# the repository you created. The information will be displayed on the right side of
# the screen on the "View push commands" button.

read -p "Enter the ECR password-stdin (e.g., 123456789012): " ecr_password_stdin
read -p "Enter the ECR Repository Name (e.g., docker-python-lambda-scripts): " ecr_repository_name
read -p "Enter AWS Region (e.g., us-east-1): " aws_region

aws ecr get-login-password --region $aws_region \
  | docker login --username AWS --password-stdin $ecr_password_stdin.dkr.ecr.$aws_region.amazonaws.com

docker build -t $ecr_repository_name .
docker tag $ecr_repository_name:latest \
  $ecr_password_stdin.dkr.ecr.$aws_region.amazonaws.com/$ecr_repository_name:latest
docker push $ecr_password_stdin.dkr.ecr.$aws_region.amazonaws.com/$ecr_repository_name:latest

