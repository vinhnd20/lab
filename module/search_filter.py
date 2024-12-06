from module.db import create_connection
from module.property_manager import print_properties_table

# Tìm kiếm bất động sản theo các tiêu chí
def search_property_by_criteria(price_min=None, price_max=None, area_min=None, area_max=None, address=None, status=None):
    conn = create_connection()
    cursor = conn.cursor()

    query = 'SELECT * FROM properties WHERE 1=1'  

    params = []

    if price_min:
        query += ' AND price >= ?'
        params.append(price_min)
    if price_max:
        query += ' AND price <= ?'
        params.append(price_max)
    if area_min:
        query += ' AND area >= ?'
        params.append(area_min)
    if area_max:
        query += ' AND area <= ?'
        params.append(area_max)
    if address:
        query += ' AND address LIKE ?'
        params.append(f'%{address}%')  # Tìm kiếm địa chỉ chứa từ khoá
    if status:
        query += ' AND status = ?'
        params.append(status)

    cursor.execute(query, tuple(params))
    properties = cursor.fetchall()
    conn.close()

    return properties  

def filter_properties_by_status():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM properties WHERE status IN ("Dang ban", "Cho thue")')
    properties = cursor.fetchall()
    conn.close()

    return properties
