# Importar o drive de comunicação do Python com o MySQL
import mysql.connector as mc

# Vamos criar uma função para estabelecer a conexâo com o banco de dados todas as vezes que 
# for executar uma consulta em uma das tabelas, esta função pode ser utilizada.
def conectar_banco():
    banco = mc.connect(
        host="127.0.0.1",
        port=3307,
        user="root",
        password="",
        database="biblioteca"
    )
    cursor = banco.cursor()
    return banco,cursor

# Função para cadastrar os dados do bibliotecário
def cadastrar(nome,email,telefone):
    banco,cursor = conectar_banco()
    # Variável para inserir os dados na tabela
    sql = "INSERT INTO bibliotecario(nome,email,telefone)VALUES(%s,%s,%s)"
    # Passando os valores para os parâmetros %s
    val = (nome,email,telefone)
    # Vamos executar a consulta
    cursor.execute(sql,val)
    # Confirmar a execução da consulta
    banco.commit()
    # Fechar o cursor
    cursor.close()
    # Fechar o banco
    banco.close()

# Função para selecionar os dados
def listar_bibliotecarios():
    banco,cursor = conectar_banco()
    # Variável para guardar o retorno do select
    sql = "SELECT * FROM bibliotecario"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado:
        print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]}")
    
    # Fechar o cursor
    cursor.close()
    # Fechar o banco
    banco.close()

# Função para realizar a atualização dos dados
def atualizar_bibliotecario(id, nome, email, telefone):
    banco,cursor = conectar_banco()
    sql = "UPDATE bibliotecario SET nome=%s, email=%s, telefone=%s WHERE id_bibliotecario=%s"
    val = (nome,email,telefone,id)
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Dados atualizados")

# Apagar o bibliotecario
def apagar_bibliotecario(id):
    banco,cursor = conectar_banco()
    sql = "DELETE FROM bibliotecario WHERE id_bibliotecario=%s"
    val = [id]
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Bibliotecario apagado")