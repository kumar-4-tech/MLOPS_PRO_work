from cnnClassifier import logger
from cnnClassifier.pipeline import stage_01_data_ingestion

STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f"Stage {STAGE_NAME} started")
    obj = stage_01_data_ingestion.DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} completed successfully")
    
except Exception as e:
    logger.exception(e)
    raise e


