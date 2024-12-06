from module.property_manager import add_property, list_properties, edit_property, delete_property
from module.customer_manager import add_customer, list_customers, edit_customer, delete_customer
from module.report_stats import count_properties_by_status, total_value_of_properties_for_sale
from prompt_toolkit import prompt
from module.property_manager import print_properties_table
from module.search_filter import search_property_by_criteria, filter_properties_by_status

def main_menu():
    while True:
        print("\n=== Menu Quan ly ===")
        print("1. Quan ly bat dong san")
        print("2. Quan ly khach hang")
        print("3. Tim kiem va loc tai san")
        print("4. Bao cao va thong ke")
        print("5. Thoat")
        
        choice = prompt("Nhap lua chon cua ban: ")

        if choice == '1':
            property_menu()
        elif choice == '2':
            customer_menu()
        elif choice == '3':
            search_menu()
        elif choice == '4':
            report_menu()
        elif choice == '5':
            break

def property_menu():
    while True:
        print("\n1. Them moi bat dong san")
        print("2. Sua thong tin bat dong san")
        print("3. Xoa bat dong san")
        print("4. Xem danh sach bat dong san")
        print("5. Quay lai")

        choice = prompt("Nhap lua chon cua ban: ")
        if choice == '1': add_property()
        elif choice == '2': edit_property()
        elif choice == '3': delete_property()
        elif choice == '4': list_properties()
        elif choice == '5': break

def customer_menu():
    while True:
        print("\n1. Them moi khach hang")
        print("2. Sua thong tin khach hang")
        print("3. Xoa khach hang")
        print("4. Xem danh sach khach hang")
        print("5. Quay lai")

        choice = prompt("Nhap lua chon cua ban: ")
        if choice == '1': add_customer()
        elif choice == '2': edit_customer()
        elif choice == '3': delete_customer()
        elif choice == '4': list_customers()
        elif choice == '5': break

def search_menu():
    while True:
        print("\n1. Tim kiem bat dong san")
        print("2. Loc tai san theo trang thai (Dang ban, Cho thue)")
        print("3. Quay lai")

        choice = prompt("Nhap lua chon cua ban: ")
        if choice == '1':
            print("\nTim kiem bat dong san theo cac tieu chi sau:")
            print("1. Gia ban (khoang gia)")
            print("2. Dien tich (khoang dien tich)")
            print("3. Dia chi (mot phan cua dia chi)")
            print("4. Trang thai (Dang ban, Cho thue, Da ban)")

            search_choice = prompt("Chon tieu chi tim kiem (1-4): ")

            if search_choice == '1':  # Tim kiem theo khoang gia
                price_min = float(prompt("Nhap gia toi thieu: "))
                price_max = float(prompt("Nhap gia toi da: "))
                properties = search_property_by_criteria(price_min=price_min, price_max=price_max)

            elif search_choice == '2':  # Tim kiem theo dien tich
                area_min = float(prompt("Nhap dien tich toi thieu: "))
                area_max = float(prompt("Nhap dien tich toi da: "))
                properties = search_property_by_criteria(area_min=area_min, area_max=area_max)

            elif search_choice == '3':  # Tim kiem theo dia chi
                address = prompt("Nhap mot phan cua dia chi: ")
                properties = search_property_by_criteria(address=address)

            elif search_choice == '4':  # Tim kiem theo trang thai
                status = prompt("Nhap trang thai (Dang ban, Cho thue, Da ban): ")
                properties = search_property_by_criteria(status=status)

            # Hien thi ket qua tim kiem
            if properties:
                print("\nKet qua tim kiem:")
                print_properties_table(properties)
            else:
                print("Khong co bat dong san nao thoa man tieu chi tim kiem.")

        elif choice == '2':  # Loc tai san theo trang thai "Dang ban" hoac "Cho thue"
            print("\nLoc tai san theo trang thai (Dang ban, Cho thue):")
            properties = filter_properties_by_status()  # Loc tat ca bat dong san co trang thai "Dang ban" hoac "Cho thue"
            if properties:
                print("\nKet qua loc tai san theo trang thai:")
                print_properties_table(properties)
            else:
                print("Khong co bat dong san nao voi trang thai nay.")

        elif choice == '3':  # Quay lai menu chinh
            break



def report_menu():
    while True:
        print("\n1. Thong ke so luong bat dong san theo trang thai")
        print("2. Tong gia tri bat dong san dang ban")
        print("3. Quay lai")

        choice = prompt("Nhap lua chon cua ban: ")
        if choice == '1':
            count_properties_by_status()
        elif choice == '2':
            total_value_of_properties_for_sale()
        elif choice == '3': break

if __name__ == '__main__':
    main_menu()
