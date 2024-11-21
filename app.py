from flask import Flask, render_template, request
from datos import dato
app = Flask(__name__)
app.config["DEBUG"] = True  # Modo debug habilitado

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acerca', methods=['GET'])
def acerca():
    return render_template('acerca.html')

@app.route('/region', methods=['GET'])
def region():
    return render_template('/region.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    nombre = request.form['Nombre']
    return render_template('/resultado.html', nombre=nombre)

@app.route('/<region>', methods=['POST'])
def show_region_page(region):
    region = request.form.get('region')
    if region == '0':
        return render_template('/region.html')
    # Accede a la región específica
    region_dato = dato.get(region.lower())
    if not region_dato:
        return "No hay datos disponibles para esta región.", 404
    total_muertos = 0
    for desastre in region_dato:
     #Calcular total de víctimas
        total_muertos = total_muertos + desastre['muertos']
    return render_template('resultado.html', region=region.capitalize(), desastres=region_dato, total_muertos=total_muertos)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)
