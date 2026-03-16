## Project 1 - Serverless AI API using Amazon Bedrock

## Architecture

User → API Gateway → Lambda → Amazon Bedrock → Response

Visual diagram
                +-------------+
                |    User     |
                |  (Browser)  |
                +------+------+ 
                       |
                       v
                +-------------+
                | API Gateway |
                +------+------+ 
                       |
                       v
                +-------------+
                |   Lambda    |
                | (Python +   |
                |   boto3)    |
                +------+------+ 
                       |
                       v
                +-------------+
                | Amazon      |
                |  Bedrock    |
                | (Nova Lite) |
                +------+------+ 
                       |
                       v
                +-------------+
                |   Response  |
                +-------------+

## How It Works

1. The user sends a request to the API endpoint.

   /ask?question=What is DevOps

2. API Gateway receives the HTTP request.

3. API Gateway triggers the Lambda function.

4. Lambda extracts the query parameter and prepares the prompt.

5. Lambda invokes the Amazon Bedrock Nova Lite model using boto3.

6. Bedrock generates the AI response.

7. Lambda returns the response to API Gateway, which sends it back to the user.
