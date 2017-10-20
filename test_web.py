
from gastos_operacion import utilidad_operacion, gastos_operacion
from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def home() -> '302':
    return redirect('/home')


@app.route('/home')
def go_home() -> 'html':
    return render_template('home.html',
                           the_title='Bienvenido al calculo de gastos y utilidades de operación')


@app.route('/entry')
def go_entry() -> 'html':
    return render_template('entry.html',
                           the_title='Bienvenido al formulario')

@app.route('/entry1')
def go_entry1() -> 'html':
    return render_template('entry1.html',
                           the_title='Bienvenido al formulario')


@app.route('/calculate', methods=['POST'])
def calculate() -> 'html':
    utidad_bruta = float(request.form['utilidad_bruta'])
    gastos_de_operacion = float(request.form['gastos_de_operacion'])
    result= utilidad_operacion(utidad_bruta, gastos_de_operacion)
    title = "Utilidad de Operacion"
    return render_template('results.html',
                           the_utilidad_bruta=utidad_bruta,
                           the_gastos_de_operacion=gastos_de_operacion,
                           the_results=result,
                           the_title=title)


@app.route('/calculate2', methods=['POST'])
def calculate2() -> 'html':
    gastos_ventas = float(request.form['gastos_ventas'])
    gastos_admon = float(request.form['gastos_admon'])
    gastos = float(request.form['gastos'])
    productos_finian = float(request.form['productos_finian'])
    result=gastos_operacion(gastos_ventas, gastos_admon, gastos, productos_finian)
    title = "Gastos de operación"
    return render_template('results2.html',
                           the_gastos_ventas=gastos_ventas,
                           the_gastos_admon=gastos_admon,
                           the_gastos=gastos,
                           the_productos_finiancieros=productos_finian,
                           the_results=result,
                           the_title=title)


app.run(debug=True)
