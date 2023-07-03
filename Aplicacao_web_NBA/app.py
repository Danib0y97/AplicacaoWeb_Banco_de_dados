from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__, template_folder='D:\Aplicacao_web_NBA')


# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Iot&tgb27',
    'database': 'bd'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        result = execute_query(query)
        return render_template('index.html', result=result)

    return render_template('index.html')

def execute_query(query):
    try:
       connection = mysql.connector.connect(**db_config)
       cursor = connection.cursor()
       cursor.execute(query)
       result = cursor.fetchall()
       cursor.close()
       connection.close()
       return result
    except mysql.connector.Error as error:
        return f'Erro ao executar a consulta: {error}'

if __name__ == '__main__':
    app.run(debug=True)