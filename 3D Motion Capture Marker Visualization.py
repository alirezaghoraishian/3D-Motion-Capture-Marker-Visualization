"""
3D Motion Capture Marker Visualization
Description: Visualizes 3D motion capture marker data with skeletal connections.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# ------------------------------
# Load motion capture data
# ------------------------------
data = np.load("1.npy")  # shape: (frames, markers, 3)

# ------------------------------
# Marker names
# ------------------------------
MARKERS = [
    'C7', 'LA', 'RA', 'REP', 'LEP', 'RUL', 'LUL',
    'RASIS', 'LASIS', 'RPSIS', 'LPSIS',
    'RGT', 'LGT', 'RLE', 'LLE',
    'RCA', 'LCA', 'RFM', 'LFM'
]

# ------------------------------
# Skeletal connections (bones)
# ------------------------------
BONES = [
    ('C7', 'LA'), ('C7', 'RA'),             # neck to shoulders
    ('LA', 'LEP'), ('RA', 'REP'),           # shoulders to elbows
    ('LEP', 'LUL'), ('REP', 'RUL'),         # elbows to wrists
    ('C7', 'RASIS'), ('C7', 'LASIS'),       # spine to pelvis
    ('RASIS', 'RPSIS'), ('LASIS', 'LPSIS'), # pelvis rectangle
    ('RPSIS', 'LPSIS'),
    ('RPSIS', 'RGT'), ('LPSIS', 'LGT'),     # pelvis to knees
    ('RGT', 'RLE'), ('LGT', 'LLE'),         # knees to ankles
    ('RLE', 'RCA'), ('RCA', 'RFM'),         # right foot
    ('LLE', 'LCA'), ('LCA', 'LFM'),         # left foot
]

# ------------------------------
# Setup figure and axes
# ------------------------------
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

def init_plot():
    """Initialize 3D axes limits."""
    ax.set_xlim(0, 2000)
    ax.set_ylim(0, 2000)
    ax.set_zlim(0, 2000)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    return []

def update_frame(frame):
    """Update function for animation."""
    ax.clear()
    ax.set_title(f"3D Marker Movement - Frame {frame}")
    ax.set_xlim(0, 2000)
    ax.set_ylim(0, 2000)
    ax.set_zlim(0, 2000)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    x = data[frame, :, 0]
    y = data[frame, :, 1]
    z = data[frame, :, 2]

    # Plot markers
    ax.scatter(x, y, z, c='blue', s=30)

    # Label markers
    for i, name in enumerate(MARKERS):
        ax.text(x[i], y[i], z[i], name, fontsize=7)

    # Draw skeletal lines
    for m1, m2 in BONES:
        try:
            i1 = MARKERS.index(m1)
            i2 = MARKERS.index(m2)
            ax.plot([x[i1], x[i2]], [y[i1], y[i2]], [z[i1], z[i2]], c='red', linewidth=2)
        except ValueError:
            continue  # skip if marker is missing

    return []

# ------------------------------
# Create animation
# ------------------------------
anim = animation.FuncAnimation(
    fig,
    update_frame,
    frames=range(0, len(data), 10),
    init_func=init_plot,
    blit=False,
    repeat=False
)

plt.show()
