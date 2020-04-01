# Intro
This folder contains a 'Dockerfile' to create a task on Fargate.

The 'task.py' is used as proof-of-concept to check XGBoost can be run on a serverless maner.

# Setup

Build the image defined on the Dockerfile
```
docker build -t task_container .
```

Log in to the registry (check *'cloudformation'* folder if you didn't created it yet)
```
$(aws ecr get-login --no-include-email --region us-east-1)
```

Retrieve the registry URI
```
aws ecr describe-repositories
```

Tag the image by appending the ':latest' string on the URI. The repositoryUri can be found on the output of the previous command.
```
docker tag task_container:latest <registry-uri-from-the-previous-command>:latest
```

Upload the docker image to the registry
```
docker push <registry-uri-from-the-previous-command>:latest
```

If following the steps for the first time, go to the *"lambda"* folder now.

# Clean up
The repositoryName can be found by the following command line:
```
aws ecr describe-repositories
```

To empty your repository issue the command below:
```
aws ecr batch-delete-image --repository-name <repository-name> --image-ids imageTag=latest
```