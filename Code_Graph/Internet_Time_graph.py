"""Use Computer Mobile and Internet"""
import pandas as pd
import pygal
import math

def call_data(year):
    """This function call data of year input"""
    info = []
    data = pd.read_csv('../data/Internet_Time_Use.csv')
    year = int(year)
    select = str(year)
    for i in data[select]:
        info.append(i/1000)
    return info

def data_2553():
    """This function plot data year 2553"""
    data = call_data(2553)
    return data

def data_2554():
    """This function plot data year 2554"""
    data = call_data(2554)
    return data

def data_2555():
    """This function plot data year 2555"""
    data = call_data(2555)
    return data

def data_2556():
    """This function plot data year 2556"""
    data = call_data(2556)
    return data

def data_2557():
    """This function plot data year 2557"""
    data = call_data(2557)
    return data

def data_2558():
    """This function plot data year 2558"""
    data = call_data(2558)
    return data

def data_2559():
    """This function plot data year 2559"""
    data = call_data(2559)
    return data

def main():
    """m"""
    datahead = []
    data = pd.read_csv('../data/Internet_Time_Use.csv')

    for i in data['อัตราการใช้']:
        datahead.append(i)
    bar_chart = pygal.Bar(title = 'อัตราการใช้อินเทอร์เน็ต(คน) 1:1000')
    bar_chart.add("2553", data_2553())
    bar_chart.add("2554", data_2554())
    bar_chart.add("2555", data_2555())
    bar_chart.add("2556", data_2556())
    bar_chart.add("2557", data_2557())
    bar_chart.add("2558", data_2558())
    bar_chart.add("2559", data_2559())
    bar_chart.x_labels = [i for i in datahead]
    bar_chart.render_to_file("1.Internet_Time_Graph.svg")
main()
