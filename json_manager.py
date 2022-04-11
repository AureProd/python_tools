#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#---------------------------------------
# permet de créer et gérer une base de données dans un fichier json
# 
# author : huet jb
#---------------------------------------

# importation des librairies python
from .console_colors import ConsoleColors as bcolors
from .tools_functions import check_type, check_type_in_array, print_error
import json
import os.path as file_manager
 
class JsonManager:
    """Cette class permet de gérer des fichiers JSON."""
    
    def __init__(self, file_path: str) -> None:
        """Constructeur de la classe JsonManager

        Args:
            file_path (str): chemin du fichier json
        """        
        
        self.file_path = check_type(file_path, str)
        
        if not file_manager.exists(self.file_path):
            print_error(f"{bcolors.RED}Le fichier \"{self.file_path}\" n'existe pas ou n'est pas un fichier.{bcolors.END}")
            
        if not self.file_path.endswith(".json"):
            print_error(f"{bcolors.RED}Le fichier \"{self.file_path}\" n'est pas un fichier json.{bcolors.END}") 
        
        # Opening JSON file
        file = open(self.file_path)
        
        self.datas = json.load(file)
 
        # Closing file
        file.close()
        
    def get_datas(self, file_type: type) -> list:
        """Fonction permettant de renvoyer le tableau de données avec un type particulier

        Args:
            file_type (type): type des données à renvoyer

        Returns:
            list: renvoie un tableau avec les données concernées
        """        
        
        return_datas = list()
        
        for index, data in enumerate(self.datas):
            return_datas.append(file_type(index, data))  
                
        return return_datas
        