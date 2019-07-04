from http.client import HTTPSConnection
from base64 import b64encode
import json
import os

from tkinter import messagebox
from tkinter import *
#This sets up the https connection
def threads():
    c = HTTPSConnection("engine.freerice.com")
    #we need to base 64 encode it 
    #and then decode it to acsii as python 3 stores it as abyte string#POST https://engine.freerice.com/games/8166e015-f435-4ce8-b1c7-48d2cfd0759b/answer HTTP/1.1
    question_id = '3f361880-805d-55ee-98b4-cb3a28ca2028'
    
    answer = '10'
    first = True
    resource = '/games/dbb11f54-6d72-43f9-b628-6a061aad4922/answer'
    number = 0
    while True:

        if first:
            body = '{"answer":"a' + answer + '","question":"' + question_id + '","user":"61b937cb-ed76-40a3-a79b-91e561914142"}'
            #then connect
            #resource = '/games/33343f63-3db9-4d58-8d44-6560aee481b9/answer'
        else:
            body = '{"category":"66f2a9aa-bac2-5919-997d-2d17825c1837","level":1}'
            #resource = '/games/33343f63-3db9-4d58-8d44-6560aee481b9/answer'
        headers = {'Host': 'engine.freerice.com',\
            'Connection': 'keep-alive',\
            'Content-Length': str(len(body)),\
            'Accept': 'application/json',\
            'Origin': 'https://beta.freerice.com',\
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjE3NDQyOTEsImV4cCI6MTU2NDMzNjI5MSwidXVpZCI6IjYxYjkzN2NiLWVkNzYtNDBhMy1hNzliLTkxZTU2MTkxNDE0MiJ9.q0NRXE58uwFzgr_O5PBSIqQ3QMFVYuyop11tph9sjMM',\
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',\
            'Content-Type': 'application/json',\
            #'Referer: https':'beta.freerice.com',\
            'Accept-Encoding': 'gzip, deflate, br',\
            'Accept-Language': 'en-US,en;q=0.9',}
        try:
            c.request('PATCH', resource, body=body, headers=headers)
        except:
            c = HTTPSConnection("engine.freerice.com")
            continue
        #get the response back
        res = c.getresponse()
        # at this point you could check the status etc
        # this gets the page text
        data = res.read()
        print(type(data))

        x = dict(json.loads(data))


        try:
            question_id = x["data"]["attributes"]["question_id"]
            print(question_id)
            question = x["data"]["attributes"]["question"]["text"]
            question = question.replace("x", "*")
            answer = str(eval(question))
            print(question + " = " + answer)
            print("Done with problem " + str(number))
            first = True
            number += 1
        except KeyError:
            first = False
            print('\n')
            print(x)
            messagebox.showerror()
            break
        if int(number) > 30000:
            raise Exception()
root = Tk()
root.attributes('-topmost', 1)
Button(root, text='Start\nThreading', command=threads).pack()
root.mainloop()
