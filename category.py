from datetime import datetime

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
    user_inputs = get_user_create_cat_input()
    cat_name, status = user_inputs.values()
    date_create = datetime.utcnow()
    sql = "INSERT INTO tbl_category (cat_name, status, date_create) VALUES (%s, %s, %s);"
    execute_sql(sql, conn, True, cat_name, status, date_create)


def get_user_create_cat_input():
    user_inputs = {}
    user_inputs['cat_name'] = input('Enter category name: ')
    status_input = input('Enter status, 1 for avaialble, other for unavailable: ')
    try:
        status = int(status_input)
        if status == 1:
            user_inputs['status'] = 1
        else:
            user_inputs['status'] = 0
    except ValueError:
        user_inputs['status'] = 0
    
    return user_inputs
        
    

def read_cat(conn):
    print('danh sách danh mục')
    sql = "SELECT * FROM  tbl_category"
    cursor = execute_sql(sql, conn)
    print('Danh sach')
    print_table(cursor._rows)



def update_cat(conn):
    print('sửa danh muc')
    if is_table_empty(conn):
        print("Table empty")
        return

    cat_id = get_cat_id(conn)
    user_cat_input = get_user_update_cat_input()
    sql_edit_fields = ', '.join([ f"{key} = '{value}'" if type(value) == str else f"{key} = {value}" for key, value in user_cat_input.items()])
    print(sql_edit_fields)

    sql = f"UPDATE tbl_category SET {sql_edit_fields} WHERE tbl_category.`cat_id` = {cat_id};"
    execute_sql(sql, conn, True)


def get_user_update_cat_input():
    user_inputs = {}
    user_cat_name_input = input('Enter category name, enter for skipping: ')
    if user_cat_name_input:
        user_inputs['cat_name'] = user_cat_name_input
    status_input = input('Enter status, 1 for avaialble, enter for skipping, other for unavailable: ')
    try:
        status = int(status_input)
        if status == 1:
            user_inputs['status'] = 1
        else:
            user_inputs['status'] = 0
    except ValueError:
        if status_input:
            user_inputs['status'] = 0
    
    return user_inputs



def delete_cat(conn):
    print('xóa danh mục')
    if is_table_empty(conn):
        print("Table empty")
        return

    cat_id = get_cat_id(conn)
    sql = f"DELETE FROM `tbl_category` WHERE `tbl_category`.`cat_id` = {cat_id};"
    execute_sql(sql, conn, True)
    

def execute_sql(sql, conn, commitable=False, *args):
    cursor = conn.cursor()
    if commitable:
        cursor.execute(sql, args)
        conn.commit()
    else:
        cursor.execute(sql)
    return cursor


def is_table_empty(conn):
    sql = "SELECT * FROM tbl_category"
    cursor = execute_sql(sql, conn)
    return cursor.rowcount == 0


def get_cat_id(conn):
    while True:
        cat_id = get_cat_id_input()
        if is_cat_with_id_existed(conn, cat_id):
            return cat_id
        else:
            print("No item with such id existed!")

def is_cat_with_id_existed(conn, cat_id):
    query_sql = f"SELECT * FROM tbl_category WHERE cat_id = {cat_id}"
    cursor = execute_sql(query_sql, conn)
    print_table(cursor._rows)
    return cursor.rowcount != 0

def get_cat_id_input():
    while True:
        try:
            cat_id = int(input("Enter category id: "))
            return cat_id
        except ValueError:
            print("Not a valid input, please try again, cat_id is an integer")


def print_table(data):
    print('-----TABLE-----')
    print()
    print('cat_id   cat_name    status      date_create')
    for item in data:
        print('     '.join([str(value) for value in item.values()]))