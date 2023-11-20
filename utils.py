import mysql.connector
from os import system

def conn():
    return mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'banco_teste'
)

def existMed(name):
    db = conn()
    mycursor = db.cursor()
    cmd = f"SELECT farmaco FROM meds WHERE farmaco LIKE '%{name}%'"
    mycursor.execute(cmd)
    res = mycursor.fetchall()
    db.close()
    return len(res) > 0


def searchFarm(name):
    db = conn()
    mycursor = db.cursor()
    cmd = f"SELECT farmaco FROM meds WHERE farmaco LIKE '%{name}%'"
    mycursor.execute(cmd)
    res = mycursor.fetchall()
    farmList = list()
    for line in res:
        if line[0] not in farmList:
            farmList.append(line[0])
    db.close()
    return farmList



def searchMed(name):
    db = conn()
    mycursor = db.cursor()
    cmd = f"SELECT medicamento, concentracao, detentor FROM meds WHERE farmaco LIKE '{name}'"
    mycursor.execute(cmd)
    result = mycursor.fetchall()
    db.close()
    return result


def limpar():
    system('cls')


