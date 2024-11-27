import sqlite3

conexao = sqlite3.connect('meu_banco_de_dados.db')

cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY
AUTOINCREMENT NOT NULL,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
        cidade TEXT NOT NULL
    )
               
''')

nome = input('digite um nome >>')
idade = int(input('digite sua idade >>'))
cidade = input('cidade >>')
cursor.execute('''
    INSERT INTO pessoas (nome, idade, cidade)
    VALUES (?, ?, ?)
''', (nome, idade, cidade))

conexao.commit()

cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()

for pessoas in pessoas:
    print(f'''ID: {pessoas[0]}, NOME: {pessoas[1]}, idade{pessoas[2]}, cidade: {pessoas[3]}''')

conexao.close()