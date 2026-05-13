import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = 'mlproject'


list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/data_ingestion",
    f"src/{project_name}/components/data_transformation",
    f"src/{project_name}/components/model_training",
    f"src/{project_name}/components/model_monitoring",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline",
    f"src/{project_name}/pipelines/prediction_pipeline",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "dockerfile",
    "requirements.txt",
    "setup.py"
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath))or (os.path.getsize(filepath) ==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating Empty file : {filepath}")

    else:
        pass
        logging.info(f"{filename} is already exist")