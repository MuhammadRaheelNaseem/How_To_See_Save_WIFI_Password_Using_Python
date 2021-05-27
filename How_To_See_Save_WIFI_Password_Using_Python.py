import subprocess

data=subprocess.check_output(['netsh','wlan','show','profile']).decode('utf-8').split('\n') # showing available network

profile=[i.split(':')[1][1:-1] for i in data if "All User Profile" in i] # showing saved network

for i in profile:
    result = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8').split('\n')
    result = [b.split(":")[1][1:-1] for b in result if "Key Content" in b]
    try:
        print("{:<30} | {:<}".format(i,result[0]))
    except IndexError:
        print("{:<30} | {:<}".format(i,""))