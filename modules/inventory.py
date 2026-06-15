######################################################################
# Title: Jeffer Einstein's Archipelago
# Assignment: Video Game
# Name: Stephen Huang & Syed Hussain
# Class: CS30
# Current Date: 6/15/2026
#######################################################################
'''
This code creates a player inventory system using the Inventory class.
'''
#######################################################################
import tabulate
from modules.type_write import *


class Inventory:
    """Represents a named inventory with a fixed number of item slots."""

    def __init__(self, name: str, inventory: int = 3):
        self.name = name  # Display name of the inventory
        # Initialise slots as EMPTY
        self.inventory = [[f"{i + 1}. EMPTY"] for i in range(inventory)]

    def __str__(self):
        return self.name

    def view_inventory(self):
        """Display the inventory contents as a formatted table."""
        type_write(f"{self.name}: ")
        print(tabulate.tabulate(self.inventory, tablefmt="fancy_grid"))
