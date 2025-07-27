# US Visa Approval Prediction

 MLOPS with US Visa Approval

## Git Commands

```bash
    git init
    
    git add .
     
    git commit -m "Updated"
     
    git push origin main
```

## enviormrnt Variables Setting

"export KEY = VALUE"
    export MONGODB_URL="mongodb+srv://sainath:sainath@cluster0.1bixffs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

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

### 5. Enviorment variables

Export Enviorment variables before running the code. create them before hand.

#### MONGODB_URL

`export MONGODB_URL="mongodb+srv://<user>:<pass>..."`

#### AWS_ACCESS_KEY_ID_ENV_KEY

`export AWS_ACCESS_KEY_ID="<AWS_ACCESS_KEY>"`

#### AWS_SECRET_ACCESS_KEY_ENV_KEY

`export AWS_SECRET_ACCESS_KEY="<AWS_SECRET_ACCESS_KEY>"`
