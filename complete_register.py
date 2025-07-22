import requests
import scratchattach
import random
import threading

accounts = []

for account in open("accounts.txt", "r").read().splitlines():
    accounts.append(account.split(","))

def complete_class(session=None,username=None, password=None):
    if session:
        session = session
    else:
        session = scratchattach.login(username, password)
    
    headers = session._headers
    headers["content-type"] = "application/x-www-form-urlencoded"
    payload = {
        "birth_month": str(random.randint(1, 11)),
        "birth_year": str(random.randint(2000, 2025)),
        "gender": "male",
        "country": "Argentina",
        "is_robot": "false",
        "password": password,
    }

    req = requests.post("https://scratch.mit.edu/classes/student_update_registration/", headers=headers, cookies=session._cookies, data=payload)
    print(req.status_code)

for i in accounts:
    threading.Thread(target=complete_class, args=(None, i[0], i[1])).start()
