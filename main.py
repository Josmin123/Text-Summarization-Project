from textsummariser.pipeline.stage_01_data_ingestion import DataIngestionTrainigPipeline
from textsummariser.pipeline.stage_02_data_validation import DataValidationTrainigPipeline
from textsummariser.pipeline.stage_03_data_transformation import DataTransformationTrainigPipeline
from textsummariser.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textsummariser.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textsummariser.logging import logger


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainigPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_validation = DataValidationTrainigPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Data Transformation stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_transformation = DataTransformationTrainigPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME="Model Training stage"

try:
   logger.info(f"*****************************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   Model_trainer = ModelTrainerTrainingPipeline()
   Model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME="Model Evaluation stage"

try:
   logger.info(f"*****************************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   Model_trainer = ModelEvaluationTrainingPipeline()
   Model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



