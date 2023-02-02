import pandas as pd


class data_cleaning():
  def __init__(self):

    self.treated_datetime = False
    self.removed_rows = False
    self.droped_cols = False

  def treat_datetime(self, df):

    if self.treated_datetime:
      print('already treated datetime, pass')
    
    else:

      datetime_cols = ['deb_time_line', 'fin_time_line', 'deb_time_entity', 'fin_time_entity']
      date_cols = ['work_date']
      time_cols = ['night_show', 'parade_1', 'parade_2']

      for col in time_cols:
        df[col] = pd.to_datetime(df['work_date'] + ' ' + df[col])

      for col in datetime_cols + date_cols:
        df[col] = pd.to_datetime(df[col])
      self.treated_datetime = True
  def drop_bad_rows(self, df):
    
    if self.removed_rows:
      print('already removed bad rows, pass')
    
    else:

      mask1 = (df.open_time == 0) 
      mask2 = ((df.nb_units < 0) | (df.guest_carried < 0) | (df.up_time < 0) )
      mask = mask1 | mask2

      df.drop(mask[mask].index, inplace=True)
      self.removed_rows = True
  
  def drop_rudundant_cols(self, df):

    if self.droped_cols:
      print('already dropped redundant columns, pass')
    else:
      drop_cols = ['Unnamed: 0', 'update_time', 'deb_time_hour', 'entity_type', 'ref_closing_description']
      df.drop(columns=drop_cols, axis=1, inplace=True)
      self.droped_cols = True


  