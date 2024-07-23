from textsummariser.config.configuration import ConfigurationManager
from textsummariser.components.data_transformation import DataTransformation
from textsummariser.logging import logger 


class DataTransformationTrainigPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.convert()
