## Project 1 - Serverless AI API using Amazon Bedrock

Architecture:

User → API Gateway → Lambda → Amazon Bedrock → Response

How it works:

1. User sends request:
/ask?question=What is DevOps

2. API Gateway receives the request

3. API Gateway triggers AWS Lambda

4. Lambda extracts the question parameter

5. Lambda calls Amazon Bedrock (Nova Lite model)

6. Bedrock generates the response

7. Lambda returns the answer
