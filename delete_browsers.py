from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
import requests
import json


auth_token = '' # Your API Key


def listBrowsers():

    url = "https://dolphin-anty-api.com/browser_profiles"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }



    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200: # Select Profile List

        response_data = json.loads(response.text)
        data = response_data.get('data', [])

        if data:
            url = "https://dolphin-anty-api.com/browser_profiles?forceDelete=1"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + auth_token
            }
            for item in data:
                profile_id = item.get("id")
                payload = {'ids': [profile_id], 'forceDelete': True}
                
                delete_url = f"https://dolphin-anty-api.com/browser_profiles/{profile_id}"
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + auth_token
                }
                

                # Delete all profiles
                response = requests.delete(delete_url, headers=headers, json=payload)
                print(response.text)

        else:
            print("There isn't any profile created.")


listBrowsers()

