# US Visa Approval Prediction

 MLOPS with US Visa Approval

## Git Commands

```bash
  `  git init`
    
  `  git add .`
     
   ` git commit -m "Updated"`
     
  `  git push origin main`
```

## SCHEMA yaml

Used for Data Validation by Checking original Database with the transformed train, test csv files we create this based on the EDA taht we performed earlier.

## How to Run ?

### 1.  Enviorment

```bash
conda create -n visa python=3.8 -y
```

### 2. Requirments

```bash
pip install -r requirements.txt
```

### 3. Database MongoDb Free tier

1. Connection String
2. Pyhton Driver

### 4. Workflow

0. DATA Access

1. DATA Ingestion Component - Example ✅

    1. Constant  "Declaration of Static variables in Proj"
        + Column length
        + Column exsist
        + Detect Data Drift
    2. entity>>`config_entity` "Managing Paths"
    3. entity>>`artifact_entity` "Output from component"
    4. component>>`data_ingestion.py` "stages like data acess , data transformations..."
    5. pipeline>>`training_pipeline.py` or `prediction_pipeline.py` "tackle above components in a single go"
    6. `app.py` or `demo.py` >>    Code testing is done by `demo.py` -> runs the code whenever needed 
        Full code execution in  one go is available in `app.py` 

2. DATA Validation Component (SCHEMA Verification) ✅
3. DATA Transformation Component ✅
4. Model Training Component ✅
5. Model Evaluation Component  ✅
6. Model Pusher Component ->S3 Bucket ✅
7. Prediction Pipeline, User App
8. User App In Fast API

### 5. Running and web Interface

check logs if there is any exception

`python app.py`

`localhost:8080` -> in browser.

### 6. enviorment Variables Setting

Export Enviorment variables before running the code. create them before hand.

#### MONGODB_URL

`export MONGODB_URL="mongodb+srv://<user>:<pass>..."`

#### AWS_ACCESS_KEY_ID_ENV_KEY

`export AWS_ACCESS_KEY_ID="<AWS_ACCESS_KEY>"`

#### AWS_SECRET_ACCESS_KEY_ENV_KEY

`export AWS_SECRET_ACCESS_KEY="<AWS_SECRET_ACCESS_KEY>"`

----

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console

## 2. Create IAM user for deployment

 #with specific access

 1. EC2 access : It is virtual machine

 2. ECR: Elastic Container registry to save your docker image in aws


 #Description: About the deployment

 1. Build docker image of the source code

 2. Push your docker image to ECR

 3. Launch Your EC2 

 4. Pull Your image from ECR in EC2

 5. Lauch your docker image in EC2

 #Policy:

 1. AmazonEC2ContainerRegistryFullAccess

 2. AmazonEC2FullAccess

 
## 3. Create ECR repo to store/save docker image

` - Save the URI: 136566696263.dkr.ecr.us-east-1.amazonaws.com/mlproject`

 
## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine
 
 #optinal
```bash
 sudo apt-get update -y

 sudo apt-get upgrade
 
 #required

 curl -fsSL https://get.docker.com -o get-docker.sh

 sudo sh get-docker.sh

 sudo usermod -aG docker ubuntu

 newgrp docker
 ```
# 6. Configure EC2 as self-hosted runner

    setting>actions>runner>new self hosted runner> choose os> then run command one by one

# 7. Setup github secrets

+ AWS_ACCESS_KEY_ID
+ AWS_SECRET_ACCESS_KEY
+ AWS_DEFAULT_REGION
+ ECR_REPO 
