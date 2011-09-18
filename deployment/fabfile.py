import os
from os.path import join
from fabric.api import run, cd, env
from fabric.operations import put, local, run
from fabric.context_managers import prefix, settings
from fabric.contrib.files import append, exists, contains

# We use the same layout for test, staging, and production
PROJECT_NAME = "visimus"
HOMEDIR = "/home/kroger"
BASE_DIR = join(HOMEDIR, "webapps", PROJECT_NAME)
PROJECT_DIR = join(BASE_DIR, PROJECT_NAME)
DEPLOYMENT_DIR = join(PROJECT_DIR, "deployment")
CONFIG_DIR = join(DEPLOYMENT_DIR, "config")
REQUERIMENTS = join(DEPLOYMENT_DIR, "requirements.txt")



def prod():
    env.hosts = ['pedrokroger.net']
    env.user = "kroger"


def git_push():
    local("git push")


def git_pull():
    with cd(PROJECT_DIR):
        run("git pull")


def apache():
    run(join(BASE_DIR, "apache2/bin/restart"))


def migrate_database():
    with cd(PROJECT_DIR):
        run("./manage.py migrate matrix")


def deploy():
    git_push()
    git_pull()
    migrate_database()
    apache()
