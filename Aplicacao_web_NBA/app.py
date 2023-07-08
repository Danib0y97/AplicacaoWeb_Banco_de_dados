from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__, template_folder='C:\\Users\\danie\\OneDrive\Documentos\\GitHub\\AplicacaoWeb_Banco_de_dados\\Aplicacao_web_NBA')

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Iot&tgb27',
    'database': 'bd'
}

@app.route('/', methods=['GET'])
def execute():
    selected_query = request.args.get('queries')  # Obter a consulta selecionada
    result = execute_query(get_query_by_route(selected_query))  # Executar a consulta correspondente à rota
    return render_template('index.html', results=[result])

@app.route('/rota1')
def rota1():
    query = "SELECT COUNT(*) AS total_pivos FROM jogadores JOIN time ON jogadores.TeamID = time.id WHERE time.full_name = 'Los Angeles Lakers' AND jogadores.position = 'Center';" 
    return query

@app.route('/rota2')
def rota2():
    query = "SELECT COUNT(*) AS total_jogadores FROM jogadores WHERE jogadores.Birthdate > 2000;"
    return query

@app.route('/rota3')
def rota3():
    query = "SELECT time.full_name AS nome_time FROM time JOIN jogadores ON time.id = jogadores.TeamID WHERE jogadores.Position = 'Guard' GROUP BY time.id, time.full_name HAVING COUNT(*) > 2;"  
    return query

@app.route('/rota4')
def rota4():
    query = "SELECT Distinct time.full_name AS nome_time FROM time JOIN jogadores ON time.id = jogadores.TeamID  INNER JOIN temporada ON jogadores.Name = temporada.MVP;" 
    return query

@app.route('/rota5')
def rota5():
    query = "Select  jogadores.name  from jogadores  where jogadores.name in ( select jogadores.name from jogadores inner join temporada on jogadores.name = temporada.MVP) Order by Birthdate desc  Limit 1;"  
    return query

@app.route('/rota6')
def rota6():
    query = "select time.full_name, time.year_founded from time where time.year_founded>= all (select time.year_founded from time)"  
    return query

@app.route('/rota7')
def rota7():
    query = "Select time.city, temporada.TimeCampeao, jogos.PontosTimeVisitante FROM temporada  LEFT JOIN jogos ON temporada.TemporadaID = jogos.SeasonID JOIN time ON jogos.idTimeVisitante = time.id where temporada.TimeCampeao = jogos.NomeTimeVisitante and temporada.TemporadaID = 2014;"  
    return query


def get_query_by_route(route):
    if route == 'rota1':
        return rota1()
    elif route == 'rota2':
        return rota2()
    elif route == 'rota3':
        return rota3()
    elif route == 'rota4':
        return rota4()
    elif route == 'rota5':
        return rota5()
    elif route == 'rota6':
        return rota6()
    elif route == 'rota7':
        return rota7()
    else:
        return ""  # Retornar consulta vazia se a rota não for encontrada

def execute_query(query):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        cursor.close()
        connection.close()
        return columns, result
    except mysql.connector.Error as error:
        return f'Erro ao executar a consulta: {error}'

if __name__ == '__main__':
    app.run(debug=True)