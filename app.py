from flask import Flask
from database import DatabaseConnection
from api_handler import LeadAPIHandler
from telemetry import TelemetryLogger

# Configuração básica do Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando a conexão com o banco de dados
db_connection = DatabaseConnection(app)
db_connection.initialize_db()

# Registrando telemetria
telemetry = TelemetryLogger()

@app.before_request
def log_telemetry():
	telemetry.log_access(request.path, request.method)

# Inicializando a API com as rotas
api_handler = LeadAPIHandler(app, db_connection.get_db())

if __name__ == '__main__':
	app.run(debug=True)




