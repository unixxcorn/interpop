""" To create for only computer using's graph"""
import pandas as pd
import pygal as pg
def com(whatfilter="location", whatyear="all",whatfilter_type='1', num=0):
    """
        Plot only Computer using graph
        com(whatilter, whatyear)
    """
    #whatfilter = location, activity, region
    #whatyear = 2559, 2558, 2557, 2556, 2555, 2554, 2553, all
    last, last_all, filter_text = ' in ' + whatyear, '', ''
    if whatfilter.lower() == 'region':
        last = ' per day in '+whatyear
    else:
        filter_text = 'and ages'
    if whatyear.lower() == 'all' :
        last_all, last = ' years', ' of '+whatyear

    data = call_data(whatyear, whatfilter, num)
    info_kind = select_data(data, whatyear, whatfilter, int(whatfilter_type))
    info = info_kind[0]
    #plotting graph all years use line grapah / single year uses bar graph
    head_graph = 'Number of computer users by '+whatfilter+' '+filter_text+' to use computer'+last+last_all
    if whatyear == 'all':
        if whatfilter.lower() == "location" or whatfilter == "activity":
            h_kind = info_kind[1]
            chart = pg.Line(title=head_graph+' in 100%'+' ('+h_kind+' old)')
            data_head = ['2553', '2554', '2555', '2556', '2557', '2558', '2559']
            kind = list((data[num])[whatfilter])
            for i in range(len(kind)):
                chart.add(kind[i], info[i])
        if whatfilter.lower() == 'region':
            h_kind = info_kind[1]
            chart = pg.Line(title=head_graph+' in 100%'+' ('+h_kind+')')
            data_head = ['2553', '2554', '2555', '2556', '2557', '2558', '2559']
            kind = list((data[num])[whatfilter])
            for i in range(len(kind)):
                chart.add(kind[i], info[i])
    else: #single year
        chart = pg.Bar(title=head_graph+'  (100%)')
        data_head = [i for i in data[whatfilter]]
        kind = list(data)[2:]
        for i in range(len(kind)):
            chart.add(kind[i], info[i])
    chart.x_labels = [i for i in data_head]
    return chart
#===============================================================================
def call_data(whatyear, whatfilter, num):
    """This function call data and return data
       This function return data_head and data"""
    #0, 1, 2 = location, activity, region
    num = 0 #Table12 location
    if whatfilter.lower() == 'activity': num = 1 #Tab14 activity
    if whatfilter.lower() == 'region': num = 2 #Tab16 region
    find_data = {'2559':['./usedata/59/Tab12.csv', \
                         './usedata/59/Tab14.csv', \
                         './usedata/59/Tab16.csv'],
                 '2558':['./usedata/58/Tab12.csv', \
                         './usedata/58/Tab14.csv', \
                         './usedata/58/Tab16.csv'],
                 '2557':['./usedata/57/Tab12.csv', \
                         './usedata/57/Tab14.csv', \
                         './usedata/57/Tab16.csv'],
                 '2556':['./usedata/56/Tab12.csv', \
                         './usedata/56/Tab14.csv', \
                         './usedata/56/Tab16.csv'],
                 '2555':['./usedata/55/Tab12.csv', \
                         './usedata/55/Tab14.csv', \
                         './usedata/55/Tab16.csv'],
                 '2554':['./usedata/54/Tab12.csv', \
                         './usedata/54/Tab14.csv', \
                         './usedata/54/Tab16.csv'],
                 '2553':['./usedata/53/Tab12.csv', \
                         './usedata/53/Tab14.csv', \
                         './usedata/53/Tab16.csv']}

    if whatyear == 'all':
        year = ['2553', '2554', '2555', '2556', '2557', '2558', '2559']
        data = [call_data(i, whatfilter, num) for i in year]
    else:
        data = pd.read_csv(find_data[whatyear][num])
    return data
#===============================================================================
def select_data(data, whatyear, whatfilter='', whatfilter_type=1):
    """Work like a filter to selects data for plotting"""
    kind = ''
    info, infos = [], []
    if whatyear == 'all':
        if whatfilter == "region":
            #whatfilter_type = float(input('A time(hours) you want to define: '))
            if whatfilter_type < 1:
                kind = 'Less than 1 hour'
            if whatfilter_type >= 1 and whatfilter_type < 2:
                kind = '1-2 hours'
            if whatfilter_type >= 2 and whatfilter_type < 3:
                kind = '2-3 hours'
            if whatfilter_type >= 3 and whatfilter_type < 4:
                kind = '3-4 hours'
            if whatfilter_type >= 4 and whatfilter_type < 5:
                kind = '4-5 hours'
            if whatfilter_type >= 5 and whatfilter_type < 6:
                kind = '5-6 hours'
            if whatfilter_type >= 6: #> 6 hours
                kind = 'More than 6 hours' #get kind of region(ages)
        if whatfilter == "location" or whatfilter == "activity":
            #whatfilter_type = float(input("An ages(years) you want to define: "))
            if whatfilter_type < 11:
                kind = '6-10 years'
            if whatfilter_type >= 11 and whatfilter_type < 15:
                kind = '11-14 years'
            if whatfilter_type >= 15 and whatfilter_type < 20:
                kind = '15-19 years'
            if whatfilter_type >= 20 and whatfilter_type < 25:
                kind = '20-24 years'
            if whatfilter_type >= 25 and whatfilter_type < 30:
                kind = '25-29 years'
            if whatfilter_type >= 30 and whatfilter_type < 35:
                kind = '30-34 years'
            if whatfilter_type >= 35 and whatfilter_type < 40:
                kind = '35-39 years'
            if whatfilter_type >= 40 and whatfilter_type < 50:
                kind = '40-49 years'
            if whatfilter_type >= 50 and whatfilter_type < 60:
                kind = '50-59 years'
            if whatfilter_type >= 60: # >60 years
                kind = '60 years and over' #get kind of location and activity(hrs)
        for yrs in range(len(data)):
            memo = [(data[yrs][kind][i]*100)/data[yrs]['Total'][i] for i in range(len(data[yrs][kind]))]
            infos.append(memo)
        for i in range(len(infos[0])):
            memo = [infos[j][i] for j in range(len(infos))]
            info.append(memo)
        #print('infos:', infos)
        #print()
    else: #region, activity, location
        info = [[(data[kind][i]*100)/data['Total'][i] for i in \
                range(len(data[kind]))] for kind in list(data)[2:]]
    return (info, kind)
