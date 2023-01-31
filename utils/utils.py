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
        attendance_label : str = mabel of the attendance column.
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