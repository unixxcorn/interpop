"""Internet Population's Graph"""

import pandas as pd
import pygal

def main(choice='1', year='all'):
    '''Core function
        choice
            1 = Number of Internet users by type of access
            2 = Time period of Internet's access
            3 = Internet activities
            ########################
        year = all, 53, 54, 55, 56, 57 ,58, 59
    '''
    data = call_data(choice, year)
    if year == 'all' and choice == '3':
        chart = pygal.Line()
        chart.title = 'Total number of Internet users by Activities'
        temp = []
        data_add = [i for i in data[0]['Activity to use Internet '] if i != 'Total']
        data_head = ['2553', '2554', '2555', '2556', '2557' , '2558', '2559']

        for i in range(1, len(data_add)+1):
            info = [(data[j]['Internet using '][i]*100)//data[j]['Total'][0] \
            for j in range(len(data_head))]
            temp.append(info)

        for i in range(len(data_add)):
            chart.add(data_add[i], temp[i])

    elif year == 'all':
        chart = pygal.Line()
        if choice == '1':
        	chart.title = 'Total number of Internet users by Type'
        else:
        	chart.title = 'Total number of Internet users by Time period'
        temp = []
        memo = [i for i in data[0]]
        data_head = ['2553', '2554', '2555', '2556', '2557' , '2558', '2559']
        data_add = memo[2:]

        for i in data_add:
            info = [(data[j][i][0]*100)//data[j]['Total'][0]\
            for j in range(len(data_head))]
            temp.append(info)

        for i in range(len(data_add)):
            chart.add(data_add[i], temp[i])

    else:
        chart = pygal.Bar()
        memo = [i for i in data]
        data_head = [i for i in data[memo[0]] if i != 'Whole kingdom' and i != 'Total']
        chart.title = memo[0] + ' in 25' + year
        
        for i in range(2, len(memo)):
            chart.add(str(memo[i]), [int((j*100)//data[memo[1]][0]) \
            for j in data[memo[i]][1:]])

    
    chart.x_labels = data_head
    chart.render_to_file('../Graph/Graph_internet.svg')


def call_data(choice, year):
    '''call data from csv'''
    data = []
    location = {'1':'../usedata/' + year + '/Taba.csv',
                '2':'../usedata/' + year + '/Tabc.csv',
                '3':'../usedata/' + year + '/Tabd.csv'}
    all_year = ['53', '54', '55', '56', '57' , '58', '59']
    if year == 'all':
        for i in all_year:
            location = {'1':'../usedata/' + i + '/Taba.csv',
                        '2':'../usedata/' + i + '/Tabc.csv',
                        '3':'../usedata/' + i + '/Tabd.csv'}
            year = i
            data.append(pd.read_csv(location[choice]))
    else:
        data = pd.read_csv(location[choice])

    return data

main(input(), input())
