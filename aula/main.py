from flask import Flask
from routes.home import bp_home
from routes.cliente import bp_cliente

app = Flask(__name__)

app.register_blueprint(bp_home)
app.register_blueprint(bp_cliente, url_prefix='/clientes')

app.run(debug=True)
