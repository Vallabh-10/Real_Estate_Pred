import argparse
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask , send_from_directory
import pickle
from pywebio.output import *
from pywebio.input import *

Salary_model=pickle.load(open('real_estate_model.pkl','rb'))
app = Flask(__name__)
def predict():
    area=input('Enter Area ',type=FLOAT)
    price=Salary_model.predict([[area]])
    put_text('Predicted Home Price : %.1f' % (price[0]))
    print(price[0])

app.add_url_rule('/tool','webio_view',webio_view(predict),methods=['GET','POST','OPTIONS'])

#app.run(host='Localhost',port=5000)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=8080)
    args=parser.parse_args()
    start_server(predict,port=args.port)