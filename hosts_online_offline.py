import os
import csv
import threading
import subprocess
from ping3 import ping
import time
from datetime import datetime, date, timedelta


start_time = datetime.now()
timestamp = start_time.strftime('%d_%b_%Y')

fileoo = 'onlineoo.csv'
file_offline = 'offline_' + timestamp + '.csv'
file_online = 'online_' + timestamp + '.csv'

def scan_file(fileoo):
    scan_list = {}
    with open(fileoo. encoding="utf8") as File:
        reader = csv.reader(File)
        for row in reader:
            scan_list[row[4]] = [row[0], row[1]]
    return scan_list

def isUp(ip, name, host_oo, off, onl):
    response = ping(ip)
    wrt = f'{name},{ip},{host_oo}\n'

    if response is not None:
        onl.write(f'ONLINE,{wrt}')
    else:
        off.write(f'OFFLINE,{wrt}')


def worker(scan_list):
    threads = []
    off = open(file_offline, 'w', encoding="utf8")
    onl = open(file_online, 'w', encoding="utf8")

    for ip, name in scan_list.items():
        threads.append(threading.Thread(target=isUp, args=(ip, name[0], name[1], off, onl)))

    for thread in threads:
        time.sleep(0.001)
        thread.start()

    for thread in threads:
        thread.join()

    off.close()
    onl.close()

def day_3_off():
    today = date.today()
    scan_list = {}
    for i in range(3):
        prev_day = today - timedelta(days=i):
        file_scan = 'offline_' + prev_day.strftime('%d_%b_%Y') + '.csv'
        if os.path.exists(file_scan):
            if len(scan_list) > 1:
                scan_day = []
                with open(file_scan, encoding="utf8") as File:
                    reader = csv.reader(File)
                    for row in reader:
                        scan_day.append(row[3])
                for key in scan_list.copy():
                    if key not in scan_day:
                        scan_list.pop(key)
            else:
                with open(file_scan, encoding="utf8") as File:
                    reader = csv.reader(File)
                    for row in reader:
                        scan_list[row[3]] = [row[1], row[2]]

    with open('off_day_3_' + today.strftime('%d_%b_%Y') + '.csv', "w", encoding="utf8", newline='') as File:
        writer = csv.writer(File, delimiter=',')
        for key,item in scan_list.items():
            writer.writerow([item[0],key,item[1]])

scan_list = scan_file(fileoo)
worker(scan_list)
day_3_off()

end_time = datetime.now()

print("Time: {}".format(end_time - start_time))

