import json
import time
import threading

def create(k,v,t):
    #text file
    with open('data.txt','w') as file:
        file.write(k)
        file.write(v)
    d={}
    with open('data.txt') as f:
        for line in f:
            k,v=line.strip().split('_')
            d[int(k)]=v.strip()
    #json file
    json_file=open('data.json','w')
    json.dump(d,json_file,indent=4,sort_keys=True)
    json_file.close()
def read(k):
    try:
        #check value present in json file
        with open('data.json','r') as file:
            data=json.load(file)
            if k in data:
                print(data[k])
            else:
                print('not found')
    except:
        print('Sorry File is empty')
def delete(k):
    try:
        with open('data.json','w') as file:
            data = json.load(file)
            for i in range(len(data)):
               if data[i][key]==k:
                   del data[i]
                   print('key deleted')
               else:
                   print('wrong key not found')
    except:
        print('Sorry file is empty')
            # print('{}:{} is deleted'.format(k,data[k]))
def deletetime(k):
    try:
        with open('data.json','w') as file:
            data = json.load(file)
            for i in range(len(data)):
                 if data[i][key]==k:
                     del data[i]
                     print('your data is expired')
                 else:
                     print('value is not found')
    except:
        print('\nSorry your key is no long ')
        print('it is expired please create new key')
        print('press 1 for create ,2 for read,3 for delete operation')


print('Do you want to continue yes(y) or no(n)')
ch=input('press y or n')

while ch=='y':
    print('press 1 for create ,2 for read,3 for delete operation')
    n = int(input('enter b/n 1 to 3 :'))
    if n>3 or n<1:
        print('you did enter correct value')
        break
    elif n==1:
        key=input('enter the key:')
        value=input('enter the value:')
        #time value for expire zero is default value
        time=float(input('enter the expire time in sec 0 is no expire'))
        create(key,'_'+value,time)
        print('Value is created')
        #thread to live the key
        if time == 0 or time < 0:
            print('no schedule')
        else:
            wait = threading.Timer(time, deletetime,args=key)
            wait.start()


    elif n==2:
        key=input('enter the key:')
        read(key)
        continue
    elif n==3:
        key=input('enter the key:')
        delete(key)
        continue
    elif n<3:
        print('you enter the wrong value ')
        print('please enter between 1 to 3')
        break

