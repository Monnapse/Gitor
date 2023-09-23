
import os
from gitor import Git, api

MyGithubConnection = Git("Monnapse",os.environ.get("GITHUB_TOKEN"))
MyPrivateRepo = MyGithubConnection.getSubRepository("monnapse-website", "app.py", True)
MyPublicRepo = MyGithubConnection.getRepository("flow")

print(MyPrivateRepo,MyPublicRepo)