"""Plot Graph"""
import pandas as pd
import numpy as np
import pygal as pg

def main(year = 'all', area = 'whole', kind = 'all'):
    """Main function to send value for plot graph"""
    if year == 'all':
        y_forf = '53-2559'
    elif year != 'all': #53 54 55 56 57 58 59
        y_forf = str(year)[-2:]
    if area.lower() == 'whole': #ทั้งประเทศ
        a_forf = 'ทั้งประเทศ' #0-4
    elif area.lower() == 'municipal': #เขตในเทศบาล
        a_forf = 'เขตในเทศบาล' #5-9
    elif area.lower() == 'non-municipal': #เขตนอกเทศบาล
        a_forf = 'เขตนอกเทศบาล' #10-14
    if kind.lower() == 'all':
        k_forf = 'all'
    elif kind.lower() == 'sms': #sms
        k_forf = 0
    elif kind.lower() == 'data': #data
        k_forf = 1
    elif kind.lower() == 'banking': #banking
        k_forf = 2
    elif kind.lower() == 'function': #function
        k_forf = 3
    return plot_graph(y_forf, a_forf, k_forf)

def plot_graph(year, area, kind):
    """Function for plot graph"""
    if area == 'ทั้งประเทศ':
        a_start = 0
    elif area == 'เขตในเทศบาล':
        a_start = 5
    elif area == 'เขตนอกเทศบาล':
        a_start = 10
    if kind == 0:
        k_name = 'SMS'
    elif kind == 1:
        k_name = 'Data'
    elif kind == 2:
        k_name = 'Mobile banking'
    elif kind == 3:
        k_name = 'Mobile function'
    elif kind == 'all':
        k_name = 'ทั้งหมด'
    data_frame = pd.read_csv('./usedata/alldata.csv')
    line_chart = pg.Bar()
    line_chart.title = 'จำนวนการใช้บริการ' + k_name + 'ทางโทรศัพท์ ของ' + area + ' ในปี 25' + year
    if year == '53-2559':
        line_chart = pg.Line()
        line_chart.title = 'จำนวนการใช้บริการ' + k_name + 'ทางโทรศัพท์ ของ' + area + ' ในปี 25' + year
        line_chart.x_labels = range(53, 60)
        if kind == 'all':
            line_chart.add('SMS', [(data_frame['53u'])[0+a_start]*100/(data_frame['53t'])[0+a_start], (data_frame['54u'])[0+a_start]*100/(data_frame['54t'])[0+a_start], \
                                   (data_frame['55u'])[0+a_start]*100/(data_frame['55t'])[0+a_start], (data_frame['56u'])[0+a_start]*100/(data_frame['56t'])[0+a_start], \
                                   (data_frame['57u'])[0+a_start]*100/(data_frame['57t'])[0+a_start], (data_frame['58u'])[0+a_start]*100/(data_frame['58t'])[0+a_start], \
                                   (data_frame['59u'])[0+a_start]*100/(data_frame['59t'])[0+a_start]])
            line_chart.add('Data', [(data_frame['53u'])[1+a_start]*100/(data_frame['53t'])[1+a_start], (data_frame['54u'])[1+a_start]*100/(data_frame['54t'])[1+a_start], \
                                   (data_frame['55u'])[1+a_start]*100/(data_frame['55t'])[1+a_start], (data_frame['56u'])[1+a_start]*100/(data_frame['56t'])[1+a_start], \
                                   (data_frame['57u'])[1+a_start]*100/(data_frame['57t'])[1+a_start], (data_frame['58u'])[1+a_start]*100/(data_frame['58t'])[1+a_start], \
                                   (data_frame['59u'])[1+a_start]*100/(data_frame['59t'])[1+a_start]])
            line_chart.add('Mobile banking', [(data_frame['53u'])[2+a_start]*100/(data_frame['53t'])[2+a_start], (data_frame['54u'])[2+a_start]*100/(data_frame['54t'])[2+a_start], \
                                   (data_frame['55u'])[2+a_start]*100/(data_frame['55t'])[2+a_start], (data_frame['56u'])[2+a_start]*100/(data_frame['56t'])[2+a_start], \
                                   (data_frame['57u'])[2+a_start]*100/(data_frame['57t'])[2+a_start], (data_frame['58u'])[2+a_start]*100/(data_frame['58t'])[2+a_start], \
                                   (data_frame['59u'])[2+a_start]*100/(data_frame['59t'])[2+a_start]])
            line_chart.add('Mobile function', [(data_frame['53u'])[3+a_start]*100/(data_frame['53t'])[3+a_start], (data_frame['54u'])[3+a_start]*100/(data_frame['54t'])[3+a_start], \
                                   (data_frame['55u'])[3+a_start]*100/(data_frame['55t'])[3+a_start], (data_frame['56u'])[3+a_start]*100/(data_frame['56t'])[3+a_start], \
                                   (data_frame['57u'])[3+a_start]*100/(data_frame['57t'])[3+a_start], (data_frame['58u'])[3+a_start]*100/(data_frame['58t'])[3+a_start], \
                                   (data_frame['59u'])[3+a_start]*100/(data_frame['59t'])[3+a_start]])
        elif kind != 'all':
            line_chart.add(k_name, [(data_frame['53u'])[kind+a_start]*100/(data_frame['53t'])[kind+a_start], (data_frame['54u'])[kind+a_start]*100/(data_frame['54t'])[kind+a_start], \
                                   (data_frame['55u'])[kind+a_start]*100/(data_frame['55t'])[kind+a_start], (data_frame['56u'])[kind+a_start]*100/(data_frame['56t'])[kind+a_start], \
                                   (data_frame['57u'])[kind+a_start]*100/(data_frame['57t'])[kind+a_start], (data_frame['58u'])[kind+a_start]*100/(data_frame['58t'])[kind+a_start], \
                                   (data_frame['59u'])[kind+a_start]*100/(data_frame['59t'])[kind+a_start]])
    elif year != '53-2559':
        if kind == 'all':
            line_chart.x_labels = ('SMS', 'Data', 'Mobile banking', 'Mobile function')
            lst_data = []
            for i in range(4):
                lst_data.append((data_frame[year+'u'])[i+a_start]*100/data_frame[year+'t'][i+a_start])
            line_chart.add('ผู้ใช้บริการปี '+year, lst_data)
        elif kind != 'all':
            line_chart.x_labels = ('จำนวนผู้ใช้'+k_name, 'จำนวนผู้ใช้บริการทั้งหมด')
            line_chart.add('ผู้ใช้บริการ'+k_name+'ปี '+year, [(data_frame[year+'u'])[kind+a_start], (data_frame[year+'t'])[kind+a_start]])
    return line_chart
