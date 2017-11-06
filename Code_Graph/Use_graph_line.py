"""Use Computer Mobile and Internet"""
import pandas as pd
import pygal
import math

def call_data(year):
    """This function call data of year input"""
    info = []
    data = pd.read_csv('../data/Use_Line.csv')
    select = str(year)
    for i in data[select]:
        info.append(i/1000)
    return info

def data_com():
    """This function plot data year ใช้คอมพิวเตอร์"""
    data = call_data('ใช้คอมพิวเตอร์')
    return data

def data_inter():
    """This function plot data year ใช้อินเทอร์เน็ต"""
    data = call_data('ใช้อินเทอร์เน็ต')
    return data

def data_mobi():
    """This function plot data year ใช้โทรศัพท์มือถือ"""
    data = call_data('ใช้โทรศัพท์มือถือ')
    return data

def main():
    """m"""
    datahead = []
    data = pd.read_csv('../data/Use_Line.csv')

    for i in data['การใช้']:
        datahead.append(i)
    bar_chart = pygal.Line(title = 'จำนวนผู้ใช้งาน คอมพิวเตอร์ อินเทอร์เน็ต และ โทรศัพท์มือถือ(คน) 1:1000')
    bar_chart.add("ใช้คอมพิวเตอร์", data_com())
    bar_chart.add("ใช้อินเทอร์เน็ต", data_inter())
    bar_chart.add("ใช้โทรศัพท์มือถือ", data_mobi())
    bar_chart.x_labels = [i for i in datahead]
    bar_chart.render_to_file("3.Use_Graph_line.svg")
main()
