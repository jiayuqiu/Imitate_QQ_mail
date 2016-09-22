# coding:utf-8

import numpy as np

from flask import Flask, request, render_template
from nmc import html
from Send_Email import send_email

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_get():
    return render_template('home.html')

@app.route('/test', methods=['POST'])
def home():
    warn_html = request.form['html_loc']
    warn_str = html(warn_html)
    return render_template('home-show.html', warning_str=warn_str)

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['GET','POST'])
def signin():

    username = request.form['username']
    password = request.form['password']

    shengsi_warning = \
        html("http://www.nmc.cn/publish/forecast/AZJ/shengsi.html")
    shanghai_warning = \
        html("http://www.nmc.cn/publish/forecast/ASH/pudong.html")

###############################################################################

    # 嵊泗获得风速数据

    six_hour_max_wind_ss = max(shengsi_warning['PwindSpeed'][0:1])
    twelve_hour_max_wind_ss = max(shengsi_warning['PwindSpeed'][0:3])
    day_max_wind_ss = max(shengsi_warning['PwindSpeed'])

    six_hou_avg_wind_ss = round(np.mean(shengsi_warning['PwindSpeed'][0:1]),2)
    twelve_hour_avg_wind_ss = round(np.mean(shengsi_warning['PwindSpeed'][0:3]),2)
    day_avg_wind_ss = round(np.mean(shengsi_warning['PwindSpeed']),2)

    # 嵊泗获得能见度数据

    six_hour_max_njd_ss = max(shengsi_warning['Pnjd'][0:1])
    twelve_hour_max_njd_ss = max(shengsi_warning['Pnjd'][0:3])
    day_max_njd_ss = max(shengsi_warning['Pnjd'])

    six_hou_avg_njd_ss = round(np.mean(shengsi_warning['Pnjd'][0:1]), 2)
    twelve_hour_avg_njd_ss = round(np.mean(shengsi_warning['Pnjd'][0:3]), 2)
    day_avg_njd_ss = round(np.mean(shengsi_warning['Pnjd']), 2)

    #### 判断处于哪种预警状态

    # 判断风速
    if(((day_avg_wind_ss <= 10.8)|
            (day_max_wind_ss <= 17.2))):
        shengsi_wind_str = "24小时内无风力预警！" + "\n"
    elif(((day_avg_wind_ss >= 10.8)&(day_avg_wind_ss <= 13.8)|
            ((day_max_wind_ss) >= 17.2)&(day_max_wind_ss <= 20.7))):
        shengsi_wind_str = "24小时内可能发生风速蓝色预警！" + "\n"
    elif(((day_avg_wind_ss >= 17.2)&(day_avg_wind_ss <= 20.7)|
            ((day_max_wind_ss) >= 20.8)&(day_max_wind_ss <= 24.4))):
        shengsi_wind_str = "24小时内可能发生风速黄色预警！" + "\n"
    elif (((twelve_hour_avg_wind_ss >= 24.5) & (twelve_hour_avg_wind_ss <= 28.4) |
                   ((twelve_hour_max_wind_ss) >= 28.5) & (twelve_hour_max_wind_ss <= 32.6))):
        shengsi_wind_str = "12小时内可能发生风速橙色预警！" + "\n"
    elif (((six_hou_avg_wind_ss >= 28.5) & (six_hou_avg_wind_ss <= 32.6) |
           ((six_hour_max_wind_ss) >= 37.0) & (six_hour_max_wind_ss <= 41.4))):
        shengsi_wind_str = "6小时内可能发生风速红色预警！" + "\n"

    # 判断能见度
    if (((day_avg_njd_ss <= 10.8) |
            (day_max_njd_ss <= 17.2))):
        shengsi_njd_str = "24小时内无能见度预警！" + "\n"
    elif (((day_avg_njd_ss >= 10.8) & (day_avg_njd_ss <= 13.8) |
           ((day_max_njd_ss) >= 17.2) & (day_max_njd_ss <= 20.7))):
        shengsi_njd_str = "24小时内可能发生能见度蓝色预警！" + "\n"
    elif (((day_avg_njd_ss >= 17.2) & (day_avg_njd_ss <= 20.7) |
           ((day_max_njd_ss) >= 20.8) & (day_max_njd_ss <= 24.4))):
        shengsi_njd_str = "24小时内可能发生能见度黄色预警！" + "\n"
    elif (((twelve_hour_avg_njd_ss >= 24.5) & (twelve_hour_avg_njd_ss <= 28.4) |
           ((twelve_hour_max_njd_ss) >= 28.5) & (twelve_hour_max_njd_ss <= 32.6))):
        shengsi_njd_str = "12小时内可能发生能见度橙色预警！" + "\n"
    elif (((six_hou_avg_njd_ss >= 28.5) & (six_hou_avg_njd_ss <= 32.6) |
           ((six_hour_max_njd_ss) >= 37.0) & (six_hour_max_njd_ss <= 41.4))):
        shengsi_njd_str = "6小时内可能发生能见度红色预警！" + "\n"

    shengsi_warning = "嵊泗天气预警信息：" + "\n" + shengsi_wind_str + \
                      shengsi_njd_str
############################################################################
    # 上海获得风速数据

    six_hour_max_wind_sh = max(shanghai_warning['PwindSpeed'][0:1])
    twelve_hour_max_wind_sh = max(shanghai_warning['PwindSpeed'][0:3])
    day_max_wind_sh = max(shanghai_warning['PwindSpeed'])

    six_hou_avg_wind_sh = round(np.mean(shanghai_warning['PwindSpeed'][0:1]), 2)
    twelve_hour_avg_wind_sh = round(np.mean(shanghai_warning['PwindSpeed'][0:3]), 2)
    day_avg_wind_sh = round(np.mean(shanghai_warning['PwindSpeed']), 2)

    # 上海获得能见度数据

    six_hour_max_njd_sh = max(shanghai_warning['Pnjd'][0:1])
    twelve_hour_max_njd_sh = max(shanghai_warning['Pnjd'][0:3])
    day_max_njd_sh = max(shanghai_warning['Pnjd'])

    six_hou_avg_njd_sh = round(np.mean(shanghai_warning['Pnjd'][0:1]), 2)
    twelve_hour_avg_njd_sh = round(np.mean(shanghai_warning['Pnjd'][0:3]), 2)
    day_avg_njd_sh = round(np.mean(shanghai_warning['Pnjd']), 2)

    #### 判断处于哪种预警状态

    # 判断风速
    if (((day_avg_wind_sh <= 10.8) |
             (day_max_wind_sh <= 17.2))):
        shanghai_wind_str = "24小时内无风力预警！" + "\n"
    elif (((day_avg_wind_sh >= 10.8) & (day_avg_wind_sh <= 13.8) |
                   ((day_max_wind_sh) >= 17.2) & (day_max_wind_sh <= 20.7))):
        shanghai_wind_str = "24小时内可能发生风速蓝色预警！" + "\n"
    elif (((day_avg_wind_sh >= 17.2) & (day_avg_wind_sh <= 20.7) |
                   ((day_max_wind_sh) >= 20.8) & (day_max_wind_sh <= 24.4))):
        shanghai_wind_str = "24小时内可能发生风速黄色预警！" + "\n"
    elif (((twelve_hour_avg_wind_sh >= 24.5) & (twelve_hour_avg_wind_sh <= 28.4) |
                   ((twelve_hour_max_wind_sh) >= 28.5) & (twelve_hour_max_wind_sh <= 32.6))):
        shanghai_wind_str = "12小时内可能发生风速橙色预警！" + "\n"
    elif (((six_hou_avg_wind_sh >= 28.5) & (six_hou_avg_wind_sh <= 32.6) |
                   ((six_hour_max_wind_sh) >= 37.0) & (six_hour_max_wind_sh <= 41.4))):
        shanghai_wind_str = "6小时内可能发生风速红色预警！" + "\n"

    # 判断能见度
    if (((day_avg_njd_sh <= 10.8) |
             (day_max_njd_sh <= 17.2))):
        shanghai_njd_str = "24小时内无能见度预警！" + "\n"
    elif (((day_avg_njd_sh >= 10.8) & (day_avg_njd_sh <= 13.8) |
                   ((day_max_njd_sh) >= 17.2) & (day_max_njd_sh <= 20.7))):
        shanghai_njd_str = "24小时内可能发生能见度蓝色预警！" + "\n"
    elif (((day_avg_njd_sh >= 17.2) & (day_avg_njd_sh <= 20.7) |
                   ((day_max_njd_sh) >= 20.8) & (day_max_njd_sh <= 24.4))):
        shanghai_njd_str = "24小时内可能发生能见度黄色预警！" + "\n"
    elif (((twelve_hour_avg_njd_sh >= 24.5) & (twelve_hour_avg_njd_sh <= 28.4) |
                   ((twelve_hour_max_njd_sh) >= 28.5) & (twelve_hour_max_njd_sh <= 32.6))):
        shanghai_njd_str = "12小时内可能发生能见度橙色预警！" + "\n"
    elif (((six_hou_avg_njd_sh >= 28.5) & (six_hou_avg_njd_sh <= 32.6) |
                   ((six_hour_max_njd_sh) >= 37.0) & (six_hour_max_njd_sh <= 41.4))):
        shanghai_njd_str = "6小时内可能发生能见度红色预警！" + "\n"

    shanghai_warning = "上海天气预警信息：" + "\n" + shanghai_wind_str + \
                       shanghai_njd_str
    #######################################################################


    if username=='admin' and password=='password':

        return render_template('sign-OK.html',
                               username=username,
                               shanghai_warning_str=shanghai_warning.decode("utf-8"),
                               shengsi_warning_str=shengsi_warning.decode("utf-8"),
                               six_avg_wind_sh = six_hou_avg_wind_sh,
                               six_avg_wind_ss = six_hou_avg_wind_ss,
                               twelve_avg_wind_sh = twelve_hour_avg_wind_sh,
                               twelve_avg_wind_ss = twelve_hour_avg_wind_ss,
                               day_avg_wind_sh = day_avg_wind_sh,
                               day_avg_wind_ss = day_avg_wind_ss,
                               six_avg_njd_sh=six_hou_avg_njd_sh,
                               six_avg_njd_ss=six_hou_avg_njd_ss,
                               twelve_avg_njd_sh=twelve_hour_avg_njd_sh,
                               twelve_avg_njd_ss=twelve_hour_avg_njd_ss,
                               day_avg_njd_sh=day_avg_njd_sh,
                               day_avg_njd_ss=day_avg_njd_ss
                               )

    return render_template('form.html',
                           message='Bad username or password',
                           username=username)

@app.route('/emailResult', methods=['GET', 'POST'])
def send_result():
    email_addr  = request.form['email_str']
    warning_str = request.form['warning_str']

    email_addr_list = email_addr.split(';')
    send_email(to_addr=email_addr_list, warning_str=warning_str)
    return render_template('emailResult.html')

if __name__ == '__main__':
    app.run(debug=True)
