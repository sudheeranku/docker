
import os
#import chromedriver_autoinstaller
import requests
import logging
# import graypy
import time
import requests, json

import shutil
import pandas as pd
from datetime import datetime
from logging import exception
from urllib import request
from contextlib import contextmanager
import repackage, json
from collections import OrderedDict
from robot.api.deco import keyword

repackage.up()
# from robot.api.deco import keyword
from TestCases.ConfigFileParser import ConfigFileParser

config = ConfigFileParser()
data=config.getCfgdetails()
# host_ip = data['Att_support']['Username']
# host_port = data['Att_support']['Password']
# print(host_ip)
# print(host_port)

# folderpath = "C:/bin/chromedriver"
@keyword("GET_CHROME_PATH")
def getChromepath(folder):
    chromedriver_autoinstaller.install(path = folder)  # Check if the current version of chromedriver exists
                                          # and if it doesn't exist, download it automatically,
                                          # then add chromedriver to path

    sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
    print("subfolder ** ", sub_folders)
    print("length ** ", len(sub_folders))
    index = len(sub_folders) - 1
    print("index*** ", index)
    if len(sub_folders) >= 1 :
        driverpath = sub_folders[index]
        chromepath = 'C:/bin/chromedriver/' + driverpath + '/chromedriver.exe'
    else:
        print("chromedriver folder not present")
        chromepath = ''
    return chromepath


@keyword("VER")
def getValue():
    print("***************")
    data=config.getCfgdetails()
    host_url = data['verizon_support']['HostPort']
    host_user = data['verizon_support']['Username']
    host_pd = data['verizon_support']['Password']
    # print(host_user)
    # print(host_pd)
    print("***************end")
    return host_url,host_user,host_pd

@keyword("FRT")
def getValue1():
    print("***************")
    data=config.getCfgdetails()
    host_url = data['frontier_support']['HostPort']
    host_user = data['frontier_support']['Username']
    host_pd = data['frontier_support']['Password']
    # print(host_user)
    # print(host_pd)
    print("***************end")
    return host_url,host_user,host_pd
