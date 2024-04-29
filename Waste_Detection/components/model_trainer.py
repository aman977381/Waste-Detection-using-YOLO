import os
import sys
import yaml
import zipfile
import shutil
from ultralytics import YOLO
from Waste_Detection.utils.main_utils import read_yaml_file
from Waste_Detection.logger import logging
from Waste_Detection.exception import AppException
from Waste_Detection.entity.config_entity import ModelTrainerConfig
from Waste_Detection.entity.artifact_entity import ModelTrainerArtifact



class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config


    

    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")

            with zipfile.ZipFile("data.zip", 'r') as zip_ref:
                zip_ref.extractall()
                print("\n Unzipping data successfull \n")
            os.system("del data.zip")

            with open("data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])
            

            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            model = YOLO(f"{model_config_file_name}.yaml")
            results = model.train(
                data = "data.yaml",
                epochs = self.model_trainer_config.no_epochs,
                batch = self.model_trainer_config.batch_size,
                # imgsz = 256,   Uncomment this to reduce size of the images
                name = "YOLOv8Model"
            )
            
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True) # Save model

            source_file_path = "runs/detect/YOLOv8Model/weights/best.pt"
            destination_directory = self.model_trainer_config.model_trainer_dir
            shutil.copy(source_file_path, destination_directory)

            #os.system("rd /s /q runs")
            os.system("rd /s /q train")
            os.system("rd /s /q valid")
            #os.system("rd /s /q test")
            os.system("del data.yaml")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov8/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact


        except Exception as e:
            raise AppException(e, sys)