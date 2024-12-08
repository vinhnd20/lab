from module.db import create_connection

## Thống kê số lượng bất động sản theo trạng thái
def count_properties_by_status():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT status, COUNT(*) FROM properties GROUP BY status')
    stats = cursor.fetchall()
    conn.close()

    if stats:
        for status, count in stats:
            print(f"Trạng thái: {status} - Số lượng: {count}")
    else:
        print("Không có tài sản nào.")

## Thống kê tổng giá trị bất động sản đang bán
def total_value_of_properties_for_sale():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(price) FROM properties WHERE status = "Dang ban"')
    total_value = cursor.fetchone()[0]
    conn.close()
    
    print(f"Tổng giá trị bất động sản đang bán: {total_value} VND")
