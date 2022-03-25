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

    local('if [ ! -d version ]; then mkdir version; fi')
    res = local(f'tar -cvzf version/{tarFile} web_static')
    if res.failed:
        return None
    return 'version/' + tarFile
