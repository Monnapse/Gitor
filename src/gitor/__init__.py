class Git:
    # Initiate Class
    def __init__(self, repoOwner: str, token: str = None):
        """
        Go to github account
        Token is only required if you are getting private repositories
        """
        self.REPO_OWNER = repoOwner
        self.TOKEN = token

    # Import all child methods
    from .repositories import get_repository, get_sub_repository, build_repository

def find_in_repo_build(repo_build: set, path: str, raw: bool = False) -> set or str:
    directories = path.split("/")
    current = repo_build
    for i in directories:
        try:
            current = current[i]
        except:
            print(f"Error: No directory called {i}")
            return

    if raw:
        return current["content"]
    else:
        return current