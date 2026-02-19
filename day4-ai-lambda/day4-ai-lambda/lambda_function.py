import boto3
import json

def lambda_handler(event, context):
    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

    prompt = "Explain AWS Lambda in one simple paragraph."

    response = bedrock.invoke_model(
        modelId="anthropic.claude-3-haiku-20240307-v1:0",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 200
        })
    )

    result = json.loads(response["body"].read())
    answer = result["content"][0]["text"]

    return {
        "statusCode": 200,
        "body": answer
    }
