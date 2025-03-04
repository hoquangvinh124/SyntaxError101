import json
import os
import datetime
import uuid
from enum import Enum

class JsonFileFactory:
    @staticmethod
    def write_data(arr_data, filename):
        """
        Chuyển danh sách đối tượng thành JSON và lưu vào file.
        :param arr_data: Danh sách đối tượng bất kỳ
        :param filename: Đường dẫn file JSON
        """
        json_string = json.dumps(
            [JsonFileFactory.serialize(item) for item in arr_data], 
            indent=4, 
            ensure_ascii=False
        )
        with open(filename, 'w', encoding='utf-8') as json_file:
            json_file.write(json_string)

    @staticmethod
    def read_data(filename, ClassName):
        """
        Đọc dữ liệu từ file JSON và chuyển thành danh sách đối tượng ClassName.
        :param filename: Đường dẫn file JSON
        :param ClassName: Class cần khôi phục
        :return: Danh sách đối tượng ClassName
        """
        if not os.path.isfile(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [JsonFileFactory.deserialize(cls, ClassName) for cls in data]

    @staticmethod
    def serialize(obj):
        """
        Chuyển đổi object sang dictionary để lưu JSON.
        """
        if isinstance(obj, datetime.date):
            return obj.strftime("%d-%m-%Y")  # Chuyển datetime thành string
        elif isinstance(obj, Enum):
            return obj.value  # Chuyển Enum thành string
        elif isinstance(obj, uuid.UUID):
            return str(obj)  # Chuyển UUID thành string
        elif isinstance(obj, list):  # Nếu obj là list, xử lý từng phần tử
            return [JsonFileFactory.serialize(item) for item in obj]
        elif isinstance(obj, dict):  # Nếu obj là dict, xử lý từng cặp key-value
            return {key: JsonFileFactory.serialize(value) for key, value in obj.items()}
        elif hasattr(obj, "__dict__"):  # Chỉ serialize object có __dict__
            return {key: JsonFileFactory.serialize(value) for key, value in obj.__dict__.items()}
        else:
            return obj  # Trả về nguyên giá trị nếu không phải đối tượng có __dict__

    @staticmethod
    def deserialize(data, ClassName):
        """
        Chuyển đổi dictionary JSON thành đối tượng ClassName.
        """
        obj = ClassName.__new__(ClassName)  # Tạo instance rỗng của ClassName
        for key, value in data.items():
            attr_type = getattr(ClassName, key, None)
            if isinstance(attr_type, Enum):  # Xử lý Enum
                setattr(obj, key, attr_type.__class__(value))
            elif isinstance(attr_type, datetime.date):  # Xử lý datetime
                setattr(obj, key, datetime.datetime.strptime(value, "%d-%m-%Y").date())
            elif isinstance(attr_type, uuid.UUID):  # Xử lý UUID
                setattr(obj, key, uuid.UUID(value))
            else:  # Gán giá trị thông thường
                setattr(obj, key, value)
        return obj
