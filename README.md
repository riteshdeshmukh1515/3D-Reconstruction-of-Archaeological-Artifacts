# 3D Reconstruction of Archaeological Artifacts

This project demonstrates a simple yet effective method to reconstruct and visualize 3D depth maps of archaeological artifacts using image processing and dimensionality reduction techniques. It provides an interactive way to transform 2D images of artifacts into 3D surface models using Singular Value Decomposition (SVD) and Plotly for visualization.

## Features

- GUI-based image selection for ease of use  
- Grayscale conversion and edge detection to highlight structural details  
- Dimensionality reduction using SVD to reconstruct core image features  
- 3D mesh generation with normalized depth mapping  
- Interactive 3D surface plot rendered in a browser with Plotly  

## Technologies Used

- Python 3  
- OpenCV for image processing  
- NumPy for numerical computation  
- Tkinter for file dialog  
- Plotly for 3D plotting and visualization  

## How It Works

1. The user selects an image of an artifact using a GUI file dialog.  
2. The image is converted to grayscale and processed to detect edges.  
3. Singular Value Decomposition (SVD) is applied to the edge image for dimensionality reduction.  
4. A 3D mesh is created using the reduced data.  
5. The result is displayed as an interactive 3D surface plot in the browser.  

## Use Case

This approach can be used in heritage preservation and virtual museum applications where partial or degraded images of artifacts can be analyzed to reconstruct and visualize their potential 3D structure.
