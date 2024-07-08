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
  
    expression = input("Enter a mathematical expression using 'x' as the variable: ")
    x = np.linspace(-10, 10, 1000)
    y = eval(expression)
    
    plot_type = input("Enter the type of plot (line/scatter): ")
    if plot_type == 'line':
        plt.plot(x, y)
    elif plot_type == 'scatter':
        plt.scatter(x, y)
    else:
        print("Invalid plot type. Defaulting to line plot.")
        plt.plot(x, y)
        
    plt.title("Plot of " + expression)
    plt.xlabel("x")
    plt.ylabel("y")
    
    return plt

if __name__ == "__main__":
    
    plt = plot_expression()
    plt.show()
    
    