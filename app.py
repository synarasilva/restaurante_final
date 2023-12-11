from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import base64
import jsonify


#cria o objeto app
app = Flask(__name__ , static_folder='static')

# conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('database\sqlite.db')
    conn.row_factory = sqlite3.Row
    return conn

# Rota para o painel de administração
@app.route("/login")
def admin_panel():    
    return render_template('admin2/login.html')

# Rota para listar categorias
@app.route("/admin/listar_categorias")
def listar_categorias():
    conn = get_db_connection()
    categorias = conn.execute('SELECT * FROM categorias').fetchall()
    conn.close()
    return render_template('admin2/listar_categorias.html', categorias=categorias)



# Rota para cadastrar categoria
@app.route("/admin/cadastrar_categoria", methods = ['GET', 'POST'])
def cadastrar_categoria():
    if request.method == 'POST':
        nome_categoria = request.form.get('nome_categoria')
        descricao = request.form.get('descricao')
        imagem = request.files.get('imagem')  # Obtém o arquivo de imagem enviado

        if nome_categoria:
            conn = get_db_connection()

            if imagem:  # Se uma imagem foi enviada
                imagem_base64 = base64.b64encode(imagem.read()).decode('utf-8')
                conn.execute('INSERT INTO categorias (nome, descricao, imagem) VALUES (?, ?, ?)',
                             (nome_categoria, descricao, imagem_base64))
            else:
                conn.execute('INSERT INTO categorias (nome, descricao) VALUES (?, ?)',
                             (nome_categoria, descricao))

            conn.commit()
            conn.close()
            return redirect(url_for('listar_categorias'))
        
    return render_template('admin2/cadastrar_categoria.html')

# Rota para excluir categoria
@app.route("/admin/excluir_categoria/<int:id>", methods=['GET', 'POST'])
def excluir_categoria(id):
    conn = get_db_connection()
    categorias = conn.execute('SELECT * FROM categorias WHERE id = ?',(id,)).fetchone()

    if request.method == 'POST':
        conn.execute('DELETE FROM categorias WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('listar_categorias'))
    conn.close()
    return render_template('/admin2/excluir_categoria.html', categorias=categorias)


# Rota para editar categoria
@app.route("/admin/editar_categoria/<int:id>", methods=['GET', 'POST'])
def editar_categoria(id):
    conn = get_db_connection()
    categorias = conn.execute('SELECT * FROM categorias WHERE id = ?', (id,)).fetchone()    
    if request.method == 'POST':
        nome_categoria = request.form.get('nome_categoria')
        descricao = request.form.get('descricao')
        imagem = request.files.get('imagem')

        if nome_categoria:
            conn.execute('UPDATE categorias SET nome=?, descricao=?, imagem=? WHERE id=?', 
                         (nome_categoria, descricao,imagem, id,))

            conn.commit()
            conn.close()
            return redirect(url_for('listar_categorias'))
    
    conn.close()
    return render_template('/admin2/editar_categoria.html', categorias=categorias)



# Rotas listar Pratos
@app.route("/admin/listar_pratos")
def listar_pratos():
    conn = get_db_connection()
    pratos = conn.execute('SELECT * FROM pratos').fetchall()
    conn.close()
    return render_template('admin2/listar_pratos.html', pratos=pratos)

# Rota para cadastrar Pratos
@app.route("/admin/cadastrar_pratos", methods = ['GET', 'POST'])
def cadastrar_pratos():
    if request.method == 'POST':
        nome_pratos = request.form.get('nome_pratos')
        descricao = request.form.get('descricao')
        imagem = request.files.get('imagem')  # Obtém o arquivo de imagem enviado
        categoria_id = request.form.get('categoria_id')
        if cadastrar_pratos:
            conn = get_db_connection()

            if imagem:  # Se uma imagem foi enviada
                imagem_base64 = base64.b64encode(imagem.read()).decode('utf-8')
                conn.execute('INSERT INTO pratos (nome, descricao, imagem, categoria_id) VALUES (?, ?, ?, ?)',
                             (nome_pratos, descricao, imagem_base64, categoria_id,))
            else:
                conn.execute('INSERT INTO pratos (nome, descricao) VALUES (?, ?)',
                             (nome_pratos, descricao))

            conn.commit()
            conn.close()
            return redirect(url_for('listar_pratos'))
    return render_template('admin2/cadastrar_prato.html')


# Rota para excluir prato
@app.route("/admin/excluir_pratos/<int:id>", methods=['GET', 'POST'])
def excluir_pratos(id):
    conn = get_db_connection()
    pratos = conn.execute('SELECT * FROM pratos WHERE id = ?',(id,)).fetchone()

    if request.method == 'POST':
        conn.execute('DELETE FROM pratos WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('listar_pratos'))
    conn.close()
    return render_template('/admin2/excluir_prato.html', pratos=pratos)

# Rota para editar Pratos
@app.route("/admin/editar_pratos/<int:id>", methods=['GET', 'POST'])
def editar_pratos(id):
    conn = get_db_connection()
    pratos = conn.execute('SELECT * FROM pratos WHERE id = ?', (id,)).fetchone()
    
    if request.method == 'POST':
        nome_pratos = request.form.get('nome_pratos')
        descricao = request.form.get('descricao')
        imagem = request.files.get('imagem') # Obtém o arquivo de imagem enviado
        categoria_id = request.form.get('categoria_id') 
        if nome_pratos:
            conn = get_db_connection()

            if imagem:  # Se uma imagem foi enviada
                imagem_base64 = base64.b64encode(imagem.read()).decode('utf-8')
              
                conn.execute('UPDATE pratos SET nome=?, descricao=?,image=?,categoria_id,=? WHERE id=?', 
                         (nome_pratos, descricao,imagem_base64, categoria_id, id,))
            conn.commit()
            conn.close()
            return redirect(url_for('listar_pratos'))
    
    conn.close()
    return render_template('/admin2/editar_prato.html', pratos=pratos)

# Rota para cardapio

@app.route("/cardapio")
def cardapio():
    conn = get_db_connection()
    categorias = conn.execute('SELECT * FROM categorias').fetchall()
    pratos = conn.execute('SELECT * FROM pratos').fetchall()

    conn.commit()
    conn.close()
    return render_template('cardapio.html', categorias=categorias, pratos=pratos)


# Rota para retornar ir para o painel
@app.route("/admin/painel")
def admin():
    return render_template('admin2/painel.html')

@app.route("/dashboard")
def dasboard():
    return render_template('admin2/painel.html')

#Rota pra lista os pratos pelo id
@app.route("/listar/<int:id>", methods=['GET'])
def listar(id):
    conn = get_db_connection()
    categorias = conn.execute('SELECT * FROM categorias WHERE id = ?', (id,)).fetchone()    
    pratos = conn.execute( 'SELECT * FROM pratos WHERE categoria_id=?', (id,)).fetchall()
    conn.commit()
    conn.close()
    return render_template('listar.html',pratos=pratos, categorias=categorias)


# Rota para página reserva de mesas
@app.route('/admin/reserva', methods=['GET', 'POST'])
def reserva():
    if request.method == 'POST':
        nome = request.form.get('nome')
        data = request.form.get('data')

        # Certifique-se de ter a função get_db_connection no arquivo db.py
        conn = get_db_connection()
        conn.execute('INSERT INTO reserva (nome, data) VALUES (?, ?)',
                     (nome, data))

        conn.commit()
        conn.close()
        return redirect(url_for('lista_reserva'))
    return render_template('admin2/reserva.html')


@app.route("/comprar")
def comprar():
    return render_template('comprar.html')

@app.route("/admin/listar_reserva", methods=['GET'])
def listar_reserva():
    conn = get_db_connection()
    reserva = conn.execute('SELECT * FROM reserva').fetchall()
    conn.close()
    return render_template('admin2/listar_reserva.html', reserva=reserva)
# Rota para Contatos
@app.route("/contatos")
def contatos():
    return render_template('contatos.html')
# cria a rota index
@app.route("/")
def index():
    conn = get_db_connection()
    categorias = conn.execute('SELECT * FROM categorias').fetchall()
    pratos = conn.execute('SELECT * FROM pratos').fetchall()
    conn.commit()
    conn.close()
    return render_template('index.html', categorias=categorias, pratos=pratos)

@app.route("/logout")
def logout():
    return redirect('/')

app.run(debug=True)