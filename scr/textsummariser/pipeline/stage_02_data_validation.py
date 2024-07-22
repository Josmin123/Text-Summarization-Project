from textsummariser.config.configuration import ConfigurationManager
from textsummariser.components.data_validation import DataValidation
from textsummariser.logging import logger 


class DataValidationTrainigPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()
