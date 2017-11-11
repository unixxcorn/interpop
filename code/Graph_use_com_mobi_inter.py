"""Graph use computer mobile and internet"""
import pandas as pd
import math
import pygal

def main():
    """Plot Graph"""
    whatuse = input()
    #1.Computer
    #2.Internet
    #3.Mobile
    #4.all
    whatyear = input()
    #1.2553
    #2.2554
    #3.2555
    #4.2556
    #5.2557
    #6.2558
    #7.2559
    #8.all
    whatfilter = input()
    #1.area
    #2.age
    use = ['Computer using', 'Internet using', 'Mobile using']
    data = call_data(whatyear, whatfilter)
    data_head, info, total = select_data(whatuse, whatyear, whatfilter, data)
    print(info)
    print(total)
    info = change_percen(info, total, whatuse)
    print(info)

    head_graph = 'Population '+whatuse+' using in '+whatyear+' year (100%)'
    add_graph = whatuse+' using'
    bar_chart = pygal.Bar(title = head_graph)
    # for all
    if whatuse == 'all':
        count = 0
        for i in use:
            bar_chart.add(i, info[count])
            count += 1
    else:
        bar_chart.add(whatuse, info)
    bar_chart.x_labels = [i for i in data_head]
    bar_chart.render_to_file("Graph.svg")

def call_data(whatyear, whatfilter):
    """Call data for year"""
    if whatyear == '2559' and whatfilter == 'area':
        data = pd.read_csv('../usedata/59/Tab2.csv')
    elif whatyear == '2559' and whatfilter == 'age':
        data = pd.read_csv('../usedata/59/Tab3.csv')

    if whatyear == '2558' and whatfilter == 'area':
        data = pd.read_csv('../usedata/58/Tab2.csv')
    elif whatyear == '2558' and whatfilter == 'age':
        data = pd.read_csv('../usedata/58/Tab3.csv')

    if whatyear == '2557' and whatfilter == 'area':
        data = pd.read_csv('../usedata/57/Tab2.csv')
    elif whatyear == '2557' and whatfilter == 'age':
        data = pd.read_csv('../usedata/57/Tab3.csv')

    if whatyear == '2556' and whatfilter == 'area':
        data = pd.read_csv('../usedata/56/Tab2.csv')
    elif whatyear == '2556' and whatfilter == 'age':
        data = pd.read_csv('../usedata/56/Tab3.csv')

    if whatyear == '2555' and whatfilter == 'area':
        data = pd.read_csv('../usedata/55/Tab2.csv')
    elif whatyear == '2555' and whatfilter == 'age':
        data = pd.read_csv('../usedata/55/Tab3.csv')

    if whatyear == '2554' and whatfilter == 'area':
        data = pd.read_csv('../usedata/54/Tab2.csv')
    elif whatyear == '2554' and whatfilter == 'age':
        data = pd.read_csv('../usedata/54/Tab3.csv')

    if whatyear == '2553' and whatfilter == 'area':
        data = pd.read_csv('../usedata/53/Tab2.csv')
    elif whatyear == '2553' and whatfilter == 'age':
        data = pd.read_csv('../usedata/53/Tab3.csv')
    return data

def select_data(whatuse, whatyear, whatfilter, data):
    """Select data to use"""
    use = ['Computer using', 'Internet using', 'Mobile using']
    if whatfilter == 'area':
        data_head = [i for i in data['Region, area'][1:]]
    elif whatfilter == 'age':
        data_head = [i for i in data['age'][1:]]

    if whatuse == 'Computer':
        info = [i for i in data['Computer using'][1:]]
    elif whatuse == 'Internet':
        info = [i for i in data['Internet using'][1:]]
    elif whatuse == 'Mobile':
        info = [i for i in data['Mobile using'][1:]]
    #for all
    elif whatuse == 'all':
        info = []
        for j in range(3):
            info.append([i for i in data[use[j]][1:]])
    total = [i for i in data['Total'][1:]]

    return data_head, info, total

def change_percen(info, total, whatuse):
    """Change data to percen"""
    ans = []
    if whatuse != 'all':
        for j in range(len(total)):
            ans.append(math.ceil((info[j]*100)/total[j]))
    else:
        for j in range(3):
            memo = []
            for i in range(len(total)):
                memo.append(math.ceil((info[j][i]*100)/total[i]))
            ans.append(memo)
    return ans

main()
