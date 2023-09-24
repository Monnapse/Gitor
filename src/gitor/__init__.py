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