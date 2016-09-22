# coding:utf-8

import numpy as np

from flask import Flask, request, render_template
# from nmc import html
from Send_Email import send_email

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_get():
    print "1"
    return render_template('index.html')

# @app.route('/', methods=['POST'])
# def home():
#     return render_template('index.html')

@app.route('/emailResult', methods=['GET', 'POST'])
def send_result():
    error_str = '' # 初始化错误信息

    try:
        email_addr = request.form['addrs']
        email_addr_list = email_addr.split(";")
        print email_addr
    except:
        tmp_error = "error email_addr"
        error_str = error_str + tmp_error
        print "error email_addr"

    try:
        email_subject = request.form['subject']
        print email_subject
    except:
        tmp_error = "error email_subject"
        error_str = error_str + tmp_error
        print "error email_subject"

    try:
        email_message = request.form['message']
        print email_message
    except:
        tmp_error = "error email_message"
        error_str = error_str + tmp_error
        print "error email_message"


    try:
        send_email(to_addr=email_addr_list,
                   subject_str=email_subject,
                   warning_str=email_message)
        print "发送成功"
    except:
        tmp_error = "error happened though sending"
        error_str = error_str + tmp_error
        # print "send error"

    if error_str:
        print "发送失败"
        return render_template('index.html', error_message=error_str)
    else:
        return render_template('send_result_ok.html')

if __name__ == '__main__':
    app.run(debug=True)