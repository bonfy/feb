# -*- coding: utf-8 -*-

"""
    app
    ~~~~~

    Sample of echarts api using Flask
"""

import functools
from flask import Flask, jsonify
# from gevent.pywsgi import WSGIServer
from echarts import Echart, Legend, Bar, Axis, Pie


def create_app():
    app = Flask(__name__)

    def crossdomain(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            resp = f(*args, **kwargs)
            h = resp.headers
            h['Access-Control-Allow-Origin'] = '*'
            h['Access-Control-Allow-Methods'] = 'GET'
            return resp

        return wrapper

    @app.route('/opt/bar')
    @crossdomain
    def bar():
        # set bar color
        color = dict(color='#EE5500')

        chart = Echart('GDP', 'This is a fake chart')
        chart.use(Bar('China', [2, 3, 4, 5], itemStyle=dict(normal=color)))
        chart.use(Legend(['GDP']))
        chart.use(Axis('category', 'bottom', data=['Nov', 'Dec', 'Jan', 'Feb']))
        return jsonify(chart.json)

    @app.route('/opt/pie')
    @crossdomain
    def pie():
        lst = [2, 3, 4, 5]
        month = ['Nov', 'Dec', 'Jan', 'Feb']
        data = [dict(value=i, name=j) for i, j in zip(lst, month)]

        chart = Echart('GDP', 'This is a fake chart', axis=False)
        chart.use(Pie('China', data))
        chart.use(Legend(['GDP']))
        return jsonify(chart.json)

    @app.errorhandler(404)
    def page_not_found(error):
        return 'Page Not Found', 404

    return app


if __name__ == '__main__':
    app = create_app()

    # windows have no gevent
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
    app.run(debug=True, port=8888)
