from utils.data_cleaning import data_cleaning
from utils.feature_engineer import feature_engineer
from utils.data_encoder import data_encoder


class DataFactory:
  def get_formatter(self, format):
    if format == 'Cleaning':
      return data_cleaning()
    elif format == 'Features':
      return feature_engineer()
    elif format == 'Encoding':
      return data_encoder()
    else:
      raise ValueError(format)