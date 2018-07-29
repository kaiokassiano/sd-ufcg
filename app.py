from flask import Flask
app = Flask(__name__)

# Rota para calculo de fatorial passado por
# parametro em /fatorial/<numero>.
@app.route('/fatorial/<int:numero>')
def calcularFatorial(numero):
    return str(fatorial(numero))

## Calcula o fatorial passado por parametro.
def fatorial(numero):
    if(numero < 0):
        return -1
    if(numero < 2):
        return 1
    return numero * fatorial(numero-1)

if __name__ == '__main__':
    app.run()