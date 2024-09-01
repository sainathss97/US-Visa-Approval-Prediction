import os
from pathlib import Path

project_name = "us_visa"

list_of_files = {
    f"{project_name}/__init__.py",
# Components -> where Stuff happens    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluvation.py",
    f"{project_name}/components/model_pusher.py",

# Project Configrations PATH for the project
    f"{project_name}/configrations/__init__.py",
    f"{project_name}/configrations/s3_operations.py",

# Output from component
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",

# All Static and Important variables
    f"{project_name}/constants/__init__.py",

# Silent Eception
    f"{project_name}/exception/__init__.py",

# Log any Event Manually
    f"{project_name}/logger/__init__.py",
    
# Pipeline -> give a flow how to execute components
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/pipeline/train_pipeline.py",

#
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

# ML Stuff
    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/feature.py",
    f"{project_name}/ml/models.py",

    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
}

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w",encoding="UTF-8") as f:
            pass
    else:
        print(f"File path is already present at {filepath}")
