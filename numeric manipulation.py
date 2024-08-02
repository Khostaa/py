#%%
# number manipulation with numpy
import numpy as np

X = np.array([1, 2, 3, 4])

m = 2
c = 3
y = m * X + c
print(y) # O/p = [5 7 9 11]


#%%
# Plotting the graph with matplotlib
import matplotlib.pyplot as plt

# line plot with matplotlib
plt.plot(X, y)
plt.title("Line Plot: X vs Y")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#%%
# Scatter plot with matplotlib
import matplotlib.pyplot as plt
plt.scatter(X, y)
plt.title("Scatter Plot: X vs Y")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#%%
import numpy as np
y = np.array([3,6, 5, 7])

print(f"Original Array: {y} with dimension {y.shape}")


# Reshaping a 1D array into 2D array with 2 elements each
z = y.reshape(2,2)
print(f"After reshaping to 2D array with 2 elements each: {z} with dimension {z.shape} ") # [[3 6][5 7]]
# Reshaping back to original form
print(f"Back to original form: {y.reshape(-1)}")

# %%
