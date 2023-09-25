from gitor import api, _set, gitrequest

def get_repository_raw(self, repo: set):
    return gitrequest.request(repo[api.raw], gitrequest.str, api.get_headers(self.TOKEN))
def get_repository_JSON(self, repo: set):
    return gitrequest.request(repo[api.children], gitrequest.json, api.get_headers(self.TOKEN))

def get_repository(self, name: str, raw: bool = False) -> set or str:
    """
    get a repository
    """
    # if raw wanted then return the raw str
    if raw:
        JSON = gitrequest.request(api.get_repo_url(self.REPO_OWNER, name), gitrequest.json, api.get_headers(self.TOKEN))
        return get_repository_raw(self, JSON)
    
    return gitrequest.request(api.get_repo_url(self.REPO_OWNER, name), gitrequest.json, api.get_headers(self.TOKEN))

def get_sub_repository(self, name: str, directory: str, raw: bool = False) -> set or str:
    DirectoryList = directory.split("/")
    LastRepo = get_repository(self, name)

    if not LastRepo: return
    
    # iterate through all the direcotries
    for i in DirectoryList:
        repo = _set.find_value_in_json(LastRepo, api.name, i)
        if not repo: return
        
        # check if another url is needed
        LastRepo = gitrequest.request(repo[api.children], gitrequest.json, api.get_headers(self.TOKEN))
        if not LastRepo: print (f"Error: could not get repo {repo}"); return

    # if raw wanted then return the raw str
    if raw:
        JSON = gitrequest.request(api.get_repo_url(self.REPO_OWNER, name), gitrequest.json, api.get_headers(self.TOKEN))
        return get_repository_raw(self, JSON)
    
    return LastRepo

def build(repo_name: str, content: str):
    return {'name': repo_name, 'content': content}

def build_repository(self, repository: set) -> set:
    repo_build = {}
        #print(proxy, last)

    def add_to_directory(build: set, path: str):
        directory_list = path.split("/")
        last = repo_build
        #proxy = last
        index = 0

        # iterate through all the paths
        for i in directory_list:
            index+=1
            if index == len(directory_list):
               last[i] = build
            else:
               try:
                    if last[i]:
                        last = last[i]
               except:
                   last[i] = {}
                   last = last[i]

    def iterate(rep: set):
        for repo in rep:
            if api.is_repo_file(repo):
                #print(repo[api.raw])
                content = get_repository_raw(self, repo)
                
                #repo_build[repo[api.name]] = build(repo[api.name],content[api.raw])
                #print(build(repo[api.name], content))
                add_to_directory(build(repo[api.name], content), repo[api.path])
            else:
                iterate(get_repository_JSON(self,repo))

    iterate(repository)
    return repo_build