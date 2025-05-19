import numpy as np
import cv2
from tkinter import Tk, filedialog
import plotly.graph_objs as go
import plotly.io as pio

# Ensure plotly opens in the browser
pio.renderers.default = "browser"

# GUI to select image file
Tk().withdraw()
file_path = filedialog.askopenfilename(title='Select Artifact Image',
                                       filetypes=[("Image files", "*.jpg *.png *.jpeg")])

# Load and convert to grayscale
img = cv2.imread(file_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Extract edges (for structure)
edges = cv2.Canny(gray, 50, 150)

# Apply SVD to edges for dimensional reduction
U, S, VT = np.linalg.svd(edges, full_matrices=False)
k = 50  # Adjustable value for detail
S_reduced = np.diag(S[:k])
edges_reconstructed = np.dot(U[:, :k], np.dot(S_reduced, VT[:k, :]))

# Create 3D meshgrid
X, Y = np.meshgrid(np.arange(edges.shape[1]), np.arange(edges.shape[0]))
Z = edges_reconstructed

# Normalize Z for better visualization (depth mapping)
Z_normalized = (Z - np.min(Z)) / (np.max(Z) - np.min(Z)) * 255  # Normalize to range [0, 255]

# Create mesh surface plot using Plotly
trace = go.Surface(
    z=Z_normalized,  # Z values representing depth
    x=X,  # X coordinates from meshgrid
    y=Y,  # Y coordinates from meshgrid
    colorscale='viridis',  # Color scale
    opacity=0.8
)

layout = go.Layout(
    title='3D Surface Plot of Reconstructed Object',
    scene=dict(
        xaxis_title='X Coordinate',
        yaxis_title='Y Coordinate',
        zaxis_title='Depth (Z)'
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

# Create the figure and show in browser
fig = go.Figure(data=[trace], layout=layout)
fig.show()