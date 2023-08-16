import mysql.connector

def conectar(host, usuario, senha, banco):
    return mysql.connector.connect(host = host, user = usuario, password = senha, database = banco)

def desconectar(con):
    return con.close()

def inserir_tabela(con, tabela, colunas, values, dados):
    cursor = con.cursor()
    sql = f"INSERT INTO {tabela} {colunas} values {values}"
    cursor.execute(sql, dados)
    cursor.close()
    con.commit()

