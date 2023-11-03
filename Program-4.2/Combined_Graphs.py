import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

# Sample data
data = [2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 9]

# Set a larger figure size
plt.figure(figsize=(10, 7))

# Plot histogram
plt.subplot(2, 2, 1)
plt.hist(data, bins=5, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')

# Plot pie chart
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [10, 35, 45, 30, 5]

plt.subplot(2, 2, 2)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Pie Chart')

# Plot line graph
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.subplot(2, 2, 3)
plt.plot(x, y, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Graph')

# Generate data for the scatter plot
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

# Plot scatter plot
plt.subplot(2, 2, 4)
plt.scatter(x_scatter, y_scatter, color='green', marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')

# Set a larger font size for the super title
plt.suptitle('Combined Graphs in a single plot', fontsize=20)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()
# x axis values 
x = [1,2,3,4,5,6] 
# corresponding y axis values 
y = [2,4,1,5,2,6] 

plt.subplot(2, 2, 1)
# plotting the points 
plt.plot(x, y, color='blue', linestyle='dashed', linewidth = 1, 
		marker='o', markerfacecolor='red', markersize=10) 

# setting x and y axis range 
plt.ylim(1,8) 
plt.xlim(1,8) 

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 

# giving a title to my graph 
plt.title('Some cool customizations!') 

# function to show the plot 
plt.show()

# x-coordinates of left sides of bars  
left = [1, 2, 3, 4, 5] 
  
# heights of bars 
height = [10, 20, 30, 40, 50] 
  
# labels for bars 
tick_label = ['one', 'two', 'three', 'four', 'five'] 
plt.subplot(2, 2, 2)  
# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.4, color = ['blue', 'red']) 
  
# naming the x-axis 
plt.xlabel('x - axis') 
# naming the y-axis 
plt.ylabel('y - axis') 
# plot title 
plt.title('My bar chart!') 
# function to show the plot 
plt.show()


# Define x, y, and colors for each point
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
colors = ['red', 'green', 'blue', 'yellow', 'purple']
# Create a scatter plot with multiple colors
plt.scatter(x, y, c=colors)
# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter plot with Multiple Colours!')
# function to show the plot 
plt.show() 

style.use('ggplot')
# x-axis values
x = [5, 2 , 6 , 9, 4, 7 , 4]
# Y-axis values
y = [10, 5, 9 , 8, 4, 2 , 4 ]
# Function to plot
plt.plot(x,y,'o:c')
plt.title('Graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
# function to show the plot
plt.show()

#Subplot
x = np.array([0, 3, 5, 7])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 1, 1)
plt.plot(x,y,color="C8",marker = 'o',ms = 10, mfc = 'r')
#plot 2:
x = np.array([0, 3, 4, 5, 2, 8, 3, 5, 8, 3, 7, 12, 13, 35])
y = np.array([10, 50, 60, 70, 80, 20, 6, 33, 87, 24, 63, 31, 52, 67])
plt.title('SubPlot')
plt.subplot(2, 1, 2)
plt.scatter(x,y,marker = '*')
plt.show()
