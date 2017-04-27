import psycopg2 as pg


def get_connection():
    conn = pg.connect(
        database='xpixttod',
        user='xpixttod',
        password='sLIj1Y6P0N5CMeYJyQkRVCkhGPiGJnkm',
        host='hard-plum.db.elephantsql.com',
        port=5432)
    return conn


def insert_catagories(EMAIL, PHONE, MESSAGE):
    connection = get_connection()
    cursor = connection.cursor()
    print "cur is created"
    query = """INSERT INTO CONTACTS(EMAIL,PHONE,MESSAGES) VALUES('%s',
    %s, '%s');"""
    query = query % (
        EMAIL, PHONE, MESSAGE)
    print query
    cursor.execute(query)
    connection.commit()
    print "Records created successfully"
    connection.close()
