from flask import Flask, render_template, request, redirect
import csv
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/<string:page_name>")
def home(page_name):
    return render_template(page_name)


SENDER_EMAIL_ADDRESS = "xxosef6@gmail.com"
SENDER_EMAIL_PASSWORD = "uiwn ihdk qusx kroh"


# def msg_saver(data):
#     with open('payam.txt', mode='a', encoding='utf-8') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n {email},{subject},{message}')


# def msg_saver2(data):
#     with open('payam.csv', mode='a', encoding='utf-8') as database2:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file2 = csv.writer(database2, delimiter=',',
#                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
#         file2.writerow([email, subject, message])


# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     print('form submitted')
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         msg_saver2(data)
#         print(data)
#         return redirect('/thanku.html')
#     else:
#         return 'something went wrong'


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            name = data.get('name')
            email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')

            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL_ADDRESS
            msg['To'] = 'xxosef6@gmail.com'
            msg['Subject'] = f"New Contact Message: {subject}"

            body = f"""
            You received a new message from your portfolio contact form:

            Name: {name}
            Email: {email}
            Subject: {subject}
            Message:
            {message}
            """

            msg.attach(MIMEText(body, 'plain'))

            # ارسال ایمیل با SMTP Gmail
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD)
                server.send_message(msg)

            print("Email sent successfully!")
            return redirect('/thanku.html')

        except Exception as e:
            print(f"Error: {e}")
            return 'Something went wrong while sending the email 😢'

    else:
        return 'Something went wrong 😢'


if __name__ == "__main__":
    print("Flask server starting...")
    app.run(debug=True, use_reloader=False)
