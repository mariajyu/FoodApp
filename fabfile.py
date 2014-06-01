from fabric.api import local
from fabric.api import lcd

def prepare_deployment(branch_name):
    local('python manage.py test FoodApp')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)


def deploy():
    with lcd('/path/to/my/prod/area/'):
        local('git pull /my/path/to/dev/area/')
        local('python manage.py migrate FoodApp')
        local('python manage.py test FoodApp')
        local('/my/command/to/restart/webserver')