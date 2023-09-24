import requests
import time

# return types
json = 0
str = 1

# rates
warning_limit = 75 # limit requests until warning
rate_limit = 100 # limit requests | so you dont get rate limited by github
rate_time = 5 # sec
last = time.time()
i = 0

def request(apiUrl: str, _response: int = 0, headers: set=None) -> set:
    """
    request with no python errors
    """
    # globals
    global i
    global last

    if i > warning_limit and time.time()-last < rate_limit:
        if i > rate_limit:
            print("Rate limit exceeded")
            return
        
        print("Warning: you should slowdown your requests")
    elif time.time()-last > rate_limit:
        i = 0

    try:
        response = requests.get(apiUrl, headers=headers)
        i+=1
        last = time.time()

        if response.status_code == 200:
            repo_data = response.content

            if _response == 0:
                repo_data = response.json()

            return repo_data
        else:
            print(f"Error: {response.status_code} | {response.text}")

    except Exception as e:
        print(f"Error: {str(e)}")