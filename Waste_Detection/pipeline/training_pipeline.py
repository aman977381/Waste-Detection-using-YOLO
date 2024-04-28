import sys, os
from Waste_Detection.logger import logging
from Waste_Detection.exception import AppException
from Waste_Detection.components.data_ingestion import DataIngestion
#from Waste_Detection.components.data_validation import DataValidation
#from Waste_Detection.components.model_trainer import ModelTrainer


from Waste_Detection.entity.config_entity import (DataIngestionConfig)

from Waste_Detection.entity.artifact_entity import (DataIngestionArtifact)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        #self.data_validation_config = DataValidationConfig()
        #self.model_trainer_config = ModelTrainerConfig()


    
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try: 
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config =  self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise AppException(e, sys)
        
    
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise AppException(e, sys)