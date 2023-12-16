
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__, template_folder='template') #using Flask class to instantiate app
print(__name__)

#a decorator saying when we use /, run hello_world function
@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>") #any html file with string name we pass will also be returned dynamically
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'something went wrong. Try again please!'

# @app.route("/components.html")
# def my_home2():
#     return render_template('components.html')

# @app.route("/favicon.ico")
# def blog2():
#     return "<p>These are my dogs</p>"

# @app.route("/blog1")
# def blog1():
#     return render_template('about.html')

# if __name__ == "__main__":
#      app.run(debug=True ,port=5000,use_reloader=False)
