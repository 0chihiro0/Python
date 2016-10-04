#-*- coding:utf-8 -*-

from bottle import route, run, static_file

@route('/')
def home():
	return static_file('index.html', root='.')

@route('/echo/<name>')
def echo(name):
	return "Wellcome to my page! : %s" % name

run(host='localhost', port=7777)

