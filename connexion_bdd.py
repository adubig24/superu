import mysql.connector as mysqlpy

class Connexion_bdd :
    __USER = 'root'
    __PWD = 'example'
    __HOST = 'localhost'
    __PORT = '3307'
    __DB = 'superu'
    __cursor = None
    __bdd = None

    @classmethod
    def connexion(cls):
        if cls.__cursor == None : 
            cls.__bdd = mysqlpy.connect(user = cls.__USER, password = cls.__PWD, host = cls.__HOST, port = cls.__PORT, database = cls.__DB)
            cls.__cursor = cls.__bdd.cursor() 
        
        return cls.__cursor


    @classmethod
    def deconnexion(cls):
        # indispensable pour closer, il faut que tout le cursor soit lu
        cls.__cursor.fetchall()
        cls.__cursor.close()
        cls.__bdd.close()
        cls.__cursor = None