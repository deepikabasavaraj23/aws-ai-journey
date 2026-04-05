import json
import boto3
import urllib.parse

# AWS clients
s3 = boto3.client("s3")
bedrock = boto3.client("bedrock-runtime")

def lambda_handler(event, context):

    print("Event:", event)

    # Get bucket name
    bucket = event["Records"][0]["s3"]["bucket"]["name"]

    # Decode file name (important fix)
    key = urllib.parse.unquote_plus(
        event["Records"][0]["s3"]["object"]["key"]
    )

    print("Bucket:", bucket)
    print("File:", key)

    # Read file from S3
    response = s3.get_object(Bucket=bucket, Key=key)

    print("File read successfully")

    # Prompt (simple version)
    prompt = f"Give a general description for an image named {key}"

    body = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ]
    })

    # Call Bedrock
    ai_response = bedrock.invoke_model(
        modelId="amazon.nova-lite-v1:0",
        body=body,
        contentType="application/json",
        accept="application/json"
    )

    result = json.loads(ai_response["body"].read())
    answer = result["output"]["message"]["content"][0]["text"]

    print("AI Output:", answer)

    return {
        "statusCode": 200,
        "body": answer
    }
