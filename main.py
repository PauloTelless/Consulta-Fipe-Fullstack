from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/fipe', methods=['POST'])
def get_fipe_vehicle():
    anoModelo = int(request.form.get('ano'))
    codigoFipe = request.form.get('codigo')
    link = f'https://brasilapi.com.br/api/fipe/preco/v1/{codigoFipe}'
    tabelaFipe = requests.get(link).json()
    for fipe in tabelaFipe:
        if fipe['anoModelo'] == anoModelo: #retorna todas as informações a partir do ano
            valor = str(fipe['valor'])
            modeloCarro = fipe['modelo']
            marcaCarro = fipe['marca']
            return render_template('fipe.html', valor=valor, ano=anoModelo, modelo=modeloCarro, marca=marcaCarro) #retorna a página onde as informações irão ficar
            
if __name__ == '__main__':
    app.run(debug=True)
