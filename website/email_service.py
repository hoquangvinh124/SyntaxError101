from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_mail import Mail, Message

email_service = Blueprint('email_service', __name__)

mail = Mail()

def create_email_blueprint(app):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'congtytnhhminhtao@gmail.com'
    app.config['MAIL_PASSWORD'] = 'pjteppcfehjuhvle'

    mail.init_app(app)

@email_service.route('/send_email', methods=['POST'])
def send_email():
    recipient = request.form['email']
    subject = "Lời mời phỏng vấn"

    html_content = render_template('email_template.html', name="Ứng viên")
    msg = Message(subject, recipients=[recipient])
    msg.html = html_content

    try:
        mail.send(msg)
        flash('Email đã gửi thành công!', 'success')
    except Exception as e:
        flash(f'Gửi email thất bại: {str(e)}', 'danger')

    return redirect(url_for('email_bp.index'))
