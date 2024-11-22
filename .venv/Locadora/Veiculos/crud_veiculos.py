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

# Função para cadastrar os dados do veículo
def cadastrar(marca,modelo,ano,placa,cor,tipo_combustivel,quilometragem,status):
    banco,cursor = conectar_banco()
    # Variável para inserir os dados na tabela
    sql = "INSERT INTO veiculos(marca,modelo,ano,placa,cor,tipo_combustivel,quilometragem,status)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    # Passando os valores para os parâmetros %s
    val = (marca,modelo,ano,placa,cor,tipo_combustivel,quilometragem,status)
    # Vamos executar a consulta
    cursor.execute(sql,val)
    # Confirmar a execução da consulta
    banco.commit()
    # Fechar o cursor
    cursor.close()
    # Fechar o banco
    banco.close()

# Função para selecionar os dados
def listar_veiculos():
    banco,cursor = conectar_banco()
    # Variável para guardar o retorno do select
    sql = "SELECT * FROM veiculos"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado:
        print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]} - {i[5]} - {i[6]} - {i[7]} - {i[8]}")
    # Fechar o cursor
    cursor.close()
    # Fechar o banco
    banco.close()

# Função para realizar a atualização dos dados
def atualizar_veiculos(id,marca,modelo,ano,placa,cor,tipo_combustivel,quilometragem,status):
    banco,cursor = conectar_banco()
    sql = "UPDATE veiculos SET marca=%s, modelo=%s, ano=%s, placa=%s, cor=%s, tipo_combustivel=%s, quilometragem=%s, status=%s WHERE id_veiculo=%s"
    val = (marca,modelo,ano,placa,cor,tipo_combustivel,quilometragem,status,id)
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Dados atualizados")

# Apagar o veiculo
def apagar_veiculos(id):
    banco,cursor = conectar_banco()
    sql = "DELETE FROM veiculos WHERE id_veiculo=%s"
    val = [id]
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Veículo apagado")