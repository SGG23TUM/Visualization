import json
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.image as mpimg


color_map = {
        "ceiling": "skyblue",
        "lighting": "gold",
        "speaker": "lightgrey",
        "wall": "sandybrown",
        "door": "darkgreen",
        "smoke alarm": "lightpink",
        "floor": "burlywood",
        "trash bin": "darkslategray",
        "elevator button": "khaki",
        "escape sign": "orange",
        "board": "mediumpurple",
        "fire extinguisher": "red",
        "door sign": "navy",
        "light switch": "yellowgreen",
        "emergency button": "crimson",
        "elevator": "steelblue",
        "handrail": "rosybrown",
        "show window": "aquamarine",
        "pipes": "silver",
        "staircase": "sienna",
        "window": "lightblue",
        "radiator": "plum",
        "stecker": "olive"
    }

# Function to load JSON data from a file
def load_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to calculate the center of an object
def get_center(obj):
    return (obj['x'], obj['y'])

# Function to plot a node
def plot_node(ax, obj):
    center = get_center(obj)
    color = color_map.get(obj['name'], 'gray')  # Default to gray if not found in color_map
    ax.scatter(*center, color=color, s=100)
    ax.text(*center, obj['name'], color=color, ha='right', va='bottom')

# Function to plot a line between two nodes and add predicate text
def plot_line(ax, subj_center, obj_center, predicate):
    ax.plot([subj_center[0], obj_center[0]], [subj_center[1], obj_center[1]], color='black')
    mid_point = ((subj_center[0] + obj_center[0]) / 2, (subj_center[1] + obj_center[1]) / 2)
    ax.text(mid_point[0], mid_point[1], predicate, color='purple', fontsize=8)

# Path to the JSON file and the background image
json_file_path = '8910.json'  # Change this to your JSON file path
image_file_path = 'test_image/IMG_8910.JPG'  # Change this to your image file path

# Load JSON data from the file
json_data = load_json_data(json_file_path)

# Creating the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Loading and displaying the background image with reduced opacity
img = mpimg.imread(image_file_path)
ax.imshow(img, alpha=0.55)  # Adjust alpha for opacity

# Iterating through the relationships to plot the nodes and lines
for relationship in json_data['relationships']:
    subject = relationship['subject']
    object_ = relationship['object']
    predicate = relationship['predicate']

    # Plotting the nodes
    plot_node(ax, subject)
    plot_node(ax, object_)

    # Plotting the line between nodes and adding predicate text
    plot_line(ax, get_center(subject), get_center(object_), predicate)

# Removing the axis labels and ticks
ax.axis('off')

# Displaying the plot
plt.show()