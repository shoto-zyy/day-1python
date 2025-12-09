import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Simple Flower Drawing 🌸")

# Create figure
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_aspect('equal')
ax.axis('off')

# Draw petals
theta = np.linspace(0, 2 * np.pi, 100)

for i in range(6):
    angle = i * np.pi / 3
    x = 0.5 * np.cos(theta) + 0.7 * np.cos(angle)
    y = 0.5 * np.sin(theta) + 0.7 * np.sin(angle)
    ax.fill(x, y, color='pink')

# Draw center
center_theta = np.linspace(0, 2 * np.pi, 100)
xc = 0.3 * np.cos(center_theta)
yc = 0.3 * np.sin(center_theta)
ax.fill(xc, yc, color='yellow')

st.pyplot(fig)
