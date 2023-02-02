import pandas as pd
import plotly.graph_objects as go

def attendance_figures(df, attraction_list, start_date, end_date, date_label, attendance_label, attraction_label):
    '''
    Return the attendance mean, max and min. 

    Inputs:
        df : pd.DataFrame() = table of the attendance per date and per attraction. 
        attraction_list : list(str) = list of the names of the attractions.
        start_date : str = starting date of the period with format yyyy/mm/dd.
        end_date : str = ending date of the period with format yyyy/mm/dd.
        date_label : str = label of the date column.
        attendance_label : str = label of the attendance column.
        attraction_label : str = label of the attraction column.

    Outputs:
        mean : int = average daily attendnace of the attraction over the period.
        min : min daily attendance at the attraction during the period.
        max : max daily attendance at the attraction during the perdiod. 
    '''
    to_plot = df.copy()

    # Change date types
    to_plot[f"{date_label}"] = pd.to_datetime(to_plot[f"{date_label}"])
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Replace negative values with zero values
    to_plot.loc[to_plot[f"{attendance_label}"]<0, f"{attendance_label}"] = 0

    # Filter the table
    to_plot = to_plot[(to_plot[f"{date_label}"]>start_date)&(to_plot[f"{date_label}"]<end_date)][to_plot[f"{attraction_label}"].isin(attraction_list)]

    # Calculate figures
    val_min = to_plot[f"{attendance_label}"].min()
    val_avg = int(to_plot[f"{attendance_label}"].mean())
    val_max = to_plot[f"{attendance_label}"].max()

    # Generate plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=to_plot["USAGE_DATE"], y=to_plot["attendance"], mode="lines", name='Attendance', line=dict(color='#002244')))
    fig.update_layout(yaxis_title='Daily Attendance', width=800, height=400)
    
    return fig, [val_min, val_avg, val_max]

def daily_wait_time_figures(df, attraction_list, start_date, end_date, date_label, wait_time_label, attraction_label):
    '''
    Return the heatmap for average wait times per ride on a daily basis. 
    Inputs:
        df : pd.DataFrame() = table of the wait time per ride every 15 min and an assortment of other related features. 
        attraction_list : list(str) = list of the names of the attractions.
        start_date : str = starting date of the period with format yyyy/mm/dd.
        end_date : str = ending date of the period with format yyyy/mm/dd.
        date_label : str = label of the date column.
        attendance_label : str = label of the attendance column.
        attraction_label : str = label of the attraction column.
    Outputs:
       fig: A detailed heatmap that shows the variation of average wait times per day for selected rides in the given timeframe
    '''
    to_plot = df.copy()

    # Change date types
    to_plot[f"{date_label}"] = pd.to_datetime(to_plot[f"{date_label}"])
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Replace negative values with zero values
    to_plot.loc[to_plot[f"{wait_time_label}"]<0, f"{wait_time_label}"] = 0

    # Filter the table
    to_plot = to_plot[(to_plot[f"{date_label}"]>=start_date)&(to_plot[f"{date_label}"]<=end_date)][to_plot[f"{attraction_label}"].isin(attraction_list)]

    # Create a dataframe dictionary with each ride name as key
    unique_rides = to_plot[f"{attraction_label}"].unique()
    df_dict = {elem : pd.DataFrame() for elem in unique_rides}
    for key in df_dict.keys():
        df_dict[key] = to_plot[:][to_plot[f"{attraction_label}"] == key]

    # Group the table by date and extract arrays of wait times for each ride per day
    namelist = unique_rides.tolist()
    complete_list = []
    for elem in namelist:
        df = df_dict[elem]
        rslt_df = df[[f"{date_label}", f"{wait_time_label}"]]
        rslt_df = rslt_df.groupby([f"{date_label}"]).mean()
        list = rslt_df[f"{wait_time_label}"].tolist()
        complete_list.append(list)
    
    # Generate plot
    fig = go.Figure(data=go.Heatmap(
        z=complete_list,
        x=rslt_df.index,
        y=unique_rides,
        colorscale='Viridis'))

    fig.update_layout(
        title='Average Wait Times of Each Ride Per Day (in minutes)',
        xaxis_title = 'Date',
        yaxis_title = 'Ride',
        xaxis_nticks = len(rslt_df.index),
        width=800, height=400)
    
    return fig

def hourly_wait_time_figures(df, attraction_list, date, date_label, hour_label, wait_time_label, attraction_label):
    '''
    Return the heatmap for average wait times per ride on an hourly basis. 
    Inputs:
        df : pd.DataFrame() = table of the wait time per ride every 15 min and an assortment of other related features. 
        attraction_list : list(str) = list of the names of the attractions.
        date : str = input date of the user with format yyyy/mm/dd.
        date_label : str = label of the date column.
        hour_lable: str = label of the hour column.
        attendance_label : str = label of the attendance column.
        attraction_label : str = label of the attraction column.
    Outputs:
       fig: A detailed heatmap that shows the variation of average wait times per hour for selected rides on the given day
    '''
    to_plot = df.copy()

    # Change date types
    to_plot[f"{date_label}"] = pd.to_datetime(to_plot[f"{date_label}"])
    date = pd.to_datetime(date)

    # Replace negative values with zero values
    to_plot.loc[to_plot[f"{wait_time_label}"]<0, f"{wait_time_label}"] = 0

    # Filter the table
    to_plot = to_plot[(to_plot[f"{date_label}"]==date)][to_plot[f"{attraction_label}"].isin(attraction_list)]

    # Create a dataframe dictionary with each ride name as key
    unique_rides = to_plot[f"{attraction_label}"].unique()
    df_dict = {elem : pd.DataFrame() for elem in unique_rides}
    for key in df_dict.keys():
        df_dict[key] = to_plot[:][to_plot[f"{attraction_label}"] == key]

    # Group the table by date and extract arrays of wait times for each ride per day
    namelist = unique_rides.tolist()
    complete_list = []
    for elem in namelist:
        df = df_dict[elem]
        rslt_df = df[[f"{hour_label}", f"{wait_time_label}"]]
        rslt_df = rslt_df.groupby([f"{hour_label}"]).mean()
        list = rslt_df[f"{wait_time_label}"].tolist()
        complete_list.append(list)
    
    # Generate plot
    fig = go.Figure(data=go.Heatmap(
        z=complete_list,
        x=rslt_df.index,
        y=unique_rides,
        colorscale='Viridis'))

    fig.update_layout(
        title='Average Wait Times of Each Ride Per Hour On The Selected Day (in minutes)',
        xaxis_title = 'Hour of Day',
        yaxis_title = 'Ride',
        xaxis_nticks = len(rslt_df.index),
        width=800, height=400)
    
    return fig

def attendance_week_month(attendance):
    '''
    Create the graph that show the monthly and weekly seasonalities

    Input : 
        attendance: pd.DataFrame = table of the attendances for the two parks
    Output :
        fig_week, fig_month = one plot for each seasonality
    '''
    # Average anual attendance
    to_plot_month = attendance.copy()
    to_plot_month["month"] = pd.to_datetime(attendance.USAGE_DATE).apply(lambda x: x.month)
    to_plot_month = to_plot_month[["FACILITY_NAME", "month", "attendance"]].groupby(["FACILITY_NAME", "month"]).mean().reset_index()
    mapping = {1: 'january',\
        2: 'february',
        3: 'march',
        4: 'april',
        5: 'may',
        6: 'june',
        7: 'july',
        8: 'august',
        9: 'september',
        10: 'october',
        11: 'november',
        12: 'december'}
    to_plot_month = to_plot_month.replace({'month': mapping})

    to_plot_day = attendance.copy()
    to_plot_day["day"] = pd.to_datetime(attendance.USAGE_DATE).apply(lambda x: x.weekday())
    to_plot_day = to_plot_day[["FACILITY_NAME", "day", "attendance"]].groupby(["FACILITY_NAME", "day"]).mean().reset_index()
    mapping = {0: 'monday',\
        1: 'tuesday',
        2: 'wednesday',
        3: 'thursday',
        4: 'friday',
        5: 'saturday',
        6: 'sunday'}
    to_plot_day = to_plot_day.replace({'day': mapping})

    to_plot_month_1 = to_plot_month[to_plot_month.FACILITY_NAME=="Tivoli Gardens"]
    to_plot_month_2 = to_plot_month[to_plot_month.FACILITY_NAME=="PortAventura World"]

    fig_month = go.Figure()
    fig_month.add_trace(go.Scatter(x=to_plot_month_1.month, y=to_plot_month_1.attendance, mode="lines", name="Tivoli Gardens", line=dict(color='#002244')))
    fig_month.add_trace(go.Scatter(x=to_plot_month_2.month, y=to_plot_month_2.attendance, mode="lines", name="PortAventura World", line=dict(color='#ff0066')))
    fig_month.update_layout(yaxis_title='Attendance', width=400, height=400, title='Monthly seasonnality')

    to_plot_day_1 = to_plot_day[to_plot_day.FACILITY_NAME=="Tivoli Gardens"]
    to_plot_day_2 = to_plot_day[to_plot_day.FACILITY_NAME=="PortAventura World"]

    fig_day = go.Figure()
    fig_day.add_trace(go.Scatter(x=to_plot_day_1.day, y=to_plot_day_1.attendance, mode="lines", name="Tivoli Gardens", line=dict(color='#002244')))
    fig_day.add_trace(go.Scatter(x=to_plot_day_2.day, y=to_plot_day_2.attendance, mode="lines", name="PortAventura World", line=dict(color='#ff0066')))
    fig_day.update_layout(yaxis_title='Attendance', width=400, height=400, title='Weekly seasonnality')

    return fig_day, fig_month
