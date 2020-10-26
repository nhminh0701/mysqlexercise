import pymysql

def get_connector():
    connector = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='thithu',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    print('Kết nối thành công')

    return connector