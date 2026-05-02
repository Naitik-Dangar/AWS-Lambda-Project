# AWS-Lambda-Project
This is the lambda function for a Simple AWS project incorporating s3, lambda, and SNS. The Lambda function is automatically triggered by a put event in a specified s3 bucket. When a new image is uploaded, the function retrieves the file, calculates the total number of pixels, and publishes the result to an SNS topic (my personal email).
