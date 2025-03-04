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

@email_service.route('/sendemail', methods=['POST'])
def send_email():
    today = datetime.today()
    interview_date = today + timedelta(days=3)
    formatted_date = interview_date.strftime("%B %d, %Y at 09:00 AM")
    name = request.form.get('name')
    email = request.form.get('email')
    position = request.form.get('position')
    action = request.form.get('action')

    print(email)

    if action == 'interview':
        subject = f"{name}, Ready for Your Interview at Minh Tao Solo Limited Company?"

        html_content = render_template('email_interview_jinja.html', name=name, position=position, date=formatted_date)
        msg = Message(subject, recipients=[email])
        msg.html = html_content
        mail.send(msg)
        print('Email đã gửi thành công!', 'success')
   
    return {}
