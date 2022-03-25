#!/usr/bin/env python3
""" Fab file for deploying static file """
from fabric.api import run, get, put, local
from datetime import datetime


def do_pack():
    """
    This function creates a tar file from the files inside the web_static
    dir
    """
    d = datetime.now()
    tarFile = f"web_static_{d.year}{d.month}{d.day}{d.hour}{d.minute}{d.second}.tgz"

    print('Packing web_static to versions/{}'.format(tarFile))
    local('if [ ! -d versions ]; then mkdir versions; fi')
    res = local(f'tar -cvzf versions/{tarFile} web_static')
    if res.failed:
        return None
    return 'versions/' + tarFile
