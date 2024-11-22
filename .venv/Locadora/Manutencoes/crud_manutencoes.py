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

# Função para cadastrar os dados da manutenção
def cadastrar(data_ultima_revisao,proxima_revisao,descricao,valor,id_veiculo):
    banco,cursor = conectar_banco()
    # Variável para inserir os dados na tabela
    sql = "INSERT INTO manutencoes(data_ultima_revisao,proxima_revisao,descricao,valor,id_veiculo)VALUES(%s,%s,%s,%s,%s)"
    # Passando os valores para os parâmetros %s
    val = (data_ultima_revisao,proxima_revisao,descricao,valor,id_veiculo)
    # Vamos executar a consulta
    cursor.execute(sql,val)
    # Confirmar a execução da consulta
    banco.commit()
    # Fechar o cursor
    cursor.close()
    # Fechar o banco
    banco.close()

# Função para selecionar os dados
def listar_manuntencoes():
    banco,cursor = conectar_banco()
    # Variável para guardar o retorno do select
    sql = "SELECT * FROM manutencoes"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado:
        print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]} - {i[5]}")
    # Fechar o cursor
    cursor.close()
    # Fechar o banco
    banco.close()

# Função para realizar a atualização dos dados
def atualizar_manutencoes(id, data_ultima_revisao, proxima_revisao, descricao, valor, id_veiculo):
    banco,cursor = conectar_banco()
    sql = "UPDATE manutencoes SET data_ultima_revisao=%s, proxima_revisao=%s, descricao=%s, valor=%s, id_veiculo=%s WHERE id_manutencao=%s"
    val = (data_ultima_revisao, proxima_revisao, descricao, valor, id_veiculo, id)
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Dados atualizados")

# Apagar a manutenção
def apagar_manutencoes(id):
    banco,cursor = conectar_banco()
    sql = "DELETE FROM manutencoes WHERE id_manutencao=%s"
    val = [id]
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Manutenção apagada")