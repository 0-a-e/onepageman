import requests
import os
import tkinter.messagebox as tkmsg
import os.path
import sys
import tkinter as tk
from flask_sockets import Sockets
from time import sleep
from flask import Flask, session, redirect, render_template, request, make_response, jsonify
from bs4 import BeautifulSoup
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
#名前
filename = "result"
#ファイルの初期化
ddf = open('result.txt','w')
ddf.write('') 
ddf.close()
#ここまで

#ここからボタンクリック時の処理
def ma():
    #入力フォーム内のURLを取得
    UR = txt.get()
    print(UR)
    #ここまでURL取得
    #URL生成
    furl = UR + "/1/"
    #ここまで
    #1ページ目の内容取得
    rf = requests.get(furl)
    soup = BeautifulSoup(rf.content, "html.parser")
    resF = soup.find_all("p")
    #ここまで１ページ目の内容取得
    #info表示
    tkmsg.showinfo('info',"処理を開始しました。結果はresult.txtに書き込まれます。5分ほどお待ちください。(現在バグ)")
    #ココマデinfo
    print(resF)
    run(UR,resF)


def run(UR,resF):
    i = 0
    sd = ch(i,"",resF)
    while not sd == "y":
        i += 1
        print(i)
        url = UR + "/" + str(i) + "/"
        print(url)

        r = requests.get(url)

        soup = BeautifulSoup(r.content, "html.parser")
        res = soup.find_all("p")
        sd = ch(i,res,resF)
        f = open('result.txt','a')
        f.write(str(res) + '\n')
        f.close()
        print(res)
        sleep(5)
def ch(i,res,resF):
    if not i == 1:
        if res == resF or res == "<p>The article you were looking for was not found, but maybe try looking again!</p>" :
            sd = "y"
        else:
            sd = "n"
    else:
#            print("I=else")
        sd = "n"
    return sd
#tkinter setup
ro = tk.Tk()
ro.title(" 記事文字起こし") 
ro.geometry("640x480")
lbl = tk.Label(text='urlを入力してください。')
lbl.place(x=100, y=70)
txt = tk.Entry(width=20)
txt.place(x=100, y=100)
btn = tk.Button(ro, text='送信', command=ma)
btn.place(x=100, y=200 )
ro.mainloop()
#ここまで
