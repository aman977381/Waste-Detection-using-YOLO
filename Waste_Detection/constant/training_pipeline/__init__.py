"""
Data Ingestion
"https://drive.google.com/file/d/1ECfl3dtYyfivY8kYPq7RHUBTjC-2vf61/view?usp=share_link"
""
"https://drive.google.com/file/d/1nEYaOxDQgdVe6Kzi-tldN25LdCKWP66o/view?usp=drive_link"
"""

ARTIFACTS_DIR: str = "artifacts"

DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/1oyJz7Dl3kJZ7el0ExDQFQlggFPVvZ35Q/view?usp=sharing"

"""
Data Validation
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "valid","test","data.yaml"]

"""
Model Trainer
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov8n.pt"

MODEL_TRAINER_NO_EPOCHS: int = 200

MODEL_TRAINER_BATCH_SIZE: int = 64
