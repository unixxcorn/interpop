"""Growth"""
import pandas as pd
import pygal

def main():
    """
        .
    """
    data = []
    data_x = []
    head = []
    fin = []
    year = ['2553', '2554', '2555', '2556', '2557', '2558', '2559']
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

    for i in year:
        memo = pd.read_csv(find_data[i][0])
        data.append(memo)
    for i in data[0]:
        if not 'not' in i:
            head.append(i)
    head = head[2:]

    memo = 0
    for j in head:
        temp = [(data[i][j][0]*100)//data[i]['Total'][0] \
                for i in range(len(data))]
        data_x.append(temp)

    for i in data_x:
        memo = 0
        ans = []
        for j in i:
            ans.append(j - memo)
            memo = j
            ans[0] = 0
        fin.append(ans)
    chart = pygal.Bar()
    chart.x_labels = year[1:]
    chart.title = 'The growth of computer, internet and mobile in Thailand'
    for i in range(len(fin)):
        chart.add(head[i], fin[i][1:])
    return chart.render_data_uri()
