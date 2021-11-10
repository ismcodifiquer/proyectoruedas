from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "hola mundo"

@app.route('/otrorecurso')
def otro():
    return '''
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Mi pagina</title>
        </head>
        <body>
            <h1>Mi saludo</h1>
            <p>Hola, mundo</p>
            <table>
                <tr>
                    <th>Company</th>
                    <th>Contact</th>
                    <th>Country</th>
                </tr>
                <tr>
                    <td>Alfreds Futterkiste</td>
                    <td>Maria Anders</td>
                    <td>Germany</td>
                </tr>
                <tr>
                    <td>Centro comercial</td>
                    <td>Ismael Vicente</td>
                    <td>Spain</td>
                </tr>
        </body>
        </html>
    '''