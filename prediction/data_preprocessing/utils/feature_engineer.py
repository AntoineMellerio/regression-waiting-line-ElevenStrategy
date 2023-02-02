import pandas as pd
import numpy as np
import holidays


class feature_engineer:
  def __init__(self) -> None:
    pass

  def modify_features(self, df):

    df = df.copy()
    self.take_log_y(df)
    self.add_public_holidays(df)
    self.compute_unfilled_capacity(df)
    self.show_parade_time(df)
    self.open_closed_time(df)
    self.check_park(df)
    self.encode_datetime(df)
    self.drop_rudundant_cols(df)

    return df

    
  def take_log_y(self, X):
    X.loc[:, "log_wait_time_max"] = np.log(1 + X.wait_time_max)

  def add_public_holidays(self, X):
    # Add public holidays
    fr_holidays = holidays.France(years=X.work_date.dt.year.unique())
    X.loc[:, "is_holiday"] = X.work_date.isin( fr_holidays.keys())
  
  def compute_unfilled_capacity(self, X):
    # Unfilled capacity
    X.loc[:, "unfilled_capacity"] = X.adjust_capacity - X.guest_carried

  def show_parade_time(self, X):
    # Show time parade time
    X.loc[:, "until_night_show"] =  ( X.night_show -X.deb_time_line ).abs().dt.seconds 
    X.loc[:, "until_parade_1"] =  ( X.parade_1 -X.deb_time_line ).abs().dt.seconds 
    X.loc[:, "until_parade_2"] =  ( X.parade_2 -X.deb_time_line ).abs().dt.seconds 

    X.loc[( X.night_show <X.deb_time_line ), 'until_night_show'] = 0
    X.loc[( X.parade_1 <X.deb_time_line ), 'until_parade_1'] = 0
    X.loc[( X.parade_2 <X.deb_time_line ), 'until_parade_2'] = 0
    X = X.fillna(-1)
  
  def open_closed_time(self, X):
    X.loc[:, "since_deb_entity"] =  ( X.deb_time_line -X.deb_time_entity  ).abs().dt.seconds 
    X.loc[:, "until_fin_entity"] =  ( X.fin_time_entity -X.deb_time_line).abs().dt.seconds 

  def check_park(self, X):
    X.loc[:, "is_PortAventura_World"] = X.park.isin(['PortAventura World'])

  def encode_datetime(self, X):
    # Encode the date information from the DateOfDeparture columns
    X.loc[:, "year"] = X["deb_time_line"].dt.year
    X.loc[:, "month"] = X["deb_time_line"].dt.month
    X.loc[:, "day"] = X["deb_time_line"].dt.day
    X.loc[:, "hour"] = X["deb_time_line"].dt.hour
    X.loc[:, "quarter"] = X["deb_time_line"].dt.minute
    X.loc[:, "weekday"] = X["deb_time_line"].dt.weekday

  def drop_rudundant_cols(self, df):
    # 
    cols= ['deb_time_line', 'night_show', 'parade_1', 'parade_2', 'work_date', 'fin_time_line', 'fin_time_entity', 'deb_time_entity','park', 'weather_icon','weather_id', 'wait_time_max']
    df.drop(columns=cols, axis=1, inplace=True)

