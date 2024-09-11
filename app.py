from flask import Flask, request
from database import DatabaseConnection
from api_handler import LeadAPIHandler  # Certifique-se de que o nome do arquivo seja correto

# Configuração básica do Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando a conexão com o banco de dados
db_connection = DatabaseConnection(app)
db_connection.initialize_db(app)  # Passa o app corretamente para inicializar o banco de dados

# Inicializando a API com as rotas
api_handler = LeadAPIHandler(app, db_connection.get_db())

if __name__ == '__main__':
    app.run(debug=True)