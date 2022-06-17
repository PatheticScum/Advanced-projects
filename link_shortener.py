# pip install pyshorteners

import pyshorteners

shortener = pyshorteners.Shortener()

result = shortener.tinyurl.short('https://youtu.be/eZH_8FxDrMQ')
