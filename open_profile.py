from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
import requests


login_url = 'http://localhost:3001/v1.0/auth/login-with-token'
auth_token = '' # Your API Key
request_data = {
    'token':auth_token
}
headers = {
    'Content-Type': 'application/json'
}

profile_id = '' # Profile id of that you want to open

response = requests.post(login_url, json=request_data, headers=headers)
if response.status_code == 200: # Profile opened successfully

    req_url = 'http://localhost:3001/v1.0/browser_profiles/'+  profile_id  +'/start?automation=1'
    response = requests.get(req_url)
    response_json = response.json()
    port = str(response_json['automation']['port'])
    chrome_drive_path = Service("C:/Users/HP/Desktop/adbot/include/chromedriver.exe")

    options = webdriver.ChromeOptions()
    options.debugger_address = '127.0.0.1:' + port

    driver = webdriver.Chrome(service=chrome_drive_path, options=options)





else: # Profile was not opened
    print('Error:', response.status_code)



