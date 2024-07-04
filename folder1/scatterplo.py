import matplotlib.pyplot as plt

# Step 2: Create Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Step 3: Plot the Data
plt.scatter(x, y)

# Step 4: Add Labels and Title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Simple Scatter Plot')

# Step 5: Show the Plot
plt.show()