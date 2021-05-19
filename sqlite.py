import sqlite3
import random

from sqlite3 import Error
__connection = None

def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect ('base.db', check_same_thread=False)
    return __connection

def init_db(force: bool = False):
    conn = get_connection()
    c = conn.cursor()
    conn.commit()

def fact_return(table, id_fact):
    name_t = table
    conn = get_connection()
    c = conn.cursor()
    strin = "SELECT Fact FROM "+ table+" where id = "+ str (id_fact)
    c.execute(strin)
    res = c.fetchall()
    fact_return = ''.join(map(str,res))
    fact_return = fact_return[2:-2]

    if table ==  'chemistry':
        name_t='Химии'
    elif table == 'physics':
        name_t='Физики'
    elif table == 'history':
        name_t='Истории'

    fact_return = "Интересный факт из "+name_t+": \n" +fact_return
    return fact_return
