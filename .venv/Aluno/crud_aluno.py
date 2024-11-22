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

# Função para cadastrar os dados do aluno
def cadastrar(nome,matricula,curso,email,telefone):
    banco,cursor = conectar_banco()
    # Variável para inserir os dados na tabela
    sql = "INSERT INTO aluno(nome,matricula,curso,email,telefone)VALUES(%s,%s,%s,%s,%s)"
    # Passando os valores para os parâmetros %s
    val = (nome,matricula,curso,email,telefone)
    # Vamos executar a consulta
    cursor.execute(sql,val)
    # Confirmar a execução da consulta
    banco.commit()
    # Fechar o cursor
    cursor.close()
    # Fechar o banco
    banco.close()

# Função para selecionar os dados
def listar_aluno():
    banco,cursor = conectar_banco()
    # Variável para guardar o retorno do select
    sql = "SELECT * FROM aluno"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado:
        print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]} - {i[5]}")
    
    # Fechar o cursor
    cursor.close()
    # Fechar o banco
    banco.close()

# Função para realizar a atualização dos dados
def atualizar_aluno(id, nome, matricula, curso, email, telefone):
    banco,cursor = conectar_banco()
    sql = "UPDATE aluno SET nome=%s, matricula=%s, curso=%s, email=%s, telefone=%s WHERE id_aluno=%s"
    val = (nome,matricula,curso,email,telefone,id)
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Dados atualizados")

# Apagar o aluno
def apagar_aluno(id):
    banco,cursor = conectar_banco()
    sql = "DELETE FROM aluno WHERE id_aluno=%s"
    val = [id]
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Aluno apagado")