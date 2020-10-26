from category import handle_cat
from product import handle_product
from mysqlconnector import get_connector

MAIN_MESSAGE = '''
------QUẢN LÝ------
 1 - them danh mục
 2 - danh sách danh mục
 3 - sửa danh muc
 4 - xóa danh mục
 
 5  - Thêm Sản phẩm
 6 - Danh Sách sản phẩm
 7 - sửa thông tin sản phẩm
 8 - Xóa sản phẩm
 Phim khac - ket thuc chuong trinh
 
 mời bạn chọn chức năng : '''

THANKYOU_MSG = 'Thank for using our program'


def main():
    conn = get_connector()

    running = True
    while running:
        user_input = input(MAIN_MESSAGE)
        try:
            user_main_choice = int(user_input)
            if user_main_choice in range(1, 5):
                handle_cat(user_main_choice, conn)
            elif user_main_choice in range(5, 9):
                handle_product(user_main_choice, conn)
            else:
                print(THANKYOU_MSG)
                running = False
        except ValueError:
            print(THANKYOU_MSG)
            running = False



main()