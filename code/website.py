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
@app.route('/charts/main/<whatuse>/<whatyear>/<whatfilter>')
def PlotGraph_main_route_attrib(whatuse, whatyear, whatfilter):
    import PlotGraph_main
    chart = PlotGraph_main.main(whatuse, whatyear, whatfilter).render_response()
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

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error = 500), 500
@app.errorhandler(404)
def internal_error(error):
    return render_template('error.html', error = 404), 404
