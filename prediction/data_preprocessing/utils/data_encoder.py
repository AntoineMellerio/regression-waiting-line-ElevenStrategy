import pandas as pd


class data_encoder:
  def __init__(self) -> None:
    pass

  def normalize(self, df):
      result = df.copy()
      cols = ['nb_units', 'guest_carried', 'capacity', 'adjust_capacity', 'open_time', 'up_time',
            'downtime', 'nb_max_unit', 'attendance', 'temp', 'dew_point', 'feels_like', 'temp_min', 'temp_max', 'humidity',
        'wind_speed', 'wind_deg', 'wind_gust', 'rain_1h', 'rain_3h', 'snow_1h',
        'clouds_all', 'unfilled_capacity', 'until_night_show', 'until_parade_1', 'until_parade_2', 'since_deb_entity', 'until_fin_entity']
      for feature_name in cols:
          max_value = df[feature_name].max()
          min_value = df[feature_name].min()
          result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
      return result
  
  def fn_cat_onehot(self, df):

    """Generate onehoteencoded features for all categorical columns in df"""

    # NaN handing
    nan_count = df.isna().sum().sum()

    # generation
    from sklearn.preprocessing import OneHotEncoder

    model_oh = OneHotEncoder(handle_unknown="ignore", sparse=False)
    for c in df.select_dtypes("object").columns:
        matrix = model_oh.fit_transform(
            df[[c]]
        )  # get a matrix of new features and values
        names = model_oh.get_feature_names_out()  # get names for these features
        df_oh = pd.DataFrame(
            data=matrix, columns=names, index=df.index
        )  
        
        df = pd.concat([df, df_oh], axis=1)  # concat with existing df
        df.drop(
            c, axis=1, inplace=True
        )  # drop categorical column so that it is all numerical for modelling

    return df

