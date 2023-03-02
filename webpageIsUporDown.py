import requests

def webpageIsdown():
    url = "https://www.google.com"
    page = requests.get(url, timeout=5)
    res = page.status_code

    #Initial status code is 200, so it checks if the condition is true.
    if res == 200:
        print("webpage is up")
    else:
        print("webpage is down")
        
webpageIsdown()