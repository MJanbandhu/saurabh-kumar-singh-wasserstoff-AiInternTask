from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Add nodes
dot.node('A', 'Start')
dot.node('B', 'Upload Image')
dot.node('C', 'Run Segmentation')
dot.node('D', 'Extract Objects')
dot.node('E', 'Identify Objects')
dot.node('F', 'Extract Text')
dot.node('G', 'Summarize Attributes')
dot.node('H', 'Map Data')
dot.node('I', 'Visualize Results')
dot.node('J', 'End')

# Add edges
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'F')
dot.edge('F', 'G')
dot.edge('G', 'H')
dot.edge('H', 'I')
dot.edge('I', 'J')

# Render and save the flowchart
dot.format = 'png'
dot.render('flowchart')