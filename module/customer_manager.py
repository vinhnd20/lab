from module.db import create_connection
from prompt_toolkit import prompt
import re  
from module.property_manager import list_properties

# Hàm kiểm tra tên khách hàng
def validate_name(name):
    if not re.match(r"^[a-zA-Z\s]+$", name):
        raise ValueError("Ten khach hang chi duoc chua ky tu chu va khoang trang.")
    return name

# Hàm kiểm tra số điện thoại
def validate_phone(phone):
    if not re.match(r"^\d{10,15}$", phone):  
        raise ValueError("So dien thoai chi duoc chua so va co do dai tu 10 den 15 ky tu.")
    return phone

# Hàm kiểm tra email
def validate_email(email):
    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):  
        raise ValueError("Email khong hop le. Phai co dau @")
    return email

# Thêm khách hàng mới
def add_customer():
    try:
        while True:
            try:
                name = validate_name(prompt("Nhap ten khach hang: "))
                break
            except ValueError as e:
                print(f"Loi: {e}. Vui long nhap lai.")

        while True:
            try:
                phone = validate_phone(prompt("Nhap so dien thoai: "))
                break
            except ValueError as e:
                print(f"Loi: {e}. Vui long nhap lai.")

        while True:
            try:
                email = validate_email(prompt("Nhap email: "))
                break
            except ValueError as e:
                print(f"Loi: {e}. Vui long nhap lai.")

        print("\nDanh sach bat dong san:")
        list_properties()
        interested_properties = prompt("Nhap danh sach bat dong san quan tam (vd: 1, 2, 3): ")

        interested_properties_list = interested_properties.split(',')
        interested_properties_list = [id.strip() for id in interested_properties_list]

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO customers (name, phone, email, interested_properties)
        VALUES (?, ?, ?, ?)''', (name, phone, email, ','.join(interested_properties_list)))
        conn.commit()
        conn.close()
        print("Khach hang da duoc them thanh cong!")
    except Exception as e:
        print(f"Loi he thong: {e}")

# Liệt kê danh sách khách hàng
def list_customers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    conn.close()

    if customers:
        print("Danh sach khach hang:")
        column_widths = {
            "ID": 6,
            "Ten": 30,
            "So dien thoai": 20,
            "Email": 35,
            "Quan tam": 20
        }

        total_width = sum(column_widths.values()) + len(column_widths) * 3 - 3

        print("-" * total_width)
        print(
            f"| {'ID':<{column_widths['ID']}}"
            f"| {'Ten':<{column_widths['Ten']}}"
            f"| {'So dien thoai':<{column_widths['So dien thoai']}}"
            f"| {'Email':<{column_widths['Email']}}"
            f"| {'Quan tam':<{column_widths['Quan tam']}} |"
        )
        print("-" * total_width)

        for customer in customers:
            print(
                f"| {customer[0]:<{column_widths['ID']}}"
                f"| {customer[1]:<{column_widths['Ten']}}"
                f"| {customer[2]:<{column_widths['So dien thoai']}}"
                f"| {customer[3]:<{column_widths['Email']}}"
                f"| {customer[4]:<{column_widths['Quan tam']}} |"
            )

        print("-" * total_width)
    else:
        print("Khong co khach hang nao.")

# Sửa thông tin khách hàng
def edit_customer():
    list_customers()  # Liệt kê khách hàng trước
    try:
        id = int(prompt("Nhap ID khach hang muon sua: "))  # Nhập ID khách hàng cần sửa

        # Kiểm tra nếu ID hợp lệ trong cơ sở dữ liệu
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customers WHERE id = ?', (id,))
        customer = cursor.fetchone()
        conn.close()

        if not customer:
            print("ID khach hang khong ton tai.")
            return

        print("\nChon thong tin muon sua:")
        print("1. Doi ten")
        print("2. Doi so dien thoai")
        print("3. Doi email")
        print("4. Doi danh sach bat dong san quan tam")

        choice = int(prompt("Nhap lua chon (1-4): "))

        if choice == 1:  # Đổi tên
            while True:
                try:
                    new_name = validate_name(prompt("Nhap ten moi: "))
                    break
                except ValueError as e:
                    print(f"Loi: {e}. Vui long nhap lai.")
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
            UPDATE customers
            SET name = ?
            WHERE id = ?''', (new_name, id))
            conn.commit()
            conn.close()
            print("Doi ten thanh cong!")

        elif choice == 2:  # Đổi số điện thoại
            while True:
                try:
                    new_phone = validate_phone(prompt("Nhap so dien thoai moi: "))
                    break
                except ValueError as e:
                    print(f"Loi: {e}. Vui long nhap lai.")
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
            UPDATE customers
            SET phone = ?
            WHERE id = ?''', (new_phone, id))
            conn.commit()
            conn.close()
            print("Doi so dien thoai thanh cong!")

        elif choice == 3:  # Đổi email
            while True:
                try:
                    new_email = validate_email(prompt("Nhap email moi: "))
                    break
                except ValueError as e:
                    print(f"Loi: {e}. Vui long nhap lai.")
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
            UPDATE customers
            SET email = ?
            WHERE id = ?''', (new_email, id))
            conn.commit()
            conn.close()
            print("Doi email thanh cong!")

        elif choice == 4:  # Đổi danh sách bất động sản quan tâm
            print("\nDanh sach bat dong san:")
            list_properties()  # Liệt kê các bất động sản
            interested_properties = prompt("Nhap danh sach bat dong san quan tam (vd: 1, 2, 3): ")

            interested_properties_list = interested_properties.split(',')
            interested_properties_list = [id.strip() for id in interested_properties_list]

            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
            UPDATE customers
            SET interested_properties = ?
            WHERE id = ?''', (','.join(interested_properties_list), id))
            conn.commit()
            conn.close()
            print("Doi danh sach bat dong san quan tam thanh cong!")

        else:
            print("Lua chon khong hop le.")

    except ValueError:
        print("ID khong hop le!")
    except Exception as e:
        print(f"Loi he thong: {e}")


# Xóa khách hàng
def delete_customer():
    list_customers()  # Liệt kê khách hàng trước
    try:
        id = int(prompt("Nhap ID khach hang muon xoa: "))  # Nhập ID khách hàng cần xóa

        # Kiểm tra nếu ID hợp lệ trong cơ sở dữ liệu
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customers WHERE id = ?', (id,))
        customer = cursor.fetchone()
        conn.close()

        if not customer:
            print("ID khach hang khong ton tai.")
            return

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM customers WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        print("Xoa khach hang thanh cong!")
    except ValueError:
        print("ID khong hop le!")
    except Exception as e:
        print(f"Loi he thong: {e}")
