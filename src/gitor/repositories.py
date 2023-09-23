from gitor import api, _set, gitrequest

def getRepository(self, name: str, raw: bool = False) -> set:
    """
    get a repository
    """
    # if raw wanted then return the raw str
    if raw:
        JSON = gitrequest.request(api.getRepoURL(self.REPO_OWNER, name), gitrequest.json, api.getHeaders(self.TOKEN))
        return gitrequest.request(JSON[api.raw], gitrequest.str, api.getHeaders(self.TOKEN))
    
    return gitrequest.request(api.getRepoURL(self.REPO_OWNER, name), gitrequest.json, api.getHeaders(self.TOKEN))

#def getSubRepositoryByJSON(JSON: set, Name: str, Directory: str):

def getSubRepository(self, name: str, directory: str, raw: bool = False) -> set:
    DirectoryList = directory.split("/")
    LastRepo = getRepository(self, name)

    if not LastRepo: return
    
    # iterate through all the direcotries
    for i in DirectoryList:
        repo = _set.findValueInJSON(LastRepo, api.name, i)
        if not repo: return
        
        # check if another url is needed
        LastRepo = gitrequest.request(repo["url"], gitrequest.json, api.getHeaders(self.TOKEN))
        if not LastRepo: print (f"Error: could not get repo {repo}"); return

    # if raw wanted then return the raw str
    if raw:
        JSON = gitrequest.request(api.getRepoURL(self.REPO_OWNER, name), gitrequest.json, api.getHeaders(self.TOKEN))
        return gitrequest.request(LastRepo[api.raw], gitrequest.str, api.getHeaders(self.TOKEN))
    
    return LastRepo