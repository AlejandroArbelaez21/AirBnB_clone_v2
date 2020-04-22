#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """ do_pack funtion """
    local("mkdir -p versions")
    current = datetime.now()
    current = current.now()
     = "web_static_{}.tgz".format(current.strftime("%Y%m%d%H%M%S"))
    working = local("tar -cavf versions/{} web_static".format(tgz))

    if working.failed:
        return None
    else:
        return tgz