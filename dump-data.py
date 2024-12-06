import sqlite3

def create_connection():
    conn = sqlite3.connect('property_management.db')
    return conn

def dump_property_data():
    properties = [
        ("Can ho cao cap", "123 Duong ABC, Quan 1, TP.HCM", 2000000000, 75, "Can ho 2 phong ngu, 2 toilet, hien dai, ban cong rong", "Dang ban"),
        ("Nha pho", "456 Duong XYZ, Quan 3, TP.HCM", 3000000000, 120, "Nha pho 3 tang, 4 phong ngu, 3 toilet, co san vuon", "Cho thue"),
        ("Cao oc van phong", "789 Duong DEF, Quan 4, TP.HCM", 10000000000, 500, "Toa cao oc 20 tang, van phong hien dai, co thang may", "Dang ban"),
        ("Mua dat nen", "321 Duong GHI, Quan 5, TP.HCM", 5000000000, 300, "Dat nen 300m2, gan khu du an", "Da ban"),
        ("Can ho studio", "654 Duong JKL, Quan 7, TP.HCM", 1200000000, 40, "Can ho studio, 1 phong ngu, phong tam", "Dang ban"),
        ("Nha bien", "987 Duong MNO, TP.Vung Tau", 8000000000, 250, "Nha bien 2 tang, 5 phong ngu, ho boi", "Cho thue"),
        ("Phong tro", "111 Duong PQR, Quan 2, TP.HCM", 30000000, 20, "Phong tro don gian, dien tich nho", "Cho thue"),
        ("Nha dat", "222 Duong STU, Quan 10, TP.HCM", 1500000000, 60, "Nha 2 phong ngu, 1 toilet, san vuon", "Dang ban"),
        ("Can ho cao cap", "333 Duong VWX, Quan 9, TP.HCM", 4000000000, 90, "Can ho cao cap, 3 phong ngu, 2 toilet, noi that hien dai", "Da ban"),
        ("Cao oc chung cu", "555 Duong YZA, Quan 6, TP.HCM", 2500000000, 85, "Chung cu 3 phong ngu, 2 toilet, co ho boi, gym", "Dang ban")
    ]

    conn = create_connection()
    cursor = conn.cursor()
    
    for property in properties:
        cursor.execute('''
        INSERT INTO properties (name, address, price, area, description, status)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', property)
    
    conn.commit()
    conn.close()
    print("Dữ liệu bất động sản đã được thêm vào thành công!")

def dump_customer_data():
    customers = [
        ("Nguyen Van A", "0123456789", "nguyenvana@gmail.com", "1,2,3"),
        ("Le Thi B", "0987654321", "lethib@gmail.com", "4,5"),
        ("Tran Minh C", "0123987456", "tranminhc@gmail.com", "2,3,4"),
        ("Pham Thi D", "0967321987", "phamthid@gmail.com", "1,6"),
        ("Nguyen Thi E", "0932145678", "nguyenthie@gmail.com", "5,7"),
        ("Hoang Mai F", "0912345678", "hoangmaif@gmail.com", "8,9"),
        ("Vu Anh G", "0908123456", "vuanhg@gmail.com", "3,4,6"),
        ("Bui Thi H", "0945678901", "buithih@gmail.com", "1,2,7"),
        ("Do Minh I", "0965432109", "dominhi@gmail.com", "5,6"),
        ("Nguyen Thi J", "0934567890", "nguyenthij@gmail.com", "4,8")
    ]

    conn = create_connection()
    cursor = conn.cursor()
    
    for customer in customers:
        cursor.execute('''
        INSERT INTO customers (name, phone, email, interested_properties)
        VALUES (?, ?, ?, ?)
        ''', customer)
    
    conn.commit()
    conn.close()
    print("Dữ liệu khách hàng đã được thêm vào thành công!")

if __name__ == '__main__':
    dump_property_data()
    dump_customer_data()
