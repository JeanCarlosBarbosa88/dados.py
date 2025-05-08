Sistema de Integração com a API da CIB2B e Banco de Dados MySQL

Este projeto implementa uma aplicação web utilizando Flask, que realiza uma requisição GET à API da plataforma CIB2B para consultar dados de fornecedores. Os dados obtidos são armazenados em um banco de dados MySQL, permitindo consultas posteriores através de uma interface web.

 Requisitos

 Python 3.x
 Flask
 Requests
 Pandas
 SQLAlchemy
 PyMySQL

Para instalar as dependências, execute o seguinte comando:

pip install flask requests pandas sqlalchemy pymysql


Integração com a API da CIB2B

A aplicação realiza uma requisição GET à API da plataforma CIB2B para consultar dados de fornecedores. A URL da API é:

https://www.cib2b.com.br/

Após obter a resposta da API, o código tenta converter os dados para o formato JSON e, em seguida, para um DataFrame do Pandas. Caso a conversão seja bem-sucedida, os dados são armazenados em um banco de dados MySQL.

Armazenamento no Banco de Dados MySQL

A aplicação utiliza SQLAlchemy para interagir com o banco de dados MySQL. As credenciais de acesso são:

  Usuário: root
  Senha: 123456
  Host: localhost
  Porta: 3306
  Banco de dados: cib2b

Os dados obtidos da API são armazenados na tabela `fornecedor`. Caso a tabela já exista, ela é substituída pelos novos dados.

Interface Web com Flask

A aplicação fornece uma interface web simples utilizando Flask. A rota `/buscar` permite que o usuário envie um critério de pesquisa através de um formulário. O critério é utilizado para consultar a tabela `fornecedor` no banco de dados MySQL, retornando os 10 primeiros resultados ordenados por preço, qualidade e logística.

A consulta SQL utilizada é:

```sql
SElECT produto, preco, qualidade, logistica
FROM nome_da_tabela
WHERE produto ILIKE '%{criterio}%'
ORDER BY preco ASC, qualidade DESC, logistica DESC
LIMIT 10;
```
Os resultados são apresentados em uma tabela HTML na página resultados.html.

Como Executar

1. Clone este repositório em sua máquina local.

2. Certifique-se de ter o Python 3.x instalado.

3. Instale as dependências listadas acima.

4. Crie um banco de dados MySQL chamado (cib2b) e configure a tabela `fornecedor` conforme necessário.

5. Execute o script Python:
python nome_do_arquivo.py

6. Acesse a aplicação web no navegador:
http://127.0.0.1:5000/

7. Utilize o formulário na rota /buscar para consultar os fornecedores.

Observações

A API da CIB2B não fornece documentação pública detalhada sobre os endpoints disponíveis. Para obter informações adicionais sobre a API, entre em contato com o suporte da plataforma.
A consulta SQL utiliza o operador ILIKE para realizar uma busca insensível a maiúsculas e minúsculas. Certifique-se de que o banco de dados MySQL esteja configurado para suportar esse operador ou ajuste a consulta conforme necessário.
A tabela fornecedor no banco de dados deve ter as colunas produto, preco, qualidade e logistica para que a consulta funcione corretamente.
