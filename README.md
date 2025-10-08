# 3D Motion Capture Marker Visualization

This project visualizes 3D motion capture data with markers representing anatomical landmarks and skeletal connections. The Python code uses `matplotlib` to animate marker trajectories frame by frame, helping analyze human movement patterns or gait data.

## Features
- 3D scatter plot of motion capture markers
- Labels for anatomical landmarks
- Skeletal lines connecting markers to represent bones
- Animated frame-by-frame visualization
- Easy to adapt to different marker sets or datasets

## Requirements
- Python 3.x
- numpy
- matplotlib

## How to Use
1. Save your motion capture data in `.npy` format with shape `(frames, markers, 3)`.
2. Update the `MARKERS` list with your marker names.
3. Run `3D_Marker_Visualization.py`.
4. The 3D animation will appear showing marker movements and skeletal connections.

## Author
[Alireza Ghoraishian] – Master’s student in Medical Engineering (Medical Robotics), FAU
