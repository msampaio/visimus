import os
import subprocess
from visimus import settings


def git(repodir, *args):
    gitdir = os.path.join(repodir, ".git")
    gitcmd = ["git", "--git-dir=" + gitdir, "--work-tree=" + repodir]
    return subprocess.check_output(gitcmd + list(args))


def git_log():
    try:
        repodir = settings.MAINDIR
        branches = git(repodir, "branch")
        settings.logger.debug(branches)
        commit = git(repodir, "log", "--format=format:%h", "-1")
        branch = [x[2:] for x in branches.split('\n') if x.startswith('*')][0]
        return branch + '--' + commit
    except Exception as error:
        settings.logger.error(error)
        return "no git"
