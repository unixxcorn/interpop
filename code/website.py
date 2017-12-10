from flask import Flask, render_template
import pygal

app = Flask("Internet Population")

@app.route('/')
def hello_world():
    return render_template( 'home.html')

@app.route('/charts/main/')
def PlotGraph_main_route():
    import PlotGraph_main
    chart = PlotGraph_main.main().render_data_uri()
    return render_template( 'charts.html', chart = chart, asider = 'navside_main.html')
@app.route('/charts/main/<whatuse>/')
@app.route('/charts/main/<whatuse>/<filterby>/')
@app.route('/charts/main/<whatuse>/<filterby>/<whatyear>/')
def PlotGraph_main_route_attrib(whatuse = 'Computer',filterby = 'area', whatyear = 'all'):
    import PlotGraph_main
    chart = PlotGraph_main.main(whatuse, whatyear, filterby).render_data_uri()
    return render_template( 'charts.html', chart = chart, asider = 'navside_main.html')

@app.route('/charts/computer/')
def PlotGraph_com_route():
    import PlotGraph_com
    chart = PlotGraph_com.com('location', 'all', '11').render_data_uri()
    return render_template( 'charts.html', chart = chart, asider = 'navside_com.html')
@app.route('/charts/computer/<whatfilter>/<whatfilter_type>')
def PlotGraph_com_route_all_with_year(whatfilter, whatfilter_type):
    import PlotGraph_com
    chart = PlotGraph_com.com(whatfilter, 'all', whatfilter_type).render_data_uri()
    return render_template( 'charts.html', chart = chart, asider = 'navside_com.html')
@app.route('/charts/computer/<whatfilter>/year/<whatyear>/')
def PlotGraph_com_route_attrib(whatyear, whatfilter):
    import PlotGraph_com
    chart = PlotGraph_com.com(whatfilter, whatyear).render_data_uri()
    return render_template( 'charts.html', chart = chart, asider = 'navside_com.html')

@app.route('/charts/internet/')
@app.route('/charts/internet/<whatfilter>/')
@app.route('/charts/internet/<whatfilter>/<whatyear>')
def PlotGraph_internet_route_attrib(whatyear='all', whatfilter='1'):
    import PlotGraph_internet
    if whatyear != 'all':
        whatyear = whatyear[-2:]
    chart = PlotGraph_internet.main(whatfilter, whatyear).render_data_uri()
    return render_template( 'charts.html', chart = chart, asider = 'navside_internet.html')

@app.route('/charts/phone/')
@app.route('/charts/phone/<kind>/')
@app.route('/charts/phone/<kind>/<area>')
@app.route('/charts/phone/<kind>/<area>/<year>')
def PlotGraph_cellular_route_attrib(year = 'all', area = 'whole', kind = 'all'):
    import PlotGraph_phone
    chart = PlotGraph_phone.main(year, area, kind).render_data_uri()
    return render_template( 'charts.html', chart = chart, asider = 'navside_phone.html')

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error = 500), 500
@app.errorhandler(404)
def internal_error(error):
    return render_template('error.html', error = 404), 404
