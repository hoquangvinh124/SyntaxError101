import uuid  # Tạo ID duy nhất
import datetime  # Import để xử lý thời gian

class Candidate:
    def __init__(self,
                 name: str,  # Họ và tên ứng viên
                 dob: str,  # Ngày sinh (dùng datetime.date)
                 gender: str,  # Giới tính (Enum)
                 email: str,  # Email liên hệ
                 phone: str,  # Số điện thoại
                 identity_card: str,  # Số CMND/CCCD
                 work_experience: str,  # Kinh nghiệm làm việc (Enum)
                 education: str,  # Trình độ học vấn
                 description: str,  # Mô tả ứng viên
                 position: str,  # Vị trí ứng tuyển
                 cv_path: str,  # Đường dẫn file CV
                 avatar_path: str,  # Đường dẫn ảnh đại diện
                 status: str
                 ):
        
        self.candidate_id: str = str(uuid.uuid4())  
        self.name: str = name
        self.dob: str = dob
        self.gender: str = gender
        self.email: str = email
        self.phone: str = phone
        self.identity_card: str = identity_card
        self.work_experience: str = work_experience
        self.education: str = education
        self.description: str = description
        self.created_date: str = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.position: str = position
        self.cv_path: str = cv_path
        self.avatar_path: str = avatar_path
        self.status: str = status
