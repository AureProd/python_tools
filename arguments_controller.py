#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#---------------------------------------
# gérer l'aide et les arguments des scripts
# 
# author : huet jb
#---------------------------------------

# importation des librairies python
import getopt
from datetime import datetime
from time import time
import sys
from .console_colors import ConsoleColors as bcolors
from .tools_functions import check_type, check_type_in_array, print_error

class Argument:
    """Cette class permet de définir un argument dans un script."""
    
    def __init__(self, letter: str, name: str, help_message: str, value_type: type = str, need_value: bool = False, default_value = None):
        """Constructor of the Argument class.

        Args:
            letter (str): Letter of the argument.
            name (str): Name of the argument.
            help_message (str): Help message of the argument.
            value_type (type, optional): Type of the argument. Defaults to str.
            need_value (bool, optional): Boolean is `False` if is optional. Defaults to False.
            default_value (_type_, optional): Default value of the argument. Defaults to None.
        """        
        
        self.letter = check_type(letter, str)
        self.name = check_type(name, str)
        self.help_message = check_type(help_message, str)
        self.value_type = check_type(value_type, type)
        self.need_value = check_type(need_value, bool)
        
        self.value = None
        if default_value is not None:
            self.value = check_type(default_value, value_type)
        elif value_type == bool:
            self.value = False

class ArgumentsManager:
    """Cette class permet de gérer les arguments dans les scripts"""    
    
    def __init__(self, script_description: str, array_of_args: list[Argument] = []) -> None:
        """Constructor of the ArgsManager class.

        Args:
            script_description (str): Description of the script.
            array_of_args (list[Argument], optional): Arguments array of script. Defaults to [].
        """        
        
        self.verb = False
        self.argv = sys.argv[1:]
        
        self.script_description = check_type(script_description, str)
        self.array_of_args: list[Argument] = check_type_in_array(array_of_args, Argument)
        
        self.time_start = time()
        self.timestamp = int(time())
        self.date_heure_today=datetime.now().strftime("%d/%m/%Y %H:%M:%S") # récupération de la date et heure du jour

        print(bcolors.YELLOW + "Horodatage : " + self.date_heure_today + bcolors.END) # affichage de l'horodatage

        self.__gestion_of_arguments()

    # fonction permettant d'afficher l'aide du script en console
    def print_help(self, error_message: str | None = None) -> None:
        """Function for print the help of the script.

        Args:
            error_message (str | None, optional): Message of the error. Defaults to None.
        """        
        
        if isinstance(error_message, str): 
            print_error(f"{error_message}\n", False)

        print(f"{bcolors.PURPLE}{bcolors.BOLD}USAGE: {self.script_description}{bcolors.END}")
        print(f'{bcolors.PURPLE}-v --verbose: Mode verbose permettant d\'afficher plus de logs{bcolors.END}')
        
        for argument in self.array_of_args:
            string_argument = f'-{argument.letter} --{argument.name}: {argument.help_message}'
            if argument.need_value:
                string_argument += f' (need value)'
            if argument.value is not None and argument.value_type != bool:
                string_argument += f' (default value: {argument.value})'
            
            print(f'{bcolors.PURPLE}{string_argument}{bcolors.END}')

        exit()      

    def __gestion_of_arguments(self) -> None:
        letter_string = "vh"
        name_array: list[str] = ["verbose", "help"]
        
        for argument in self.array_of_args:
            letter_string += argument.letter
            name_array += [argument.name]
            
            if argument.value_type != bool:
                letter_string += ":"
                name_array[len(name_array) - 1] += "="            
        
        try:
            opts, args = getopt.getopt(self.argv, letter_string, name_array)
        except getopt.GetoptError:
            self.print_help('Erreur dans les arguments')

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                self.print_help()
            elif opt in ("-v", "--verbose"):
                self.verb = True
                print(f'{bcolors.YELLOW}mode verbose actif{bcolors.END}')
            else:
                arg_is_used: bool = False
                for argument in self.array_of_args:
                    if opt in (f"-{argument.letter}", f"--{argument.name}"):
                        # check the type of arg variable
                        if argument.value_type == bool:
                            argument.value = True 
                        elif argument.value_type == datetime:
                            argument.value = datetime.fromtimestamp(int(arg))
                        else:
                            try:
                                argument.value = argument.value_type(arg)
                            except ValueError:
                                self.print_help(f'Erreur dans la valeur de l\'argument {opt}. Le type de l\'argument est {type(arg)} et il doit être {argument.value_type}')
                            
                        arg_is_used = True
                        break   

                if not arg_is_used: 
                    self.print_help('invalid option')
            
        for argument in self.array_of_args:
            if argument.need_value and argument.value is None:
                self.print_help(f'{argument.name} ne peux pas être null')
                
    def script_finisher(self):
        """Function for terminate the script"""
        
        total_time = time() - self.time_start # récupération et calcul du temps de récupération des données

        print(f"{bcolors.YELLOW}Temp d'éxécution : {total_time}s {bcolors.END}") # affichage de le compte rendu