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

def read_product(conn):
    print('Danh Sách sản phẩm')

def update_product(conn):
    print('sửa thông tin sản phẩm')

def delete_product(conn):
    print('Xóa sản phẩm')