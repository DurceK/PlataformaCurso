import sqlite3

banco  = sqlite3.connect('curso.db')

cursor = banco.cursor()

# Criação da tabela usuarios
# cursor.execute('''
# CREATE TABLE usuarios (
#     id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome VARCHAR(255) NOT NULL,
#     email VARCHAR(255) UNIQUE NOT NULL,
#     senha VARCHAR(255) NOT NULL,
#     tipo_usuario VARCHAR(255) NOT NULL,
#     data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
# );
# ''')

# # Criação da tabela cursos
# cursor.execute('''
# CREATE TABLE cursos (
#     id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
#     titulo VARCHAR(255) NOT NULL,
#     descricao TEXT NOT NULL,
#     id_instrutor INTEGER,
#     categoria VARCHAR(255),
#     preco DECIMAL(10, 2) NOT NULL,
#     data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
#     status VARCHAR(255) DEFAULT 'ativo',
#     FOREIGN KEY (id_instrutor) REFERENCES usuarios(id_usuario)
# );
# ''')

# # Criação da tabela aulas
# cursor.execute('''
# CREATE TABLE  aulas (
#     id_aula INTEGER PRIMARY KEY AUTOINCREMENT,
#     id_curso INTEGER,
#     titulo VARCHAR(255) NOT NULL,
#     descricao TEXT,
#     url_video VARCHAR(255),
#     ordem INTEGER,
#     FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
# );
# ''')

# # Criação da tabela matriculas
# cursor.execute('''
# CREATE TABLE matriculas (
#     id_matricula INTEGER PRIMARY KEY AUTOINCREMENT,
#     id_usuario INTEGER,
#     id_curso INTEGER,
#     data_matricula DATETIME DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
#     FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
# );
# ''')

# # Criação da tabela avaliacoes
# cursor.execute('''
# CREATE TABLE avaliacoes (
#     id_avaliacao INTEGER PRIMARY KEY AUTOINCREMENT,
#     id_curso INTEGER,
#     id_usuario INTEGER,
#     nota DECIMAL(2, 1) CHECK (nota >= 1 AND nota <= 5),
#     comentario TEXT,
#     data_avaliacao DATETIME DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (id_curso) REFERENCES cursos(id_curso),
#     FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
# );
# ''')

# # Criação da tabela compras
# cursor.execute('''
# CREATE TABLE compras (
#     id_compra INTEGER PRIMARY KEY AUTOINCREMENT,
#     id_usuario INTEGER,
#     id_curso INTEGER,
#     valor_pago DECIMAL(10, 2) NOT NULL,
#     data_compra DATETIME DEFAULT CURRENT_TIMESTAMP,
#     metodo_pagamento VARCHAR(255),
#     FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
#     FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
# );
# ''')

# # Criação da tabela categorias
# cursor.execute('''
# CREATE TABLE categorias (
#     id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome VARCHAR(255) NOT NULL,
#     descricao TEXT
# );
# ''')

# # Criação da tabela cupons
# cursor.execute('''
# CREATE TABLE cupons (
#     id_cupom INTEGER PRIMARY KEY AUTOINCREMENT,
#     codigo VARCHAR(50) UNIQUE NOT NULL,
#     desconto DECIMAL(5, 2) NOT NULL,
#     data_validade DATETIME,
#     id_curso INTEGER,
#     FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
# );
# ''')

# Confirma as alterações e fecha a conexão
# banco.commit()
# banco.close()

# print("Tabelas criadas com sucesso!")

# cursor.execute("Select * From categorias")
# print(cursor.fetchall())
