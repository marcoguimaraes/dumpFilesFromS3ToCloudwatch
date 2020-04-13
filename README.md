# dumpFilesFromS3ToCloudwatch
Project to write the contents of text files in UTF-8, uploaded in S3 buckets of AWS, to Cloudwatch logs. Written in Python 3.8.

- AWSLambdaBasicExecutionRole.json file has the policy used regarding writing in Cloudwatch logs
- AWSLambdaS3ExecutionRole.json file has the policy used regarding access to S3 buckets by the lambda function
