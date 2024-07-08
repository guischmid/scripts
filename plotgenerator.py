#author: gigi
#date : 2024-07-08
#version: 1.0
'''
This script asks the user for a mathematical expression and plots the graph of the expression.
It prompts the user to specify the type of plot (e.g., scatter plot or line plot) and other style options.
'''
import numpy as np
import matplotlib.pyplot as plt

import numpy as np

def plot_expression():
    """
    Plot a mathematical expression using 'x' as the variable.

    This function prompts the user to enter a mathematical expression and plots
    the graph of the expression using the values of 'x' ranging from -10 to 10.

    Parameters:
        None

    Returns:
        None
    """
    expression = input("Enter a mathematical expression using 'x' as the variable: ")
    x = np.linspace(-10, 10, 1000)
    y = eval(expression)
    
    