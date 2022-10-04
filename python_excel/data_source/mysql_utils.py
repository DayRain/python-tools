import pymysql
from data_source import properties_loader

db_config = 'db.properties'


def get_connection(db_config):
    dic = properties_loader.load(db_config)
    host = dic['host']
    user = dic['user']
    password = dic['password']
    db = dic['db']
    charset = dic['charset']
    con = pymysql.connect(host=host, user=user, password=password, db=db,
                          charset=charset)
    return con


def query(sql):
    con = get_connection(db_config)
    cursor = con.cursor()
    cursor.execute(sql)

    result = cursor.fetchall()
    headers = []
    for info in cursor.description:
        headers.append(info[0])

    rows = []
    for row in result:
        rows.append(list(row))

    return {
        'headers': headers,
        'rows': rows
    }


def insert():
    pass
