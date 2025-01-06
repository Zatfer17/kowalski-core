from datetime import datetime
from git      import Repo
from os       import path


MESSAGE = """Sync notes

{}
"""

class Git():

    def __init__(self, local_path: str, user_name: str, repo_name: str, branch_name: str, log_file: str):
        self.local_path = local_path
        self.user_name = user_name
        self.repo_name = repo_name
        self.branch_name = branch_name
        self.log_file = log_file

    def initialize(self):
        self.repo = Repo(self.local_path)
        self.origin = self.repo.remote(name='origin')
        self.origin.set_url(f"git@github.com:{self.user_name}/{self.repo_name}.git")

    def lean_commit(self, message: str, name: str):
        f = open(self.log_file, 'a+')
        commit_message = f"{message} Note {name}.md\n"
        f.write(commit_message)

    def pull(self):
        self.origin.fetch()
        self.origin.pull(refspec=self.branch_name)

    def commit(self):
        self.repo.git.add(all=True)
        if not path.exists(self.log_file):
            open(self.log_file, 'w').close()    
        f = open(self.log_file)
        self.repo.index.commit(MESSAGE.format(f.read()))
        open(self.log_file, 'w').close() # Empty it

    def push(self):
        self.origin.push(refspec=self.branch_name)