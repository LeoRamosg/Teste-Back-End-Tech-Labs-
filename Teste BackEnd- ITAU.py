from flask import Flask, jsonify, request 

app = Flask(__name__)

Pessoas = [
    {
        'id': '',
        'Nome completo':'' ,
        'Data de nacimento':'' ,
        'Endereco':'' ,
        'CPF':'',
        'Estado civil':'' 
  
    },
]

# Consultar (todos)
@app.route('/Pessoas',methods=['GET'])
def obter_pessoas():
    return jsonify(Pessoas)

# Consultar (id)
@app.route('/Pessoas/<int:id>',methods=['GET'])
def obter_pessoas_por_id(id):
    for Pessoa in Pessoas:
       if Pessoa.get('id') == id:
           return jsonify(Pessoa)
# Editar 
@app.route('/Pessoas/<int:id>', methods=['PUT'])
def editar_Pessoas_por_id(id):
        Pessoa_alterada = request.get_json()
        for indice,Pessoa in enumerate(Pessoas):
             print(Pessoa)
             if Pessoa.get('id') == id:
                Pessoas[indice].update(Pessoa_alterada)
                return jsonify(Pessoas[indice])
# Criar
@app.route('/Pessoas', methods=['POST'])
def incluir_nova_Pessoa():
    nova_Pessoa = request.get_json()
    Pessoas.append(nova_Pessoa)

    return jsonify(Pessoas)

# Excluir
@app.route('/Pessoas/<int:id>', methods=['DELETE'])
def excluir_pessoa(id):
     for indice, Pessoa in enumerate(Pessoas):
         if Pessoa.get('id') == id:
             del Pessoas[indice]

     return jsonify(Pessoas)
app.run(port=5000,host='localhost',debug=True)
