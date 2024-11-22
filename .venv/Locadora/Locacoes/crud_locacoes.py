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

# Função para cadastrar os dados da locação
def cadastrar(data_inicio, data_fim, valor_total, id_veiculo, id_cliente, forma_pagamento):
    banco,cursor = conectar_banco()
    # Variável para inserir os dados na tabela
    sql = "INSERT INTO locacoes(data_inicio, data_fim, valor_total, id_veiculo, id_cliente, forma_pagamento)VALUES(%s,%s,%s,%s,%s,%s)"
    # Passando os valores para os parâmetros %s
    val = (data_inicio, data_fim, valor_total, id_veiculo, id_cliente, forma_pagamento)
    # Vamos executar a consulta
    cursor.execute(sql,val)
    # Confirmar a execução da consulta
    banco.commit()
    # Fechar o cursor
    cursor.close()
    # Fechar o banco
    banco.close()

# Função para selecionar os dados
def listar_locacoes():
    banco,cursor = conectar_banco()
    # Variável para guardar o retorno do select
    sql = "SELECT * FROM locacoes"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado:
        print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]} - {i[5]} - {i[6]}")
    # Fechar o cursor
    cursor.close()
    # Fechar o banco
    banco.close()

# Função para realizar a atualização dos dados
def atualizar_locacoes(id, data_inicio, data_fim, valor_total, id_veiculo, id_cliente, forma_pagamento):
    banco,cursor = conectar_banco()
    sql = "UPDATE locacoes SET data_inicio=%s, data_fim=%s, valor_total=%s, id_veiculo=%s, id_cliente=%s, forma_pagamento=%s WHERE id_locacao=%s"
    val = (data_inicio, data_fim, valor_total, id_veiculo, id_cliente, forma_pagamento, id)
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Dados atualizados")

# Apagar a locação
def apagar_locacoes(id):
    banco,cursor = conectar_banco()
    sql = "DELETE FROM locacoes WHERE id_locacao=%s"
    val = [id]
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Locação apagada")