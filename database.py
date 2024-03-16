import sqlite3

class Database:
    def __init__(self, db_name="usuarios.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY,
                                nome TEXT NOT NULL,
                                idade INTEGER NOT NULL)''')
        self.conn.commit()

    def insert_usuario(self, nome, idade):
        self.cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
        self.conn.commit()

    def get_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()

    def update_usuario(self, id, nome, idade):
        self.cursor.execute("UPDATE usuarios SET nome=?, idade=? WHERE id=?", (nome, idade, id))
        self.conn.commit()

    def delete_usuario(self, id):
        self.cursor.execute("DELETE FROM usuarios WHERE id=?", (id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
