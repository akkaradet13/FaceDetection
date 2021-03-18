
import requests, time, os

def sendData(file):
    url = 'http://127.0.0.1:8000/getData'
    # myobj = {
    #     'postName' : 'koko',
    #     'description' : '123456789',
    #     'time' : '16/8/2020:23:06'
    #          }
    file = {
        'upload_file': open(file,'rb')
        }
    # x = requests.post(url, data = myobj, files=file)
    x = requests.post(url, files=file)
    if x.text == "200":
        os.remove("demofile.txt")
    else :
        print(f'Error {file}')

entries = os.listdir('face2/')
amountFile = len(entries)
n = 0
for file in entries:
    sendData(f'face2/{file}')
    time.sleep(1)
    n+=1
    print(f'Processing... {(amountFile/n)*100}%')
print(entries)
