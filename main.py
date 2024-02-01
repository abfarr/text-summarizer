from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data transformation Stage"

try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

# stage_names = ["Data Ingestion", "Data Validation", "Data Transformation"]
# pipelines = [DataIngestionTrainingPipeline(), DataValidationTrainingPipeline(), DataTransformationTrainingPipeline()]

# for stage_name, pipeline in zip (stage_names, pipelines):
#     try:
#         logger.info(f">>>>> {stage_name} Stage started <<<<<")
#         data_stage = pipeline
#         data_stage.main()
#         logger.info(f">>>>> {stage_name} Stage completed <<<<<\n\nx========x")
#     except Exception as e:
#         logger.exception(e)
#         raise e