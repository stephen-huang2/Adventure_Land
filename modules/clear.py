######################################################################
# Title: Jeffer Einstein's Archipelago
# Assignment: Video Game
# Name: Stephen Huang & Syed Hussain
# Class: CS30
# Current Date: 6/15/2026
#######################################################################
'''This code allows for terminal refreshing.'''
#######################################################################
# Imports & Global Variables ------------------------------------------
import os
from subprocess import run


# Functions -----------------------------------------------------------
def clear():
    """Clear the terminal screen."""
    command = "cls" if os.name == "nt" else "clear"
    run(command, shell=True)
