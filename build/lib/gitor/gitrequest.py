import requests

# return types
json = 0
str = 1

def request(apiUrl: str, _response: int = 0, headers: set=None) -> set:
    """
    request with no python errors
    """
    try:
        response = requests.get(apiUrl, headers=headers)

        if response.status_code == 200:
            repo_data = response.content

            if _response == 0:
                repo_data = response.json()

            return repo_data
        else:
            print(f"Error: {response.status_code} | {response.text}")

    except Exception as e:
        print(f"Error: {str(e)}")