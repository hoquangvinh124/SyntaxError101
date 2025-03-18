from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_mail import Mail, Message
from datetime import datetime, timedelta

email_service = Blueprint('email_service', __name__)

mail = Mail()

def create_email_blueprint(app):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_DEFAULT_SENDER'] = 'congtytnhhminhtao@gmail.com'
    app.config['MAIL_USERNAME'] = 'congtytnhhminhtao@gmail.com'
    app.config['MAIL_PASSWORD'] = 'pjteppcfehjuhvle'

    mail.init_app(app)

@email_service.route('/sendemail/interview', methods=['POST'])
def send_interview_email():
    candidate_id = request.form.get('candidate_id')
    today = datetime.today()
    interview_date = today + timedelta(days=3)
    formatted_date = interview_date.strftime("%B %d, %Y at 09:00 AM")
    name = request.form.get('name')
    email = request.form.get('email')
    position = request.form.get('position')

    subject = f"{name}, Ready for Your Interview at Minh Tao Solo Limited Company?"

    html_content = render_template('email_interview_jinja.html', name=name, position=position, date=formatted_date)
    msg = Message(subject, recipients=[email])
    msg.html = html_content
    mail.send(msg)
    print('Email Sent!')

    return redirect(url_for('views.edit_candidate', candidate_id=candidate_id))


@email_service.route('/sendemail/hired', methods=['POST'])
def send_offer_email():
    candidate_id = request.form.get('candidate_id')
    name = request.form.get('name')
    email = request.form.get('email')
    position = request.form.get('position')

    start_date = datetime.today().strftime("%B %d, %Y")  # Ví dụ: "March 5, 2025"

    subject = f"🔥 {name}, You're Hired! Welcome to Minh Tao Solo Limited Company! 🎉"

    # Render template email
    html_content = render_template('email_hired_jinja.html', name=name, position=position, start_date=start_date)

    # Gửi email
    msg = Message(subject, recipients=[email])
    msg.html = html_content
    mail.send(msg)
    print('Offer Email Sent!')

    return redirect(url_for('views.edit_candidate', candidate_id=candidate_id))


@email_service.route('/sendemail/rejection', methods=['POST'])
def send_rejection_email():
    candidate_id = request.form.get('candidate_id')
    name = request.form.get('name')
    email = request.form.get('email')
    position = request.form.get('position')

    subject = f"Update on Your Application for {position}"

    # Render template email
    html_content = render_template('email_rejection_jinja.html', name=name, position=position)

    # Gửi email
    msg = Message(subject, recipients=[email])
    msg.html = html_content
    mail.send(msg)
    print('Rejection Email Sent!')

    return redirect(url_for('views.edit_candidate', candidate_id=candidate_id))



