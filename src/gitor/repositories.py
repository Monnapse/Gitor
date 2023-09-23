from gitor import api, _set, gitrequest

def get_repository(self, name: str, raw: bool = False) -> set:
    """
    get a repository
    """
    # if raw wanted then return the raw str
    if raw:
        JSON = gitrequest.request(api.get_repo_url(self.REPO_OWNER, name), gitrequest.json, api.get_headers(self.TOKEN))
        return gitrequest.request(JSON[api.raw], gitrequest.str, api.get_headers(self.TOKEN))
    
    return gitrequest.request(api.get_repo_url(self.REPO_OWNER, name), gitrequest.json, api.get_headers(self.TOKEN))

#def getSubRepositoryByJSON(JSON: set, Name: str, Directory: str):

def get_sub_repository(self, name: str, directory: str, raw: bool = False) -> set:
    DirectoryList = directory.split("/")
    LastRepo = get_repository(self, name)

    if not LastRepo: return
    
    # iterate through all the direcotries
    for i in DirectoryList:
        repo = _set.find_value_in_json(LastRepo, api.name, i)
        if not repo: return
        
        # check if another url is needed
        LastRepo = gitrequest.request(repo["url"], gitrequest.json, api.get_headers(self.TOKEN))
        if not LastRepo: print (f"Error: could not get repo {repo}"); return

    # if raw wanted then return the raw str
    if raw:
        JSON = gitrequest.request(api.get_repo_url(self.REPO_OWNER, name), gitrequest.json, api.get_headers(self.TOKEN))
        return gitrequest.request(LastRepo[api.raw], gitrequest.str, api.get_headers(self.TOKEN))
    
    return LastRepo