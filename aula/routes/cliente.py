from flask import Blueprint, render_template, request
from database.clientes import CLIENTES

bp_cliente = Blueprint('cliente', __name__)

# lista os clientes
@bp_cliente.route('/')
def lista_cliente():
    return render_template('lista_clientes.html', clientes=CLIENTES)

# Inserir dados do cliente
@bp_cliente.route('/', methods=['POST'])
def inserir_cliente():
    data = request.json

    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome": data["nome"],
        "email": data['email'],
    }

    CLIENTES.append(novo_usuario)
    return render_template('item_cliente.html', cliente=novo_usuario)

# Formulario para cadastrar um cliente
@bp_cliente.route('/new')
def form_cliente():
    return render_template('form_cliente.html')

# Exibir detalhes do cliente
@bp_cliente.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    pass

# FOrmulario para editar cliente
@bp_cliente.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    pass

# FOrmulario para atualizar cliente
@bp_cliente.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    pass

# deletar cliente
@bp_cliente.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    pass
