# realizar uma requisão GET a API 
import requests
import pandas as pd
from flask import Flask, render_template, request
from sqlalchemy import create_engine
import pymysql  # Ensure pymysql is imported for MySQL connection

app = Flask(__name__)

# consutar fornecedor
url_api = "https://www.cib2b.com.br/"

response = requests.get(url_api)

# Verificar a requisição 
try:
    dados = response.json()  # converte o JSON em um data frame
    df = pd.DataFrame(dados)
except ValueError:
    print("Erro ao converter a resposta da API para JSON.")
    df = pd.DataFrame()  # Cria um DataFrame vazio para evitar erros posteriores
else:
    print("Erro ao acessar a API:", response.status_code)  
    
from sqlalchemy import create_engine
# Conectar ao banco de dados
usuario = 'root'
senha = '123456'
host = 'localhost'
porta = '3306'
banco = 'cib2b'
# Criar a string de conexão
engine = create_engine(f'mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}')
if not df.empty:
    df.to_sql('fornecedor', con=engine, if_exists='replace', index=False)
else:
    print("DataFrame está vazio. Nenhum dado foi salvo no banco de dados.")

# armazenar o dataframe no banco de dados
df.to_sql('fornecedor', con=engine, if_exists='replace', index=False)
@app.route('/buscar', methods=['POST'])
def buscar_produtos():
    criterio = request.form['criterio']
    query = f"""
        SELECT produto, preco, qualidade, logistica
        FROM nome_da_tabela
        WHERE produto ILIKE '%{criterio}%'
        ORDER BY preco ASC, qualidade DESC, logistica DESC
        LIMIT 10;
        """
    resultados = pd.read_sql(query, engine)
    return render_template('resultados.html', tabelas=[resultados.to_html(classes='data')], titulos=resultados.columns.values)

if __name__ == '__main__':
    app.run(debug=True)     