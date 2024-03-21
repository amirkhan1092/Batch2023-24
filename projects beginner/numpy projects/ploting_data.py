import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Frame, Label, OptionMenu, StringVar

# Sample data loading and preprocessing
# Replace with your own dataset
np.random.seed(0)
data = np.random.randn(100, 2)  # Sample 2D data

# Matplotlib plot functions
def plot_line():
    plt.figure()
    # Plot line plot
    plt.plot(data[:, 0], data[:, 1])
    plt.title('Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

def plot_scatter():
    plt.figure()
    # Plot scatter plot
    plt.scatter(data[:, 0], data[:, 1])
    plt.title('Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

def plot_histogram():
    plt.figure()
    # Plot histogram
    plt.hist(data[:, 0], bins=20, color='skyblue', edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.show()

def plot_pie_chart():
    plt.figure()
    # Plot pie chart
    labels = ['Group 1', 'Group 2']
    sizes = [len(data[data[:, 0] > 0]), len(data[data[:, 0] <= 0])]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Pie Chart')
    plt.show()

# GUI setup
root = Tk()
root.title('Data Visualization Dashboard')

# Frame for buttons
frame = Frame(root)
frame.pack(padx=10, pady=10)

# Label for plot selection
label = Label(frame, text='Select a plot:')
label.pack(side='left', padx=5)

# Dropdown menu for plot selection
plot_options = ['Line Plot', 'Scatter Plot', 'Histogram', 'Pie Chart']
selected_plot = StringVar()
selected_plot.set(plot_options[0])
plot_menu = OptionMenu(frame, selected_plot, *plot_options)
plot_menu.pack(side='left', padx=5)

# Button to generate selected plot
generate_button = Button(frame, text='Generate Plot', command=lambda: generate_plot(selected_plot.get()))
generate_button.pack(side='left', padx=5)

# Function to generate selected plot
def generate_plot(plot_type):
    if plot_type == 'Line Plot':
        plot_line()
    elif plot_type == 'Scatter Plot':
        plot_scatter()
    elif plot_type == 'Histogram':
        plot_histogram()
    elif plot_type == 'Pie Chart':
        plot_pie_chart()

# Run the GUI main loop
root.mainloop()
