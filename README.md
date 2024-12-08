- Cài đặt môi trường: 

``` bash
python3.8 -m venv myenv
source myenv/bin/activate
```

- Cài đặt các thư viện cần thiết:

``` bash
pip install -r requirements.txt
```


- Cài đặt database: 


``` bash 
python3 module/db.py
python3 dump-data.py
```


- Giải thích: 

    - `python3 module/db.py`: Tạo database `mydb` và các bảng cần thiết và sử dụng sqlite.
    - `python3 dump-data.py`: Thêm dữ liệu mẫu vào database.
    - `python3 app.py`: Chạy ứng dụng.

- Các module: 
- `module/db.py`: Tạo database `mydb` và các bảng cần thiết.
- `module/customer_manager.py`: Quản lý khách hàng, bên trong có các hàm thêm, sửa, xóa khách hàng.
- `module/property_manager.py`: Quản lý bất động sản, bên trong có các hàm thêm, sửa, xóa bất động sản.
- `module/reports_stats.py`: Thống kê báo cáo, bên trong có các hàm thống kê báo cáo.


- Hàm validate dữ liệu: 

``` bash
# Kiểm tra dữ liệu nhập vào
class NumberValidator(Validator):
    def validate(self, document):
        try:
            float(document.text)
        except ValueError:
            raise ValidationError(message="Phai nhap mot gia tri so hop le", cursor_position=len(document.text))
```

- Chạy file thì gõ: 

``` bash
python main.py
````
