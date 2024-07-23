from textsummariser.constants import *
from textsummariser.utils.common import read_yaml, create_directories
from textsummariser.entity import DataIngestionConfig
from textsummariser.entity import DataValidationconfig
from textsummariser.entity import DataTransformationconfig


class ConfigurationManager:
    def __init__(
            self,
            config_filepath =CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH):

            self.config = read_yaml(config_filepath)
            self.params =read_yaml(params_filepath)

            create_directories([self.config.artifacts_root])



    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config  



    def get_data_validation_config(self) -> DataValidationconfig:
          config=self.config.data_validation

          create_directories([config.root_dir])

          data_validation_config= DataValidationconfig(
                root_dir=config.root_dir,
                STATUS_FILE=config.STATUS_FILE,
                ALL_REQUIRED_FILES= config.ALL_REQUIRED_FILES,
          ) 

          return data_validation_config   


    def get_data_transformation_config(self) ->DataTransformationconfig:
          config =self.config.data_transformation

          create_directories([config.root_dir])  

          data_transformation_config=DataTransformationconfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                tokenizer_name=config.tokenizer_name,
          )  

          return data_transformation_config    