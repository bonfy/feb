/*
  Initilizing echarts samples.
*/

import Echart from 'echarts'

var chart_main = Echart.init(document.getElementById('main'))
var chart_n = Echart.init(document.getElementById('n'))

var ht = {}

var sendXHR = (request, chart) => {
  chart.showLoading()

  var { method, url, data, headers } = request

  var xhr = new XMLHttpRequest(), response = { url: url }, handler
  xhr.open(request.method, url, true)

  handler = (event) => {

    response.data = JSON.parse(xhr.responseText)
    response.status = xhr.status
    response.statusText = xhr.statusText
    response.headers = xhr.getAllResponseHeaders()

    data = response.data
    // 
    // if( data.series[0].type === 'pie') {
    //   delete data.xAxis
    //   delete data.yAxis
    // }

    console.log('hello > ', data.series)

    chart.setOption(data)
    console.log('Response > ', response)
    chart.hideLoading()

  }

  xhr.timeout = 0
  xhr.onload = handler
  xhr.onabort = handler
  xhr.onerror = handler
  xhr.ontimeout = function () {}
  xhr.onprogress = function () {}

  for (header in request.headers || {})
    xhr.setRequestHeader(header, request.headers[header])

  xhr.send(request.data);
}

ht.loadChart = (url, chart, data = {}, headers = {}) => {
  var request = {
    method: 'get',
    url: url,
    data: data,
    headers: headers
  }
  return sendXHR(request, chart)
}

ht.loadChart('http://127.0.0.1:8888/opt/pie', chart_main)
ht.loadChart('http://127.0.0.1:8888/opt/bar', chart_n)
