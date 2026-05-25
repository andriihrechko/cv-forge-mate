import os
import sys

GTK_PATH = r'C:\Users\1\GTK3-Runtime Win64\bin'

if sys.platform == 'win32' and os.path.exists(GTK_PATH):
    try:
        os.add_dll_directory(GTK_PATH)
    except AttributeError:
        os.environ['PATH'] = GTK_PATH + os.path.pathsep + os.environ['PATH']