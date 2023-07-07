from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__, template_folder='C:\\Users\\danie\\OneDrive\Documentos\\GitHub\\AplicacaoWeb_Banco_de_dados\\Aplicacao_web_NBA')

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Iot&tgb27',
    'database': 'bd'
}

# Página inicial da aplicação
@app.route('/consulta', methods=['POST'])
def index():
    valor_desejado = request.form.get('valor')
    # Estabeleça a conexão com o banco de dados
    conexao = mysql.connector.connect(**db_config)

    # Crie um cursor para executar as consultas
    cursor = conexao.cursor()

    # Defina a consulta
    consulta = "SELECT COUNT(*) AS total_jogadores FROM jogadores WHERE jogadores.Birthdate > %s"

    # Parâmetros para a consulta
    parametros = ("valor_desejado",)

    # Execute a consulta
    cursor.execute(consulta, parametros)

    # Obtenha os resultados da consulta
    resultados = cursor.fetchall()

    # Feche o cursor e a conexão
    #cursor.close()
   # conexao.close()

    # Renderize o template HTML com os resultados
    return render_template('index2.html', resultados=resultados)

if __name__ == '__main__':
    app.run()