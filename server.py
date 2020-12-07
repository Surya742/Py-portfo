from flask import Flask , render_template , request
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page>')
def home2(page):
    return render_template(page)

def write_msg_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["msg"]
        file = database.write(f'\nEmail: {email} , Subject: {subject} , message: {message}')

def write_msg_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["msg"]
        csv_writer = csv.writer(database2 , delimiter=',' , quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form' , methods=['POST' , 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_msg_csv(data)
            return render_template('thanku.html')
        except:
            return "Did not saved to database"
    else:
        return "Something went wrong!"


# @app.route('/<username>/<int:post_id>') 
# def diffrent(username=None , post_id=None):
#     return render_template('index.html', name=username , post_id=post_id)


# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# > $env:FLASK_APP = "server.py"  ------>>>>Powershell cmd
# > $env:FLASK_ENV = "development"
# > python -m flask run   

