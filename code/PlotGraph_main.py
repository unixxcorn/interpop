"""Plot Graph (Final)"""
import pandas as pd
import pygal
import math
from pygal.style import NeonStyle
from pygal.style import DefaultStyle
def main(whatuse = 'Computer', whatyear = 'all', whatfilter = 'area', style=DefaultStyle):
    """main(whatuse, whatyear, whatfilter)
        whatuse
        1.Computer
        2.Internet
        3.Mobile
        whatyear
        1.2553
        2.2554
        3.2555
        4.2556
        5.2557
        6.2558
        7.2559
        8.all
        whatfilter
        1.area
        2.age
        3.education
    """
    if whatfilter == 'area':
        num = 0
        head = 'Region, area'
    elif whatfilter == 'age':
        num = 1
        head = 'age'
    elif whatfilter == 'education':
        num = 2
        head = 'Level of education'

    data = call_data(whatyear, whatfilter, num)
    info = select_data(data, whatuse, whatyear)

    if whatyear == 'all':
        bar_chart = pygal.Line(title = 'Graph '+whatuse+' using('\
                    +whatfilter+') in '+whatyear+' year (100%)', style=style)
        count = 1
        data_head = ['2553', '2554', '2555', '2556', '2557', '2558', '2559']
        for i in range(len(info)):
            bar_chart.add(data[0][head][count], info[i])
            count += 1
    else:
        bar_chart = pygal.Bar(title = 'Graph '+whatuse+' using('\
                    +whatfilter+') in '+whatyear+' year (100%)', style=style)
        data_head = [i for i in data[head][1:]]
        bar_chart.add('', info)
    bar_chart.x_labels = [i for i in data_head]
    return bar_chart

def call_data(whatyear, whatfilter, num):
    """This function call data and return data"""
    """This function return data_head and data"""
    find_data = {'2559':['./usedata/59/Tab2.csv', \
                         './usedata/59/Tab3.csv', \
                         './usedata/59/Tab4.csv'],
                 '2558':['./usedata/58/Tab2.csv', \
                         './usedata/58/Tab3.csv', \
                         './usedata/58/Tab4.csv'],
                 '2557':['./usedata/57/Tab2.csv', \
                         './usedata/57/Tab3.csv', \
                         './usedata/57/Tab4.csv'],
                 '2556':['./usedata/56/Tab2.csv', \
                         './usedata/56/Tab3.csv', \
                         './usedata/56/Tab4.csv'],
                 '2555':['./usedata/55/Tab2.csv', \
                         './usedata/55/Tab3.csv', \
                         './usedata/55/Tab4.csv'],
                 '2554':['./usedata/54/Tab2.csv', \
                         './usedata/54/Tab3.csv', \
                         './usedata/54/Tab4.csv'],
                 '2553':['./usedata/53/Tab2.csv', \
                         './usedata/53/Tab3.csv', \
                         './usedata/53/Tab4.csv'],}
    if whatyear == 'all':
        year = ['2553', '2554', '2555', '2556', '2557', '2558', '2559']
        data = [call_data(i, whatfilter, num) for i in year]
    else:
        data = pd.read_csv(find_data[whatyear][num])
    return data

def select_data(data, whatuse, whatyear):
    use = whatuse + ' using'
    info = []
    infos = []
    if whatyear == 'all':
        for i in range(len(data)):
            memo = [(data[i][use][j] * 100)/data[i]['Total'][j] \
            for j in range(1, len(data[i]['Total']))]
            infos.append(memo)
        for i in range(len(infos[0])):
            memo = [infos[j][i] for j in range(len(infos))]
            info.append(memo)
    else:
        info = [(data[use][i]*100)/data['Total'][i]\
        for i in range(1, len(data[use]))]
    return info
