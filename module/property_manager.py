from module.db import create_connection
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator, ValidationError

# Kiểm tra dữ liệu nhập vào
class NumberValidator(Validator):
    def validate(self, document):
        try:
            float(document.text)
        except ValueError:
            raise ValidationError(message="Phai nhap mot gia tri so hop le", cursor_position=len(document.text))

def print_properties_table(properties):
    # Định nghĩa độ rộng của từng cột
    column_widths = {
        "ID": 6,  # ID
        "Ten": 30,  # Tên
        "Dia chi": 35,  # Địa chỉ
        "Gia": 15,  # Giá
        "Dien tich": 12,  # Diện tích
        "Mo ta": 30,  # Mô tả
        "Trang thai": 15  # Trạng thái
    }

    # Tính tổng chiều dài dòng --- bao gồm cả khoảng trắng và dấu |
    total_width = sum(column_widths.values()) + len(column_widths) * 3 - 5

    # In tiêu đề bảng
    if properties:
        print("-" * total_width)
        print(
            f"| {'ID':<{column_widths['ID']}}"
            f"| {'Ten':<{column_widths['Ten']}}"
            f"| {'Dia chi':<{column_widths['Dia chi']}}"
            f"| {'Gia':<{column_widths['Gia']}}"
            f"| {'Dien tich':<{column_widths['Dien tich']}}"
            f"| {'Mo ta':<{column_widths['Mo ta']}}"
            f"| {'Trang thai':<{column_widths['Trang thai']}} |"
        )
        print("-" * total_width)

        # In dữ liệu bảng
        for property in properties:
            # property[5] là Mô tả, nếu quá dài thì rút gọn
            description = property[5][:column_widths["Mo ta"] - 3] + '...' if len(property[5]) > column_widths["Mo ta"] else property[5]
            print(
                f"| {property[0]:<{column_widths['ID']}}"  # ID lấy trực tiếp từ cơ sở dữ liệu
                f"| {property[1]:<{column_widths['Ten']}}"
                f"| {property[2]:<{column_widths['Dia chi']}}"
                f"| {property[3]:<{column_widths['Gia']},.0f}"
                f"| {property[4]:<{column_widths['Dien tich']}}"
                f"| {description:<{column_widths['Mo ta']}}"
                f"| {property[6]:<{column_widths['Trang thai']}} |"
            )

        print("-" * total_width)
    else:
        print("Khong co bat dong san nao.")

# Hàm thêm bất động sản
def add_property():
    name = prompt("Nhap ten tai san: ")
    address = prompt("Nhap dia chi: ")
    price = prompt("Nhap gia ban: ", validator=NumberValidator())
    area = prompt("Nhap dien tich: ", validator=NumberValidator())
    description = prompt("Nhap mo ta: ")
    status = prompt("Chon trang thai (Dang ban, Cho thue, Da ban): ")

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO properties (name, address, price, area, description, status)
    VALUES (?, ?, ?, ?, ?, ?)''', (name, address, float(price), float(area), description, status))
    conn.commit()
    conn.close()
    print("Bat dong san da duoc them thanh cong!")

# Hàm liệt kê bất động sản
def list_properties():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM properties')
    properties = cursor.fetchall()
    conn.close()

    # Gọi hàm in bảng bất động sản
    print_properties_table(properties)

def edit_property():
    list_properties()  # Liet ke tat ca cac bat dong san
    try:
        id = int(prompt("Nhap ID bat dong san muon sua: "))
        
        # Hien thi cac lua chon
        print("Chon thong tin ban muon sua:")
        print("1. Ten")
        print("2. Dia chi")
        print("3. Gia")
        print("4. Dien tich")
        print("5. Mo ta")
        print("6. Trang thai")
        choice = int(prompt("Nhap so tuong ung (1-6): "))
        
        # Khoi tao cac bien moi
        new_name = None
        new_address = None
        new_price = None
        new_area = None
        new_description = None
        new_status = None

        # Xu ly tuy chon sua doi
        if choice == 1:
            new_name = prompt("Nhap ten moi: ")
        elif choice == 2:
            new_address = prompt("Nhap dia chi moi: ")
        elif choice == 3:
            new_price = prompt("Nhap gia moi: ", validator=NumberValidator())
        elif choice == 4:
            new_area = prompt("Nhap dien tich moi: ", validator=NumberValidator())
        elif choice == 5:
            new_description = prompt("Nhap mo ta moi: ")
        elif choice == 6:
            new_status = prompt("Nhap trang thai moi: ")

        # Cap nhat thong tin vao co so du lieu
        conn = create_connection()
        cursor = conn.cursor()
        
        # Duyet qua tung cot va cap nhat chi khi co thay doi
        query = "UPDATE properties SET "
        params = []

        if new_name:
            query += "name = ?, "
            params.append(new_name)
        if new_address:
            query += "address = ?, "
            params.append(new_address)
        if new_price:
            query += "price = ?, "
            params.append(float(new_price))
        if new_area:
            query += "area = ?, "
            params.append(float(new_area))
        if new_description:
            query += "description = ?, "
            params.append(new_description)
        if new_status:
            query += "status = ?, "
            params.append(new_status)

        # Loai bo dau phay thua o cuoi cau lenh
        query = query.rstrip(', ') 
        query += " WHERE id = ?"
        params.append(id)
        
        cursor.execute(query, tuple(params))
        conn.commit()
        conn.close()
        
        print("Cap nhat thanh cong!")
        
    except ValueError:
        print("ID khong hop le!")

# Hàm xóa bất động sản
def delete_property():
    list_properties()
    try:
        id = int(prompt("Nhap ID bat dong san muon xoa: "))

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM properties WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        print("Xoa thanh cong!")
    except ValueError:
        print("ID khong hop le!")
