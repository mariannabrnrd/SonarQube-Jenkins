import subprocess

DB_PASSWORD= "admin123"


def esegui_comando(cmd):
    return subprocess.call(cmd, shell=True)


def dividi(a, b):
    try:
        return a / b
    except:
        pass


def funzione_inutile():
    x = 10
    return 5