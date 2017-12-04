from flask import Flask
import pygal

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/charts/line.svg')
def line_route():
    line_chart = pygal.Line()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    return line_chart.render_response()

@app.route('/charts/main/')
def PlotGraph_main_route():
    import PlotGraph_main
    return PlotGraph_main.main().render_response()
@app.route('/charts/main/<whatuse>/<whatyear>/<whatfilter>')
def PlotGraph_main_route_attrib(whatuse, whatyear, whatfilter):
    import PlotGraph_main
    return PlotGraph_main.main(whatuse, whatyear, whatfilter).render_response()

@app.route('/charts/com/')
def PlotGraph_com_route():
    import PlotGraph_com
    return PlotGraph_com.com().render_response()
@app.route('/charts/com/<whatyear>/<whatfilter>')
def PlotGraph_com_route_attrib(whatyear, whatfilter):
    import PlotGraph_com
    return PlotGraph_com.com(whatfilter, whatyear).render_response()