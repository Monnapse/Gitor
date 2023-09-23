# pip install . or set PYTHONPATH=%PYTHONPATH%;D:\Documents\Packages\Python\Gitor\src

import os
from gitor import Git, api

#
MyGithubConnection = Git("Monnapse",os.environ.get("GITHUB_TOKEN"))
MyPrivateRepo = MyGithubConnection.get_sub_repository("monnapse-website", "app.py", True)
MyPublicRepo = MyGithubConnection.get_repository("flow")

print(MyPublicRepo)