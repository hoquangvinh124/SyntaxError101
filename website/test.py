import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "congtytnhhminhtao@gmail.com"
EMAIL_PASSWORD = "pjteppcfehjuhvle"

TO_EMAIL = "huynhquoclong.2005@gmail.com"  # Email nhận thử
SUBJECT = "Thư mời nhận việc - Vị trí Quản lý Đường Dây Quận Cam"
BODY = """Kính gửi Anh Huỳnh Quốc Long,

Công ty TNHH Một Mình Tao xin gửi lời cảm ơn đến Anh vì đã tham gia quá trình tuyển dụng của chúng tôi. 
Sau khi xem xét kỹ lưỡng, chúng tôi vui mừng thông báo rằng Anh đã trúng tuyển vào vị trí **Vị trí Quản lý Đường Dây Quận Cam** tại công ty.

Thông tin công việc:
- Vị trí: Vị trí Quản lý Đường Dây Quận Cam
- Thời gian bắt đầu làm việc: 3/3/2025
- Địa điểm làm việc: Campuchia - Khu tự trị Tam Thái Tử - Pnompenh
- Thời gian làm việc: 2 giờ sáng - 1 giờ đêm hôm sau
- Lương và các chế độ: Không lương và quyền lợi được chích điện 2 lần mỗi ngày


Trân trọng,
Hr Manager CTY TNHH Một Mình Tao
"""
try:
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = SUBJECT
    msg.attach(MIMEText(BODY, 'plain'))
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
    server.quit()
    print("Email đã được gửi thành công!")
except Exception as e:
    print(f"Gửi email thất bại: {str(e)}")
