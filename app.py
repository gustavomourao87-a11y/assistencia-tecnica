from flask import Flask, render_template, request, redirect
from database import conectar

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/clientes", methods=["GET", "POST"])
def clientes():
    if request.method == "POST":
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        email = request.form["email"]
        endereco = request.form["endereco"]

        conexao = conectar()

        conexao.execute("""
            INSERT INTO clientes (nome, telefone, email, endereco)
            VALUES (?, ?, ?, ?)
        """, (nome, telefone, email, endereco))

        conexao.commit()
        conexao.close()

        return redirect("/clientes")

    conexao = conectar()

    clientes = conexao.execute(
        "SELECT * FROM clientes"
    ).fetchall()

    conexao.close()

    return render_template("clientes.html", clientes=clientes)


@app.route("/clientes/excluir/<int:id>")
def excluir_cliente(id):
    conexao = conectar()

    conexao.execute(
        "DELETE FROM clientes WHERE id = ?",
        (id,)
    )

    conexao.commit()
    conexao.close()

    return redirect("/clientes")


if __name__ == "__main__":
    app.run(debug=True)