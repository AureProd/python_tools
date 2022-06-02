#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#---------------------------------------
# controlle les fonctions liées à la db
# 
# author : huet jb
#---------------------------------------

from .tools_functions import check_type, print_error
import pymysql

def db_connect(host: str, user: str, passwd: str, db: str) -> pymysql.connect:
    """Connection to a MySQL database.

    Args:
        host (str): MySQL host.
        user (str): MySQL user.
        passwd (str): MySQL password.
        db (str): MySQL database name.

    Returns:
        pymysql.connect: MySQL connection instance.
    """
    
    try:
        # Connexion a la base de données MYSQL
        db = pymysql.connect(port=0, host=host, user=user, passwd=passwd, db=db)
        db.autocommit(True) # pour effectuer les commandes instantanement (updates, insert)
    except Exception as e:
        print_error(f"Erreur dans la connexion à la base de données MySQL: '{e}'")
    
    return db

def db_insert(db: pymysql.connect, query: str, parameter: tuple) -> int:
    """Insert request to a MySQL database.

    Args:
        db (pymysql.connect): MySQL connection instance.
        query (str): MySQL query.
        parameter (tuple): MySQL query parameters.

    Returns:
        int: MySQL request result.
    """
    
    query = check_type(query, str)
    cur = db.cursor()
    
    try:
        cur.execute(query, parameter)   
        db.commit()
        r = cur.lastrowid
    except Exception as e:
        r = -1
        db.rollback()
        print_error(f"Erreur dans la requête SQL INSERT: '{query}'")
        
    return r

def db_update(db: pymysql.connect, query: str, parameter: tuple) -> int:
    """Update request to a MySQL database.

    Args:
        db (pymysql.connect): MySQL connection instance.
        query (str): MySQL query.
        parameter (tuple): MySQL query parameters.

    Returns:
        int: MySQL request result.
    """    
    
    query = check_type(query, str)
    cur = db.cursor()
    
    try:
        r = cur.execute(query, parameter)
        db.commit()
    except Exception as e:
        r = -1
        db.rollback()
        print_error(f"Erreur dans la requête SQL UPDATE: '{query}'")
        
    return r

def db_delete(db: pymysql.connect, query: str, parameter: tuple) -> int:
    """Delete request to a MySQL database.

    Args:
        db (pymysql.connect): MySQL connection instance.
        query (str): MySQL query.
        parameter (tuple): MySQL query parameters.

    Returns:
        int: MySQL request result.
    """    
    
    query = check_type(query, str)
    cur = db.cursor()
    
    try:
        cur.execute(query, parameter)   
        db.commit()
        r=1
    except Exception as e:
        r = -1
        db.rollback()
        print_error(f"Erreur dans la requête SQL DELETE: '{query}'")
        
    return r

def db_query(db: pymysql.connect, query: str, parameter: tuple, get_one: bool = False) -> list:
    """Query request to a MySQL database.

    Args:
        db (pymysql.connect): MySQL connection instance.
        query (str): MySQL query.
        parameter (tuple): MySQL query parameters.
        get_one (bool): If True, return only the first result.

    Returns:
        list: MySQL request results.
    """
    
    query = check_type(query, str)
    cur = db.cursor()
    
    try :
        cur.execute(query, parameter)
        
        if check_type(get_one, bool):
            r = cur.fetchone()
        else:
            r = cur.fetchall()
    except Exception as e:
        r = -1
        print_error(f"Erreur dans la requête SQL SELECT: '{query}'")
        
    return r