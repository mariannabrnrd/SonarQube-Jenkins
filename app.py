import subprocess

DB_PASSWORD= "admin123"


def esegui_comando(cmd):
    return subprocess.call(cmd, shell=True)


def dividi(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def funzione_inutile():
    return 5

def calcola_media(valori):
    totale = 0
    for v in valori:
        totale += v
    try:
        return totale / len(valori)
    except ZeroDivisionError:
        return None





