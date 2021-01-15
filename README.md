# Api_IBovespa_Python

Api para consultas simples de ações brasileiras com intuito de criar um projeto em flask , foram utilizadas as seguintes bibliotecas:

    Flask
    SqlAlchemy

Para obter os dados das ações os seguintes dominios são consultados:

    "https://statusinvest.com.br/acoes"
    "https://query1.finance.yahoo.com/v8/finance/chart/XXX.SA"
    "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=XXX.SAO&apikey=XXX"
    "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=XXX.SAO&outputsize=full&apikey=XXX"

Pelo fato do consumo ser de dominios externos , peço que não utilizem com respeito a aplicação.

Para utilizar o servidor você precisa de uma chave da Api AlphaVantage:

    Para ter uma chave basta acessar o link abaixo e concluir seu cadastro:
    
      https://www.alphavantage.co/support/#api-key

Para rodar o servidor devemos instalar as seguintes dependencias:

    Isso pode ser feito tanto de forma global quanto em uma venv
    
    pip install flask_sqlalchemy
    pip install flask
    pip install sqlalchemy

Com todos os pacotes instalados podemos rodar o sevidor:
    
    python run.py
    
Para acessa-lo basta abrir uma janela em qualquer navegador e digitar na barra de busca:

    http://localhost:5000
    
As consultas possiveis sao de uma lista de ações ja consultadas anteriormente ou de uma ação de forma unitaria:

    http://localhost:5000/tick/prio3/"Chave AlphaVantage" => Isto retorna os dados da prio3 
    
    http://localhost:5000/tick/"Chave AlphaVantage" => Isto retorna os dados de todas as ações ja consultadas
    
Meus agradecimentos, façam bom uso :)
