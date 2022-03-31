#!/usr/bin/python3
""" Fab file for deploying static file """
from fabric.api import run, put, local
from datetime import datetime
import os


def do_pack():
    """This function creates a tar file from the files inside the web_static
    dir
    """
    d = datetime.now()
    date = f"{d.year}{d.month}{d.day}{d.hour}{d.minute}{d.second}.tgz"
    tarFile = "web_static_" + date

    print('Packing web_static to versions/{}'.format(tarFile))

    if os.path.isdir("versions") is False:
        local("mkdir -p versions")
    res = local(f'tar -cvzf versions/{tarFile} web_static')
    if res.failed:
        return None
    return 'versions/' + tarFile
