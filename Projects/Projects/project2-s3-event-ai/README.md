Project 2: AWS S3 + Lambda + Bedrock (Event-Driven AI System)
📌 Description
This project demonstrates an event-driven serverless AI pipeline built using AWS services. The system automatically processes files uploaded to Amazon S3 and generates AI-based responses using Amazon Bedrock.

When a user uploads an image to an S3 bucket, it triggers an AWS Lambda function. The Lambda function reads the uploaded file and sends relevant input to Amazon Bedrock, which generates an AI response. The entire process is automated without any manual intervention.

🧠 Architecture
S3 (Upload File)
      ↓
Lambda (Triggered Automatically)
      ↓
Bedrock (AI Processing)
      ↓
AI Output (CloudWatch Logs)


⚙️ Services Used
Amazon S3 – Stores uploaded files
AWS Lambda – Processes the file automatically
Amazon Bedrock – Generates AI responses
IAM – Manages permissions for secure access
CloudWatch – Logs and monitors execution

🔥 Key Features
Event-driven architecture (no manual trigger)
Automatic Lambda execution on file upload
Integration with AI model (Bedrock)
Serverless (no infrastructure management)
Real-time processing pipeline

🔄 Workflow
User uploads an image to S3 bucket
S3 triggers Lambda function automatically
Lambda reads file using s3:GetObject
Lambda sends input to Bedrock
Bedrock generates AI response
Output is logged in CloudWatch

🎯 Learning Outcomes
Understanding event-driven architecture
Working with S3 triggers
Managing IAM roles and permissions
Integrating AWS services
Building serverless AI applications

💡 Interview Summary (1–2 lines)
Built an event-driven AI system using AWS S3, Lambda, and Bedrock where uploading a file automatically triggers processing and generates AI-based output.
