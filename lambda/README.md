# Setup

Create the S3 bucket to hold the Lambda package. You will have to define an unique bucket name. Take note of it because it will be used in other steps.

```
aws s3 mb s3://<bucket-name>
```

# Package and deploy

Once you have written what you need on the Lambda function, update the Python package (with a virtual environment):

1-Create a virtual environment:

```
python3 -m venv v-env
```

2-Active the environment:

```
source v-env/bin/activate
```

3-Install dependencies:

```
pip install -r requirements.txt
```

4-Deactivate the environment:

```
deactivate
```

5-Create the zip package:

```
cd v-env/lib/python3.7/site-packages
zip -r9 ${OLDPWD}/function.zip .
```

6-Add the lambda function to the zip package:
```
cd $OLDPWD
zip -g function.zip lambda_function.py
```

7-Upload the package to the S3 Bucket:
```
aws s3 cp function.zip s3://<bucket-name>/
```

# Revisit the *"cloudformation"* folder

In case you didn't finish the instructions on the *"cloudformation"* folder, now it is the time to revisit it.

# Cleanup

In case the bucket is no longer needed make sure to dispose of its contents and the bucket itself:
```
aws s3 rm s3://<bucket-name>/function.zip
aws s3 rb s3://<bucket-name>
```
