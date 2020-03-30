# Setup

## VPC
Validate that the VPC template is correct:
```
aws cloudformation validate-template --template-body file://public-vpc.yml
```

Use the template to create the VPC:
```
aws cloudformation deploy --stack-name public-vpc-stack --template-file public-vpc.yml
```

## Fargate
Validate that the Fargate template is correct:
```
aws cloudformation validate-template --template-body file://fargate-fauna.yml
```

Use the template to create an ECR to hold docker images, ECS Cluster, Fargate Task Definition, Execution Roles, etc.
```
aws cloudformation deploy --stack-name fargate-fauna --template-file fargate-fauna.yml --capabilities CAPABILITY_NAMED_IAM
```

After this step go to the folder *"docker_with_task"* and follow its instructions in order to push a docker image to the newly created ECR. It will be used to run the task on Fargate.

## Lambda

Make sure you completed the steps above before visiting the *"lambda"* folder. Please finish what is instructed there. Only then proceed with the final stack instructions described below.

Validate that the Lambda template is correct:
```
aws cloudformation validate-template --template-body file://lambda.yml
```

Use the template to create the Lambda function and its Execution Role. The *bucket-name* and *key-name* comes from the instructions on *"lambda"* folder.
```
aws cloudformation deploy --stack-name lambda-stack --template-file lambda.yml --parameter-overrides S3Bucket="<bucket-name>" PackageName="<package-name>" --capabilities CAPABILITY_NAMED_IAM
```

## Enjoy all the moving parts.

# Clean-up
First execute the commands from the *Clean-up* section in the *"lambda"* folder. Once finished, execute the *"Clean-up"* from the *"docker_with_task"*.

When done, proceed to the final clean-up:
```
aws cloudformation delete-stack --stack-name lambda-stack
aws cloudformation delete-stack --stack-name fargate-fauna
aws cloudformation delete-stack --stack-name public-vpc-stack
```