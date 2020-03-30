This repository contains a proof-of-concept to verify a serverless architecture mixing Lambda and Fargate.

It is structured as follows:
* **cloudformation**: set of cloudformation templates to create the infra-structure. It also conveniently allows one to remove all configured services when done.
* **docker_with_task**: a Docker container to be run as an ECS Task in Fargate. 
* **lambda**: a lambda function that triggers the Fargate task

# Setup

Before following any of the **README** on each folder, make sure you have a profile configured for AWS CLI and that it is set using an affordable AWS region such as **us-east-1**. Currently (sa-east-1) Sao Paulo is too expensive.
```
aws configure list --profile <profile-name>
```

Configure the terminal to use a named profile for the next AWS CLI commands:
```
export AWS_PROFILE=<profile-name>
```

This will ensure that all you AWS CLI commands will be run on this terminal with the proper profile and in addition not needing to expose any AWS Secrets or Keys in any version controlled file.