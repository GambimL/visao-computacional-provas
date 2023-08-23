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

def consultar_tabela(con, tabela, colunas, especificacao):
    dados = []
    cursor = con.cursor()
    sql = f"SELECT {colunas} FROM {tabela} WHERE {especificacao}"
    cursor.execute(sql)

    for dado in cursor:
        dados.append(dado)
    cursor.close()  
    return dados
    
def atualiza_tabela(con, tabela, values, especificacao):
    cursor = con.cursor()
    sql = f'UPDATE {tabela} SET {values} WHERE {especificacao}'
    print(sql)
    cursor.execute(sql)
    cursor.close()

    

