
import os
from gitor import Git, api

MyGithubConnection = Git("Monnapse",os.environ.get("GITHUB_TOKEN"))
MyPublicRepo = MyGithubConnection.getSubRepository("monnapse-website", "app.py", True)
MyPublicRepo = MyGithubConnection.getRepository("monnapse-website")

print(MyPublicRepo)