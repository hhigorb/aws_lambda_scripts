variable "env_name" {
  description = "Lambda functions environment name"
}

data "aws_ecr_repository" "ecr_repository" {
  name = "lambda-archetype"
}

resource "aws_lambda_function" "lambda_function" {
  function_name = var.env_name
  timeout       = 5 # seconds
  image_uri     = "${data.aws_ecr_repository.ecr_repository.repository_url}:${var.env_name}"
  package_type  = "Image"

  role = aws_iam_role.lambda_function_role.arn

  environment {
    variables = {
      ENVIRONMENT = var.env_name
    }
  }
}

resource "aws_iam_role" "lambda_function_role" {
  name = var.env_name

  assume_role_policy = jsonencode({
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })
}
