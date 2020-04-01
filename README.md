# Circle CI
The config.yml has the stept for build the docker image since the dockerfile and using the app.py file. Then it downloads the aws cli, pushes the new image to the ecs repository, then modifies the task definition and updates the service to use the newest task definition.

The pipeline has the folowing eviroment parameters:
* AWS_ECR_ACCOUNT_URL: this one refers to the ecs' url, to which the docker repository will be pushed
* MY_APP_PREFIX: refers to the repository's name to which the image will be pushed
* MY_ID: refers to the task definition's name that will be modified
* SERVICE_NAME: represent the service that will be modified
* AWS_SESSION_TOKEN
* AWS_SECRET_ACCESS_KEY
* AWS_SESSION_TOKEN

## App.py
Has the code with which the docker image will be created

## DockerFile
Has the commands to create the docker image



