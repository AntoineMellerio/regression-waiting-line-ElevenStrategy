
import pandas as pd

def MergeDataSource(PATH):


    attendance = pd.read_csv(PATH + "attendance.csv")
    entity_schedule = pd.read_csv(PATH + "entity_schedule.csv")
    link_attraction_park = pd.read_csv(PATH + "link_attraction_park.csv", sep=";")
    parade_night_show = pd.read_excel(PATH + "parade_night_show.xlsx")
    waiting_times = pd.read_csv(PATH + "waiting_times.csv")
    weather_data = pd.read_csv(PATH + "weather_data.csv")

    waiting_times.WORK_DATE = pd.to_datetime(waiting_times.WORK_DATE)
    waiting_times.FIN_TIME = pd.to_datetime(waiting_times.FIN_TIME)
    attendance.USAGE_DATE = pd.to_datetime(attendance.USAGE_DATE)

    wt_linked = waiting_times.merge(link_attraction_park, left_on="ENTITY_DESCRIPTION_SHORT", right_on="ATTRACTION")
    wt_linked.drop("ATTRACTION", axis=1, inplace=True)


    # Attendance 
    wt_linked_att = wt_linked.merge(attendance, left_on=['WORK_DATE', 'PARK'], right_on=['USAGE_DATE', "FACILITY_NAME"])
    wt_linked_att.drop(["USAGE_DATE", "FACILITY_NAME"], axis=1, inplace=True)

    # Entity Scedule
    entity_schedule.WORK_DATE = pd.to_datetime(entity_schedule.WORK_DATE)
    wt_linked_att_ent = wt_linked_att.merge(
        entity_schedule,
        on=["WORK_DATE", "ENTITY_DESCRIPTION_SHORT"],
        suffixes=('_LINE', '_ENTITY')
    )

    parade_night_show.WORK_DATE = pd.to_datetime(parade_night_show.WORK_DATE)
    final = wt_linked_att_ent.merge(parade_night_show.drop('Unnamed: 0', axis=1),on="WORK_DATE")

    weather_keep = ['dt_iso', 'timezone', 'temp', 'dew_point', 'feels_like', 'temp_min', 'temp_max', 'humidity', 'wind_speed', 'wind_deg','wind_gust','rain_1h', 'rain_3h', 'snow_1h','clouds_all', 'weather_id', 'weather_main', 'weather_icon']
    weather_data = weather_data[weather_keep]
    weather_data = weather_data[weather_data['dt_iso'] >= "2018-01-01"].fillna(0)
    weather_data.dt_iso = pd.to_datetime(weather_data.dt_iso.map(lambda x: x[:-4]))
    weather_data['summer_time'] = weather_data.timezone.map(lambda x: x==7200)
    weather_data['DEB_TIME_HOUR'] =  weather_data.dt_iso.map(lambda x: x.hour)
    weather_data['WORK_DATE'] =  weather_data.dt_iso.map(lambda x: x.date)
    weather_data = weather_data.drop(columns=['timezone', 'dt_iso'])

    weather_data.WORK_DATE = pd.to_datetime(weather_data.WORK_DATE)
    final_weather = final.merge(
        weather_data,
        on=["WORK_DATE", "DEB_TIME_HOUR"],
    )

    final_weather.columns= final_weather.columns.str.lower()

    return final_weather
