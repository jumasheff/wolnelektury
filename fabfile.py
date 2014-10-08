from fnpdjango.deploy import *
try:
    from fabfile_local import *
except ImportError:
    pass


env.project_name = 'wolnelektury'


@task
def production():
    env.hosts = ['giewont.icm.edu.pl']
    env.user = 'lektury'
    env.app_path = '/srv/wolnelektury.pl'
    env.services = [
        DebianGunicorn('wolnelektury'),
        Supervisord('celery.wolnelektury:'),
    ]


@task
def staging():
    env.hosts = ['54.77.63.92']
    env.user = 'dastan'
    env.app_path = '/home/dastan/wolnelektury'
    env.services = [
        DebianGunicorn('wolnelektury'),
    ]
