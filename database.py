import sqlite3


def conectar():
    conexao = sqlite3.connect("assistencia.db")
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_banco():
    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT,
            endereco TEXT
        )
    """)

    conexao.commit()
    conexao.close()


if __name__ == "__main__":
    criar_banco()
    print("Banco de dados criado com sucesso!")