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

        for idx, customer in enumerate(customers, 1):
            print(
                f"| {idx:<{column_widths['ID']}}"
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
    list_customers()
    try:
        id = int(prompt("Nhap ID khach hang muon sua: "))

        while True:
            try:
                new_name = validate_name(prompt("Nhap ten moi: "))
                break
            except ValueError as e:
                print(f"Loi: {e}. Vui long nhap lai.")

        while True:
            try:
                new_phone = validate_phone(prompt("Nhap so dien thoai moi: "))
                break
            except ValueError as e:
                print(f"Loi: {e}. Vui long nhap lai.")

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
        SET name = ?, phone = ?, email = ?
        WHERE id = ?''', (new_name, new_phone, new_email, id))
        conn.commit()
        conn.close()
        print("Cap nhat khach hang thanh cong!")
    except ValueError:
        print("ID khong hop le!")
    except Exception as e:
        print(f"Loi he thong: {e}")

# Xóa khách hàng
def delete_customer():
    list_customers()
    try:
        id = int(prompt("Nhap ID khach hang muon xoa: "))

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
