# Day 1 – AWS S3 + Lambda Project

## What I built
- Created an S3 bucket and uploaded a text file
- Created an IAM role with least-privilege access
- Built an AWS Lambda function using Python (boto3)
- Lambda reads file content from S3
- Verified execution using CloudWatch logs

## AWS Services Used
- Amazon S3
- AWS Lambda
- IAM
- CloudWatch

## Output
Lambda successfully returned:
Hello AWS from Day 1

---

# Day 2 – AWS API Gateway + Lambda (Public API)

## What I built
- Exposed the existing Lambda function using Amazon API Gateway (HTTP API)
- Created GET endpoint `/read-file`
- Deployed API using `prod` stage with auto-deploy enabled
- Connected API Gateway to Lambda integration
- Debugged and fixed Lambda timeout issues using CloudWatch logs

## AWS Services Used
- Amazon API Gateway (HTTP API)
- AWS Lambda
- Amazon S3
- IAM
- CloudWatch

## API Endpoint
GET /read-file

Example:
https://1172s7dk3e.execute-api.ap-south-1.amazonaws.com/prod/read-file


## Output
Hello AWS from Day 1
