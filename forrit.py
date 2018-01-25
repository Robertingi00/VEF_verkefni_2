from bottle import *
import os

@route('/')
def index():
    return "<a href='/verk1'>Verkefni 1</a>" \
           "<a href='/verk2'>Verkefni 2</a>"

@route('/verk1')
def verkefni1():
    return "<h1>Verhefni 2.b<h1>"\
           "<h3><a href='/verk1/sida1'>Siða 1</a>" \
           "<a href='/verk1/sida2'>Siða 2</a>" \
           "<a href='/verk1/sida3'>Siða 3</a></h3>" \
           "<a href='/'>Til baka</a>"

@route('/verk1/<n>')
def sidur(n):
    return "<h3>Þetta er síða "+n+"</h3>" \
    "<a href='/verk1'>Til baka</a>"

@route('/verk2')
def verk2():
    return "<h1>Verhefni 2.b<h1>"\
    "<h1>Hvað viltur borða af þessu<h1>" \
    '<a href="lidur2?matur=pizza"><img src="/static/pizza.png" width="150"></a>' \
    '<a href="lidur2?matur=watermelone"><img src="/static/watermelone.png" width="150"></a>' \
    '<a href="lidur2?matur=fiskur"><img src="/static/fiskur.png" width="150"></a>'

@route('/lidur2')
def lidur2():
    z = request.query.matur
    if z == "pizza" or z=="watermelone" or z =="fiskur":
        return "<h1>Þú valdir að fá: <h1>" \
               '<img src="/static/'+z+'.png" width="200" >' \
               '<a href="/verk2">Til baka</a>'

    else:
        return "<h1>Síða ekki til<h1>"
        "<a href='/verk1'>Til baka</a>"


@error(404)
def error404(error):
    return '<h1>Þessi siða er ekki til</h1>' \
           '<a href="/verk2">Til baka</a>'




@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='../myndir')
run()