name = "name"
raw = "download_url"

def getRepoURL(owner: str, name: str):
    """
    Get the repository url
    """
    owner = owner.lower()
    name = name.lower()
    return f"https://api.github.com/repos/{owner}/{name}/contents"

def getHeaders(token: str):
    """
    get headers for private repositories
    """
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }