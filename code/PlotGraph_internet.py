"""Internet Population's Graph"""

import pandas as pd
import pygal

def main(choice='1', year="all"):
    """Core function"""
    # input() = 53, 54 , 55, 56, 57, 58, 59, all
    if choice == "user" or choice == "1":
        return analytic(year, "/Taba.csv", "Number of Internet users by type", "Region", 1, 5)
    elif choice == "location" or choice == "2":
        return analytic(year, "/Tabb.csv", "Internet's using location", "Internet's using location", 2, 4)
    elif choice == "access" or choice == "3":
        return analytic(year, "/Tabc.csv", "Time period of Internet's access", "Region", 2, 9)
    elif choice == "activity" or choice == "4":
        return analytic(year, "/Tabd.csv", "Internet activities", "activity to use Internet", 2, 12)

def analytic(year, path, name, x_axis_labels, start_select, stop_select):
    """Analysis function"""
    if year != "all":
        data_frame = pd.read_csv("./usedata/" + year + path)
        line_chart = pygal.Bar()
        line_chart.title = name + " in " + year
        line_chart.x_labels = list(data_frame[x_axis_labels])
        column_list = list(data_frame.columns.values)[start_select:stop_select]
        for column in column_list:
            raw_data_list = list(data_frame[column])
            total_list = list(data_frame["Total"])
            percentage_list = list()
            for i in range(len(raw_data_list)):
                if total_list[i] == 0:
                    total_list[i] = 1
                percentage_list.append((raw_data_list[i] / total_list[i]) * 100)
            line_chart.add(column, percentage_list)
        return line_chart
        
    else:
        df_list = []
        total_list = []
        for i in range(53, 60):
            df_list.append(pd.read_csv("./usedata/"+ str(i) + path))
        line_chart = pygal.Line()
        line_chart.title = 'Total number of Internet users by ' + x_axis_labels
        line_chart.x_labels = map(str, range(2553, 2560))
        temp_list = []
        for i in range(len(df_list[0][x_axis_labels])):
            for j in df_list:
                temp_list.append(j["Total"][i])
            total_list.append(temp_list)
            temp_list = []
        for i in range(len(total_list)):
            total_list[i] = list(map(lambda x: round((x/sum(total_list[i]))*100, 2), total_list[i]))
        for i in range(len(df_list[0][x_axis_labels])):
            line_chart.add(df_list[0][x_axis_labels][i], total_list[i])
        return line_chart