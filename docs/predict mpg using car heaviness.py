import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LinearRegression

# 1. Fetch the REAL Auto MPG dataset from OpenML
print("Fetching real car data from the web...")
auto_mpg = fetch_openml(name='autoMpg', version=1, as_frame=True, parser='pandas')
df = auto_mpg.frame

# 2. Extract real features (Weight vs MPG)
# Note: Real weight in this dataset is in actual pounds, not thousands.
X_real_weight = df[['weight']].values  
y_real_mpg = df['class'].values

# 3. Train the model on raw, untouched real data
# Notice: No magic slope or noise numbers are provided here!
model = LinearRegression()
model.fit(X_real_weight, y_real_mpg)

# 4. Discover the mathematical truths found by Scikit-Learn
slope = model.coef_[0]
intercept = model.intercept_

print("\n--- RESULTS DISCOVERED BY AI ---")
print(f"Calculated Real Slope: {slope:.5f}")
print(f"Calculated Real Intercept: {intercept:.2f}")
print(f"Real Equation: y' = {slope:.5f}x + {intercept:.2f}")

# 5. Plot the real chaotic data points alongside the calculated line
plt.figure(figsize=(7, 4.5))
plt.scatter(X_real_weight, y_real_mpg, color='purple', alpha=0.5, label='Real Cars (Data Points)')

# Generate trend line coordinates
X_line = [[df['weight'].min()], [df['weight'].max()]]
y_line = model.predict(X_line)
plt.plot(X_line, y_line, color='gold', linewidth=3, label='Scikit-Learn Best Fit Line')

plt.title("Linear Regression on Real-World Vehicle Data")
plt.xlabel("Car Weight (Pounds)")
plt.ylabel("Fuel Efficiency (MPG)")
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()
