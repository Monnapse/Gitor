name = "name"
raw = "download_url"

def get_repo_url(owner: str, name: str):
    """
    Get the repository url
    """
    owner = owner.lower()
    name = name.lower()
    return f"https://api.github.com/repos/{owner}/{name}/contents"

def get_headers(token: str):
    """
    get headers for private repositories
    """
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }