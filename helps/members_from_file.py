import time
import requests



url_add = "http://10.0.0.3:5000/add_member"

file = "members.txt"

with open(file, 'r') as f:
    for line in f:
        name, email = line.strip().split(",")
        post_data = {'name':name, 'email':email}
        print(post_data, url_add)

        ans = requests.post(url=url_add, data=post_data)
        print(ans.raw)
        print(ans.text)
        print(ans.url)
        time.sleep(1)