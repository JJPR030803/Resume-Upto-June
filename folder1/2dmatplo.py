import random
import matplotlib.pyplot as plt

# Step 2: Create 2D Data (Replace this with your actual data)
x = [random.uniform(0, 10) for _ in range(50)]
y = [random.uniform(0, 10) for _ in range(50)]

# Step 3: Plot the Data
plt.scatter(x, y, label='Data Points', color='blue')

# Step 4: Add Labels and Title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('2D Scatter Plot')

# Step 5: Show the Plot
plt.legend()  # Show legend if labels are used
plt.grid(True)  # Add a grid for better readability
plt.show()