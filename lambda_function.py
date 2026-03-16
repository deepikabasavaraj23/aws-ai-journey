import json
import boto3

bedrock = boto3.client("bedrock-runtime")

def lambda_handler(event, context):

    print("Received event:", event)

    query_params = event.get("queryStringParameters", {})
    question = query_params.get("question", "Explain cloud computing")

    print("User question:", question)

    prompt = f"Answer this clearly: {question}"

    body = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": [
                    {"text": prompt}
                ]
            }
        ]
    })

    try:
        response = bedrock.invoke_model(
            modelId="amazon.nova-lite-v1:0",
            body=body,
            contentType="application/json",
            accept="application/json"
        )

        result = json.loads(response["body"].read())

        answer = result["output"]["message"]["content"][0]["text"]

        print("Generated answer:", answer)

        return {
            "statusCode": 200,
            "body": answer
        }

    except Exception as e:

        print("Error occurred:", str(e))

        return {
            "statusCode": 500,
            "body": "Error generating AI response"
        }
