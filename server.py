from flask import Flask , render_template ,request , redirect
import os 
import csv


app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('./index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)




def write_to_txt(full_data):

    with open('database.txt' , mode = 'a' , newline='') as database : 
    
        email = full_data['email']
        subject= full_data['subject']
        message= full_data['message']
        file = database.write(f'\n{email} , {subject} , {message}') # if indentation goes back , file will be closed and can not do anything like appending


def write_to_csv(full_data):
    with open('database.csv' , mode='a' , newline='') as database2 :
        email = full_data['email']
        subject= full_data['subject']
        message= full_data['message']
        csv_writer =csv.writer(database2 , delimiter = ',' , quotechar= '|' , quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email , subject , message])

                           
 

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form ():
    if request.method == 'POST':
        data0 = request.form['subject']
        full_data = request.form.to_dict()
        write_to_csv(full_data)
        return render_template('./thankyou.html' , name = data0)

    else : 
        return 'something went wrong , try again'


 

