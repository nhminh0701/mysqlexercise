def handle_cat(choice, conn):
    if choice == 1:
        create_cat(conn)
    elif choice == 3:
        update_cat(conn)
    elif choice == 4:
        delete_cat(conn)
    read_cat(conn)

def create_cat(conn):
    print('them danh mục')
    sql = "INSERT INTO `tbl_category` (`cat_name`, `status`, `date_create`) VALUES (%s, %s, %s);"
    execute_sql(sql, conn, True, 'DELL', '0', '2020-10-01')

    

def read_cat(conn):
    print('danh sách danh mục')
    sql = "SELECT * FROM  `tbl_category`"
    cursor = execute_sql(sql, conn)
    print('Danh sach')
    for row in cursor:
        print(row)

def update_cat(conn):
    print('sửa danh muc')
    sql = "UPDATE `tbl_category` SET `status` = %s WHERE `tbl_category`.`cat_id` = %s;"
    execute_sql(sql, conn, True, 1, 7)


def delete_cat(conn):
    print('xóa danh mục')
    sql = "DELETE FROM `tbl_category` WHERE `tbl_category`.`cat_id` = %s;"
    execute_sql(sql, conn, True, 2)
    

def execute_sql(sql, conn, commitable=False, *args):
    cursor = conn.cursor()
    if commitable:
        cursor.execute(sql, args)
        conn.commit()
    else:
        cursor.execute(sql)
    return cursor
