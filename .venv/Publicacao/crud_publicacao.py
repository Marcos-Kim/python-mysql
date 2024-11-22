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

# Função para cadastrar os dados de publicação
def cadastrar(titulo,autor,editora,data_publicacao,isbn,assunto,tipo_publicacao,palavras_chave,quantidade,localizacao):
    banco,cursor = conectar_banco()
    # Variável para inserir os dados na tabela
    sql = "INSERT INTO publicacao(titulo,autor,editora,data_publicacao,isbn,assunto,tipo_publicacao,palavras_chave,quantidade,localizacao)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # Passando os valores para os parâmetros %s
    val = (titulo,autor,editora,data_publicacao,isbn,assunto,tipo_publicacao,palavras_chave,quantidade,localizacao)
    # Vamos executar a consulta
    cursor.execute(sql,val)
    # Confirmar a execução da consulta
    banco.commit()
    # Fechar o cursor
    cursor.close()
    # Fechar o banco
    banco.close()

# Função para selecionar os dados
def listar_publicacao():
    banco,cursor = conectar_banco()
    # Variável para guardar o retorno do select
    sql = "SELECT * FROM publicacao"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado:
        print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]} - {i[5]} - {i[6]} - {i[7]} - {i[8]} - {i[9]} - {i[10]}")
    # Fechar o cursor
    cursor.close()
    # Fechar o banco
    banco.close()

# Função para realizar a atualização dos dados
def atualizar_publicacao(id,titulo,autor,editora,data_publicacao,isbn,assunto,tipo_publicacao,palavras_chave,quantidade,localizacao):
    banco,cursor = conectar_banco()
    sql = "UPDATE publicacao SET titulo=%s, autor=%s, editora=%s, data_publicacao=%s, isbn=%s, assunto=%s, tipo_publicacao=%s, palavras_chave=%s, quantidade=%s, localizacao=%s WHERE id_publicacao=%s"
    val = (titulo,autor,editora,data_publicacao,isbn,assunto,tipo_publicacao,palavras_chave,quantidade,localizacao,id)
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Dados atualizados")

# Apagar o bibliotecario
def apagar_publicacao(id):
    banco,cursor = conectar_banco()
    sql = "DELETE FROM publicacao WHERE id_publicacao=%s"
    val = [id]
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Publicação apagada")