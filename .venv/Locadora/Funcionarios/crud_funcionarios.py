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
        database="locadora"
    )
    cursor = banco.cursor()
    return banco,cursor

# Função para cadastrar os dados do funcionario
def cadastrar(nome,cargo,salario,data_contratacao):
    banco,cursor = conectar_banco()
    # Variável para inserir os dados na tabela
    sql = "INSERT INTO funcionarios(nome,cargo,salario,data_contratacao)VALUES(%s,%s,%s,%s)"
    # Passando os valores para os parâmetros %s
    val = (nome,cargo,salario,data_contratacao)
    # Vamos executar a consulta
    cursor.execute(sql,val)
    # Confirmar a execução da consulta
    banco.commit()
    # Fechar o cursor
    cursor.close()
    # Fechar o banco
    banco.close()

# Função para selecionar os dados
def listar_funcionarios():
    banco,cursor = conectar_banco()
    # Variável para guardar o retorno do select
    sql = "SELECT * FROM funcionarios"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado:
        print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]}")
    # Fechar o cursor
    cursor.close()
    # Fechar o banco
    banco.close()

# Função para realizar a atualização dos dados
def atualizar_funcionarios(id, nome, cargo, salario, data_contratacao):
    banco,cursor = conectar_banco()
    sql = "UPDATE funcionarios SET nome=%s, cargo=%s, salario=%s data_contratacao=%s WHERE id_funcionario=%s"
    val = (nome,cargo,salario,data_contratacao,id)
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Dados atualizados")

# Apagar o funcionario
def apagar_funcionario(id):
    banco,cursor = conectar_banco()
    sql = "DELETE FROM funcionario WHERE id_funcionario=%s"
    val = [id]
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Funcionario apagado")