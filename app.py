from Waste_Detection.logger import logging
from Waste_Detection.exception import AppException
from Waste_Detection.pipeline.training_pipeline import TrainPipeline
import sys

obj = TrainPipeline()
obj.run_pipeline()