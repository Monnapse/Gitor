# pip install . or set PYTHONPATH=%PYTHONPATH%;D:\Documents\Packages\Python\Gitor\src

import os
from gitor import Git, api, gitrequest, find_in_repo_build

#gitrequest.warning_limit = 1
#gitrequest.rate_limit = 1
#gitrequest.rate_time = 0

MyGithubConnection = Git("Monnapse",os.environ.get("GITHUB_TOKEN"))
#MyPrivateRepo = MyGithubConnection.get_sub_repository("monnapse-website", "app.py", True)
MyPublicRepo = MyGithubConnection.get_repository("Utils")
MyPublicRepoBuild = MyGithubConnection.build_repository(MyPublicRepo)

print(find_in_repo_build(MyPublicRepoBuild, "src/Instances/init.lua", True))