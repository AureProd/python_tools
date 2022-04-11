#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#---------------------------------------
# tools for python script
# 
# author : huet jb
#---------------------------------------

from .console_colors import ConsoleColors as bcolors

def check_type(var, type_var: type, default_value = None): 
    """Function for check type of variable.

    Args:
        var (any): Variable to check.
        type_var (type): Type of the variable.
        default_value (any, optional): Default value of the variable if is `None`. Defaults to None.

    Returns:
        any: Return the variable.
    """     
     
    if (var is None) and (default_value is not None):
        return default_value 
        
    if not isinstance(var, type_var):
        print_error(f'Le type de la variable n\'est pas correct. Le type de la variable est {type(var)} et il doit être {type_var}')
    
    return var        
        
def check_type_in_array(array_of_var: list, type_var: type):
    """Function for check type of variable in array.

    Args:
        array_of_var (list[any]): Array of variable to check.
        type_var (type): Type of the variable.

    Returns:
        list[any]: Return the array of variable.
    """    
    
    if isinstance(array_of_var, list):
        for var in array_of_var:
            check_type(var, type_var)
            
        return array_of_var

def print_error(error_message: str, exit_after_print: bool = True, script_error: Exception | None = None) -> None:
    """Function for print error message.

    Args:
        error_message (str): Error message to print.
        exit_after_print (bool, optional): Booleand is True if the script exit after print. Defaults to True.
        script_error (Exception | None, optional): Exception of the script. Defaults to None.
    """    
    
    print(f"{bcolors.RED}{bcolors.BOLD}ERROR: {error_message}{bcolors.END}")
    
    if isinstance(script_error, Exception):
        error_line = script_error.__traceback__.tb_lineno
        print(f"{bcolors.RED}{bcolors.BOLD}Error Detail:{bcolors.END}{bcolors.RED} {script_error} (line: {error_line}){bcolors.END}")
    
    if exit_after_print:
        exit()