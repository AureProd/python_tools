#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#---------------------------------------
# permet de gérer des fichier json
# 
# author : huet jb
#---------------------------------------

# importation des librairies python
from .console_colors import ConsoleColors as bcolors
from .tools_functions import check_type, print_error
import json
import os.path as file_manager
        
def getJsonFile(file_path: str) -> dict:
    """Cette fonction permet de récupérer un fichier json et de le retourner sous forme de dictionnaire

    Args:
        file_path (str): chemin vers le fichier json

    Returns:
        dict: dictionnaire contenant les données du fichier json
    """
    
    file_path = check_type(file_path, str)
    
    if not file_manager.exists(file_path):
        print_error(f"{bcolors.RED}Le fichier \"{file_path}\" n'existe pas ou n'est pas un fichier.{bcolors.END}")
        
    if not file_path.endswith(".json"):
        print_error(f"{bcolors.RED}Le fichier \"{file_path}\" n'est pas un fichier json.{bcolors.END}") 
    
    # Opening JSON file and get content
    with open(file_path) as json_file:
        datas = json.load(json_file)

    return datas
        