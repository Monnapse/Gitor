name = "name"
raw = "download_url"
type = "type"
path = "path"
children = "url"

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

def is_file(type: str):
    """
    Check if the current argument value is equal to file
    """
    if type == "file": return True
    return False

def is_repo_file(repo: set):
    """
    Check if repo is a file or a directory/folder
    """
    return is_file(repo[type])