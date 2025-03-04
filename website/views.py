from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from .utils.JsonCRUD import JsonCRUD
from .utils.class_info.Candidate import Candidate
from datetime import datetime
from .utils.SearchCandidate import search_candidates


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('login.html')


@views.route('/tables')
def tables():
    # Lấy các tham số tìm kiếm từ query string
    search_name = request.args.get('namesearch')
    search_experience = request.args.get('experiencefilter')
    search_date_created = request.args.get('recencyfilter')

    # Gọi hàm search_candidates
    candidates = search_candidates('website/data/candidates/candidates.json', search_name, search_experience)
    
    return render_template('tables_jinja.html', candidates=candidates)

@views.route('/api/candidates', methods=['POST'])
def create_candidate():
    """
    Nhận dữ liệu form (bao gồm file upload) từ client:
    - Các trường text: name, dob, gender, email, phone, identityCard, workExperience, education, position, status, description
    - Các trường file: avatarPath, cvPath
    """
    # Lấy dữ liệu dạng text
    name = request.form.get('name')
    dob = request.form.get('dob')
    gender = request.form.get('gender')
    email = request.form.get('email')
    phone = request.form.get('phone')
    identity_card = request.form.get('identityCard')
    work_experience = request.form.get('workExperience')
    education = request.form.get('education')
    position = request.form.get('position')
    status = request.form.get('status')
    description = request.form.get('description')

    # Lấy file từ form
    avatar_file = request.files.get('avatarPath')  # input name="avatarPath"
    cv_file = request.files.get('cvPath')          # input name="cvPath"

    # Xác định thư mục lưu file, sử dụng current_app.root_path để lấy đường dẫn gốc của ứng dụng
    avatar_dir = os.path.join(current_app.root_path, 'static', 'avt-images')
    cv_dir = os.path.join(current_app.root_path, 'static', 'cv')


    avatar_path = None
    if avatar_file:
        avatar_filename = secure_filename(avatar_file.filename)
        avatar_file.save(os.path.join(avatar_dir, avatar_filename))
        avatar_path = f'/static/avt-images/{avatar_filename}'

    cv_path = None
    if cv_file:
        cv_filename = secure_filename(cv_file.filename)
        cv_file.save(os.path.join(cv_dir, cv_filename))
        cv_path = f'/static/cv/{cv_filename}'

    
    new_candidate = Candidate(name=name, gender=gender, dob=dob, email=email, phone=phone, identity_card=identity_card, 
                              work_experience=work_experience, education=education, description=description, 
                              position=position, cv_path=cv_path, avatar_path=avatar_path, status=status)
    

    add_candidate = JsonCRUD('website/data/candidates/candidates.json', Candidate).create(new_candidate)
    
    return redirect(url_for('views.tables'))

@views.route('edit/<candidate_id>', methods=['GET', 'POST'])
def edit_candidate(candidate_id):
    """
    - GET: Trả về thông tin ứng viên theo ID
    - POST: Cập nhật thông tin ứng viên theo ID
    """
    if request.method == 'GET':
        candidate = JsonCRUD('website/data/candidates/candidates.json', Candidate).read_by_id(candidate_id)
        return render_template('edit_profile_jinja.html', candidate=candidate)
    if request.method == 'POST':
        # Thực hiện xóa ứng viên bằng JsonCRUD
        JsonCRUD('website/data/candidates/candidates.json', Candidate).delete(candidate_id)
            
        return redirect(url_for('views.tables'))
        
    
@views.route('/api/candidates/<candidate_id>', methods=['POST'])
def update_candidate(candidate_id):
    name = request.form.get('name')
    dob = request.form.get('dob')
    gender = request.form.get('gender').lower()
    email = request.form.get('email')
    phone = request.form.get('phone')
    identity_card = request.form.get('identityCard')
    work_experience = request.form.get('workExperience').lower()
    education = request.form.get('education')
    position = request.form.get('position')
    status = request.form.get('status').lower()
    description = request.form.get('description')

    # Lấy file từ form
    avatar_file = request.files.get('profile-pic-upload')  # input name="avatarPath"
    cv_file = request.files.get('cv-file-upload')          # input name="cvPath"

    # Xác định thư mục lưu file, sử dụng current_app.root_path để lấy đường dẫn gốc của ứng dụng
    avatar_dir = os.path.join(current_app.root_path, 'static', 'avt-images')
    cv_dir = os.path.join(current_app.root_path, 'static', 'cv')


    avatar_path = None
    if avatar_file:
        avatar_filename = secure_filename(avatar_file.filename)
        avatar_file.save(os.path.join(avatar_dir, avatar_filename))
        # Đường dẫn trả về dạng URL (đầu /static)
        avatar_path = f'/static/avt-images/{avatar_filename}'

    cv_path = None
    if cv_file:
        cv_filename = secure_filename(cv_file.filename)
        cv_file.save(os.path.join(cv_dir, cv_filename))
        cv_path = f'/static/cv/{cv_filename}'
        

    new_data = {
    "name": name,
    "dob": dob,
    "gender": gender,
    "email": email,
    "phone": phone,
    "identity_card": identity_card,
    "work_experience": work_experience,
    "education": education,
    "position": position,
    "status": status,
    "description": description
}

# Nếu có upload file, cập nhật đường dẫn tương ứng
    if avatar_path:
        new_data["avatar_path"] = avatar_path
    if cv_path:
        new_data["cv_path"] = cv_path


    candidate = JsonCRUD('website/data/candidates/candidates.json', Candidate).update(object_id=candidate_id, new_data=new_data)

    return redirect(url_for('views.tables'))

@views.route('/deleteCandidate', methods=['POST'])
def delete_candidate():
    candidate_id = request.form.get('candidate_id')
    
    JsonCRUD('website/data/candidates/candidates.json', Candidate).delete(candidate_id)
        
    return redirect(url_for('views.tables'))





