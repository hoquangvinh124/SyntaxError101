from .JsonFactory import JsonFileFactory # Import từ module bạn đã cung cấp

class JsonCRUD:
    def __init__(self, filename, ClassName):
        """
        Khởi tạo CRUD với file JSON.
        - Load dữ liệu từ file vào list (`self.data`) ngay khi khởi tạo.
        - Thao tác CRUD trên `self.data`, sau đó ghi lại file JSON nếu có thay đổi.
        """
        self.filename = filename
        self.ClassName = ClassName
        self.data = JsonFileFactory.read_data(self.filename, self.ClassName)  # Tự động load dữ liệu

    def save_data(self):
        """Ghi lại dữ liệu từ `self.data` vào file JSON nếu có thay đổi."""
        JsonFileFactory.write_data(self.data, self.filename)

    def create(self, obj):
        """Thêm một đối tượng mới vào danh sách và lưu file JSON."""
        self.data.append(obj)
        self.save_data()

    def read_all(self):
        """Lấy danh sách tất cả bản ghi từ list."""
        return self.data

    def read_by_id(self, object_id):
        """Tìm một bản ghi theo ID từ list."""
        for item in self.data:
            if getattr(item, "candidate_id", None) == object_id:
                return item
        return None

    def update(self, object_id, new_data):
        """Cập nhật bản ghi theo ID trong list và lưu file JSON."""
        updated = False
        for item in self.data:
            if getattr(item, "candidate_id", None) == object_id:
                for key, value in new_data.items():
                    if hasattr(item, key):
                        setattr(item, key, value)
                updated = True
                break
        if updated:
            self.save_data()
        return updated

    def delete(self, object_id):
        """Xóa một bản ghi theo ID trong list và lưu file JSON."""
        original_length = len(self.data)
        self.data = [item for item in self.data if getattr(item, "candidate_id", None) != object_id]
        if len(self.data) < original_length:
            self.save_data()
            return True
        return False
