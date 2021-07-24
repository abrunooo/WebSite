from flask  import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/topic')
def topic():
    return render_template('topic.html')

@app.route('/biologia')
def Biología():
    return render_template('biologia.html')

@app.route('/ccff')
def ccff():
    return render_template('ccff.html')
    

@app.route('/quimica')
def Química():
    return render_template('quimica.html')

@app.route('/informatica')
def Informática():
    return render_template('info.html')

@app.route('/matematica')
def Matemática():
    return render_template('mate.html')

@app.route('/sociales')
def Sociales():
    return render_template('sociales.html')

@app.route('/lenguaje')
def Lengua():
    return render_template('lengua.html')

@app.route('/literatura')
def Literatura():
    return render_template('lite.html')

@app.route('/geografia')
def Geografía():
    return render_template('geo.html')

@app.route('/musica')
def Música():
    return render_template('musica.html')

@app.route('/plastica')
def Plástica():
    return render_template('pl.html')

@app.route('/opv')
def OPV():
    return render_template('opv.html')

@app.route('/ig')
def IG():
    return render_template('ig.html')


if __name__=='__main__':
    app.run(debug=True, port=5050)