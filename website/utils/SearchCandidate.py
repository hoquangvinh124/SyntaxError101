import datetime
from .JsonFactory import JsonFileFactory
from .class_info.Candidate import Candidate

def search_candidates(filename, search_name=None, search_status=None):
    """
    Tìm kiếm ứng viên theo tên và kinh nghiệm, sau đó sắp xếp theo created_date mới nhất.
    
    :param filename: Đường dẫn file JSON chứa danh sách ứng viên.
    :param search_name: Chuỗi tìm kiếm theo tên (không phân biệt chữ hoa chữ thường).
    :param search_experience: Giá trị kinh nghiệm (ví dụ: "senior", "junior", "fresher").
    :return: Danh sách ứng viên sau khi lọc và sắp xếp.
    """
    # Đọc danh sách ứng viên từ file JSON sử dụng JSON factory
    candidates = JsonFileFactory.read_data(filename, Candidate)
    
    # Lọc theo tên nếu được cung cấp (tìm kiếm dưới dạng chứa chuỗi)
    if search_name:
        candidates = [c for c in candidates if search_name.lower() in c.name.lower()]
    
    # Lọc theo kinh nghiệm nếu được cung cấp
    if search_status:
        candidates = [c for c in candidates if search_status.lower() == c.status.lower()]
    
    # Sắp xếp danh sách theo created_date (mới nhất trước)
    # Chuyển đổi created_date từ chuỗi sang datetime theo định dạng "dd-mm-YYYY HH:MM:SS"
    candidates.sort(key=lambda c: datetime.datetime.strptime(c.created_date, "%d-%m-%Y %H:%M:%S"), reverse=True)
    
    return candidates
