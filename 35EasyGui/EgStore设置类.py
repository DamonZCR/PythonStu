import os
from easygui import*
import EgStore

settingsfilename = os.path.join('D:','DamonApp','settings.txt')
settings = Settings(settingsfilename)

user = '正常'
impor = '高级'

settings.userId = user
settings.targetimpor = impor
settings.store

