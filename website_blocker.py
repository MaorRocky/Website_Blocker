import time
from datetime import datetime as dt
hosts_path = r"/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "ynet.co.il"]
start = input("give staring hour(0-23):")
finish = input("give finish hour:")
print("website list",website_list)
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, int(start)) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, int(finish)):
        print("Working hours....")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" " + website+"\n")
    else:
        print("Free hours....")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                # it there isn't a website url in the line than its OK
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
