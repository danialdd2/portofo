from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/<string:page_name>")
def home(page_name):
    return render_template(page_name)


# @app.route("/about.html")
# def about():
#     return render_template("about.html")
def msg_saver(data):
    with open('payam.txt', mode='a', encoding='utf-8') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email},{subject},{message}')


def msg_saver2(data):
    with open('payam.csv', mode='a', encoding='utf-8') as database2:
        email = data['email']          
        subject = data['subject']
        message = data['message']
        file2 = csv.writer(database2, delimiter=',',
                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
        file2.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    print('form submitted')
    if request.method == 'POST':
        data = request.form.to_dict()
        msg_saver2(data)
        print(data)
        return redirect('/thanku.html')
    else:
        return 'something went wrong'


if __name__ == "__main__":
    print("Flask server starting...")
    app.run(debug=True, use_reloader=False)
