import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def load_html_template(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        exit(1)
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def send_email_smtp(sender_email, sender_password, receiver_email, subject, html_content):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the HTML content
    msg.attach(MIMEText(html_content, 'html'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    email_file = input("Enter the path to your HTML email file (default: email.html): ").strip()
    if email_file == "":
        email_file = "email.html"

    sender_email = input("Sender email address: ").strip()
    receiver_email = input("Receiver email address: ").strip()
    subject = input("Email subject: ").strip()
    sender_password = input("Sender email password or app password: ").strip()

    html_content = load_html_template(email_file)

    send_email_smtp(sender_email, sender_password, receiver_email, subject, html_content)
