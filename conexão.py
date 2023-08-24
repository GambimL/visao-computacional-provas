import mysql.connector
from mysql.connector import Error

def conectar(host, usuario, senha, banco):
    try:
        return mysql.connector.connect(host = host, user = usuario, password = senha, database = banco)
    except Error as erro:
        print("Falha na conexão")

def desconectar(con):
    return con.close()

def inserir_tabela(con, tabela, colunas, values, dados):
    try:
        cursor = con.cursor()
        sql = f"INSERT INTO {tabela} {colunas} values {values}"
        cursor.execute(sql, dados)
        cursor.close()
        con.commit()
    except Error as erro:
        print(f"Falha ao inserir dados na tabela devido ao erro: {erro}")
    finally:
        if con.is_connected():
            cursor.close()

def consultar_tabela(con, tabela, colunas, especificacao):
    try:
        dados = []
        cursor = con.cursor()
        sql = f"SELECT {colunas} FROM {tabela} WHERE {especificacao}"
        cursor.execute(sql)

        for dado in cursor:
            dados.append(dado) 
        return dados
    except Error as erro:
        print(f"Falha ao consultar na tabela devido ao erro {erro}")
    finally:
        if con.is_connected():
            cursor.close()

    
def atualiza_tabela(con, tabela, values, especificacao):
    try:
        cursor = con.cursor()
        sql = f'UPDATE {tabela} SET {values} WHERE {especificacao}'
        print(sql)
        cursor.execute(sql)
        con.commit()
        cursor.close()
    except Error as erro: 
        print(f"Falha em atualizar o dados da tabela devido ao erro: {erro}")
    finally:
        if con.is_connected():
            cursor.close()

    

