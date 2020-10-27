from category import read_cat, is_table_empty, is_cat_with_id_existed
from datetime import datetime

def handle_product(choice, conn):
    if choice == 5:
        create_product(conn)
    elif choice == 6:
        read_product(conn)
    elif choice == 7:
        update_product(conn)
    else:
        delete_product(conn)

def create_product(conn):
    print('Thêm Sản phẩm')
    user_input_data = get_user_create_product_input(conn)
    user_input_data['date_create'] = datetime.utcnow()

    sql_keys = ', '.join(user_input_data.keys())
    sql_values = ', '.join([f"'{value}'" if type(value) not in (int, float) else str(value) for value in user_input_data.values()])
    sql = f"INSERT INTO tbl_product ({sql_keys}) VALUES ({sql_values});"
    print(sql)

    execute_sql(sql, conn, commit=True)



def read_product(conn):
    print('Danh Sách sản phẩm')
    sql = "SELECT * from tbl_product"
    cursor = execute_sql(sql, conn)
    print_table(cursor._rows)


def update_product(conn):
    print('sửa thông tin sản phẩm')

def delete_product(conn):
    print('Xóa sản phẩm')


def execute_sql(sql, conn, commit=False, *args):
    cursor = conn.cursor()
    if commit:
        cursor.execute(sql, args)
        conn.commit()
    else:
        cursor.execute(sql)
    return cursor

def print_table(data):
    print('-----TABLE-----')
    print()
    print('pro_id       cat_id      pro_name        price       status      date_create')
    for row in data:
        print('     '.join([item if type(item)==str else str(item) for item in row.values()]))


def get_user_create_product_input(conn):
    input_data = {}
    cat_id = get_cat_id_input(conn)
    if cat_id:
        input_data['cat_id'] = cat_id
    input_data['pro_name'] = input("Enter product name: ")
    input_data['price'] = get_product_price_input()
    input_data['status'] = get_product_status_input()
    return input_data
    


def get_cat_id_input(conn):
    if is_table_empty(conn):
        return

    while True:
        read_cat(conn)
        cat_id_input = input("Enter id of one of above category, or enter to skip: ")
        try:
            cat_id = int(cat_id_input)
            if is_cat_with_id_existed(conn, cat_id_input):
                return cat_id
            else:
                print("No category with such id existed")
        except:
            print("Invalid input, it was supposed to be an integer")


def get_product_price_input():
    price_input = input("Enter a number to set price, invalid values will set the price to 0: ")
    try: 
        price = float(price_input)
        return price
    except ValueError:
        return 0


def get_product_status_input():
    status_input = input("Enter status, 1 for available, other for unavailable: ")
    try:
        status = int(status_input)
        if status == 1:
            return status
        else:
            return 0
    except ValueError:
        return 0