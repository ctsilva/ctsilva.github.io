#!/usr/bin/env python3
"""
Generate missing network visualization diagrams for Week 13 slides.
Creates 8 conceptual diagrams using matplotlib and networkx.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import warnings
warnings.filterwarnings('ignore')

# Set default figure size for slides (1920x1080)
SLIDE_WIDTH = 19.2
SLIDE_HEIGHT = 10.8
DPI = 100

def setup_figure(title=""):
    """Create a figure with slide dimensions."""
    fig, ax = plt.subplots(figsize=(SLIDE_WIDTH, SLIDE_HEIGHT), dpi=DPI)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    if title:
        ax.set_title(title, fontsize=36, pad=20, weight='bold')
    return fig, ax

def save_figure(fig, filename):
    """Save figure to figs/week13/ directory."""
    output_path = f"figs/week13/{filename}"
    fig.savefig(output_path, bbox_inches='tight', dpi=DPI, facecolor='white')
    print(f"✓ Generated: {output_path}")
    plt.close(fig)

# ============================================================================
# 1. Friendship Network Example
# ============================================================================
def generate_friendship_network():
    """Simple friendship network with 4 people."""
    fig, ax = setup_figure()

    # Create network
    G = nx.Graph()
    nodes = ['John\n(25)', 'Jessica\n(22)', 'Paul\n(24)', 'Mandy\n(21)']
    edges = [('John\n(25)', 'Jessica\n(22)'),
             ('John\n(25)', 'Paul\n(24)'),
             ('Jessica\n(22)', 'Paul\n(24)'),
             ('Paul\n(24)', 'Mandy\n(21)')]

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # Layout
    pos = {
        'John\n(25)': (2, 7),
        'Jessica\n(22)': (8, 7),
        'Paul\n(24)': (5, 3),
        'Mandy\n(21)': (8, 3)
    }

    # Draw
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=3000,
                           edgecolors='steelblue', linewidths=3, ax=ax)
    nx.draw_networkx_edges(G, pos, width=3, edge_color='gray', ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=18, font_weight='bold', ax=ax)

    # Add title
    ax.text(5, 9.5, 'Friendship Network', ha='center', fontsize=32, weight='bold')

    save_figure(fig, 'friendship-network-example.png')

# ============================================================================
# 2. Force Diagram (Edge Attraction + Node Repulsion)
# ============================================================================
def generate_force_diagram():
    """Diagram showing edge attraction and node repulsion forces."""
    fig, ax = setup_figure()

    # Node positions
    node1_pos = (3, 5)
    node2_pos = (7, 5)
    node3_pos = (5, 7)

    # Draw nodes
    for pos in [node1_pos, node2_pos, node3_pos]:
        circle = Circle(pos, 0.4, color='lightblue', ec='steelblue', linewidth=3, zorder=10)
        ax.add_patch(circle)

    # Edge between node1 and node2 (connected)
    ax.plot([node1_pos[0], node2_pos[0]], [node1_pos[1], node2_pos[1]],
            'gray', linewidth=3, zorder=5)

    # Edge attraction (spring force) - green arrows pulling together
    ax.annotate('', xy=(4.5, 5), xytext=(3.5, 5),
                arrowprops=dict(arrowstyle='->', lw=4, color='green'))
    ax.annotate('', xy=(5.5, 5), xytext=(6.5, 5),
                arrowprops=dict(arrowstyle='->', lw=4, color='green'))
    ax.text(5, 5.7, 'Edge Attraction\n(Spring Force)', ha='center', fontsize=20,
            color='green', weight='bold')

    # Node repulsion (electric force) - red arrows pushing apart
    # Between node1 and node3
    ax.annotate('', xy=(2.8, 5.3), xytext=(3.5, 6.2),
                arrowprops=dict(arrowstyle='->', lw=4, color='red'))
    ax.annotate('', xy=(4.6, 7.2), xytext=(3.9, 6.5),
                arrowprops=dict(arrowstyle='->', lw=4, color='red'))

    # Between node2 and node3
    ax.annotate('', xy=(7.2, 5.3), xytext=(6.5, 6.2),
                arrowprops=dict(arrowstyle='->', lw=4, color='red'))
    ax.annotate('', xy=(5.4, 7.2), xytext=(6.1, 6.5),
                arrowprops=dict(arrowstyle='->', lw=4, color='red'))

    ax.text(5, 8.5, 'Node Repulsion\n(Electric Force)', ha='center', fontsize=20,
            color='red', weight='bold')

    # Title
    ax.text(5, 9.5, 'Force-Directed Layout: Forces', ha='center', fontsize=32, weight='bold')

    save_figure(fig, 'force-diagram.png')

# ============================================================================
# 3. Force-Directed Step 1: Random Initial Positions
# ============================================================================
def generate_force_step1():
    """Initial random node positions."""
    fig, ax = setup_figure()

    # Create network
    G = nx.karate_club_graph()

    # Random positions (seed for reproducibility)
    np.random.seed(42)
    pos = {node: (np.random.rand() * 8 + 1, np.random.rand() * 8 + 1)
           for node in G.nodes()}

    # Draw
    nx.draw_networkx_nodes(G, pos, node_color='lightgray', node_size=200,
                           edgecolors='gray', linewidths=1, ax=ax)
    nx.draw_networkx_edges(G, pos, width=1, edge_color='lightgray', alpha=0.5, ax=ax)

    # Title
    ax.text(5, 9.5, 'Step 1: Initial Random Positions', ha='center', fontsize=32, weight='bold')
    ax.text(5, 0.5, 'Nodes placed randomly - no structure visible yet',
            ha='center', fontsize=20, style='italic')

    save_figure(fig, 'force-step1-random.png')

# ============================================================================
# 4. Force-Directed Step 4: Converged/Final Layout
# ============================================================================
def generate_force_step4():
    """Final converged force-directed layout."""
    fig, ax = setup_figure()

    # Create network
    G = nx.karate_club_graph()

    # Force-directed layout
    pos = nx.spring_layout(G, seed=42, iterations=100)

    # Rescale positions to fit nicely
    pos = {node: (x * 7 + 5, y * 7 + 5) for node, (x, y) in pos.items()}

    # Draw with nice colors
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=300,
                           edgecolors='steelblue', linewidths=2, ax=ax)
    nx.draw_networkx_edges(G, pos, width=2, edge_color='gray', alpha=0.6, ax=ax)

    # Title
    ax.text(5, 9.5, 'Step 4: Converged Layout', ha='center', fontsize=32, weight='bold')
    ax.text(5, 0.5, 'Forces balanced - clusters and structure now visible',
            ha='center', fontsize=20, style='italic')

    save_figure(fig, 'force-step4-iterate.png')

# ============================================================================
# 5. Friendship Network with Visual Encodings
# ============================================================================
def generate_friendship_encoded():
    """Friendship network with multiple visual encodings."""
    fig, ax = setup_figure()

    # Create network
    G = nx.Graph()
    nodes = ['John', 'Jessica', 'Paul', 'Mandy']

    # Node attributes: (age, gender)
    node_attrs = {
        'John': (25, 'M'),
        'Jessica': (22, 'F'),
        'Paul': (24, 'M'),
        'Mandy': (21, 'F')
    }

    # Edge attributes: (messages, relationship_age)
    edges = [
        ('John', 'Jessica', {'messages': 150, 'old': True}),
        ('John', 'Paul', {'messages': 80, 'old': True}),
        ('Jessica', 'Paul', {'messages': 200, 'old': False}),
        ('Paul', 'Mandy', {'messages': 50, 'old': True})
    ]

    G.add_edges_from([(u, v) for u, v, _ in edges])

    # Layout
    pos = {'John': (2, 7), 'Jessica': (8, 7), 'Paul': (5, 3), 'Mandy': (8, 3)}

    # Draw edges with varying thickness and style
    for u, v, attrs in edges:
        width = attrs['messages'] / 30  # Scale thickness by messages
        style = 'solid' if attrs['old'] else 'dashed'
        nx.draw_networkx_edges(G, pos, [(u, v)], width=width,
                               style=style, edge_color='gray', ax=ax)

    # Draw nodes with size by age, color by gender
    for node in nodes:
        age, gender = node_attrs[node]
        size = age * 100  # Scale size by age
        color = 'lightblue' if gender == 'M' else 'lightpink'
        nx.draw_networkx_nodes(G, pos, [node], node_size=size,
                               node_color=color, edgecolors='black',
                               linewidths=2, ax=ax)

    # Labels
    nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold', ax=ax)

    # Legend
    legend_elements = [
        mpatches.Patch(color='lightblue', label='Male'),
        mpatches.Patch(color='lightpink', label='Female'),
        plt.Line2D([0], [0], color='gray', linewidth=3, label='Old Friendship', linestyle='solid'),
        plt.Line2D([0], [0], color='gray', linewidth=3, label='New Friendship', linestyle='dashed'),
    ]
    ax.legend(handles=legend_elements, loc='lower left', fontsize=16,
              title='Encodings', title_fontsize=18)

    # Title
    ax.text(5, 9.5, 'Encoded Network: Size=Age, Color=Gender, Thickness=Messages',
            ha='center', fontsize=26, weight='bold')

    save_figure(fig, 'friendship-network-encoded.png')

# ============================================================================
# 6. Fixed Layout Patterns
# ============================================================================
def generate_fixed_layout_patterns():
    """Show circular, linear, and grid layout patterns."""
    fig = plt.figure(figsize=(SLIDE_WIDTH, SLIDE_HEIGHT), dpi=DPI)

    # Create 3 subplots
    gs = fig.add_gridspec(1, 3, wspace=0.3)

    # Small graph
    G = nx.karate_club_graph().subgraph(range(10))

    # Circular layout
    ax1 = fig.add_subplot(gs[0])
    pos1 = nx.circular_layout(G)
    nx.draw_networkx(G, pos1, ax=ax1, node_color='lightblue',
                     node_size=300, with_labels=False, edge_color='gray', width=2)
    ax1.set_title('Circular Layout', fontsize=24, weight='bold', pad=20)
    ax1.axis('off')

    # Linear layout
    ax2 = fig.add_subplot(gs[1])
    pos2 = {i: (i, 0) for i in G.nodes()}
    nx.draw_networkx(G, pos2, ax=ax2, node_color='lightcoral',
                     node_size=300, with_labels=False, edge_color='gray', width=2)
    ax2.set_title('Linear Layout', fontsize=24, weight='bold', pad=20)
    ax2.axis('off')

    # Grid layout
    ax3 = fig.add_subplot(gs[2])
    grid_size = int(np.ceil(np.sqrt(len(G))))
    pos3 = {i: (i % grid_size, i // grid_size) for i in G.nodes()}
    nx.draw_networkx(G, pos3, ax=ax3, node_color='lightgreen',
                     node_size=300, with_labels=False, edge_color='gray', width=2)
    ax3.set_title('Grid Layout', fontsize=24, weight='bold', pad=20)
    ax3.axis('off')

    # Overall title
    fig.suptitle('Fixed Layout Patterns', fontsize=32, weight='bold', y=0.98)

    save_figure(fig, 'fixed-layout-patterns.png')

# ============================================================================
# 7. Directed Matrix Diagram
# ============================================================================
def generate_directed_matrix():
    """Directed graph matrix representation."""
    fig, ax = setup_figure()

    # Create a simple directed graph
    nodes = ['A', 'B', 'C', 'D']
    n = len(nodes)

    # Create matrix with some directed edges
    matrix = np.array([
        [0, 1, 1, 0],  # A -> B, A -> C
        [0, 0, 1, 0],  # B -> C
        [0, 0, 0, 1],  # C -> D
        [1, 0, 0, 0],  # D -> A
    ])

    # Draw matrix
    cell_size = 1.5
    start_x = 2.5
    start_y = 3

    # Draw cells
    for i in range(n):
        for j in range(n):
            x = start_x + j * cell_size
            y = start_y + (n - 1 - i) * cell_size

            if matrix[i, j] == 1:
                color = 'steelblue'
                alpha = 0.8
            else:
                color = 'white'
                alpha = 1.0

            rect = Rectangle((x, y), cell_size, cell_size,
                             facecolor=color, edgecolor='black',
                             linewidth=2, alpha=alpha)
            ax.add_patch(rect)

    # Row labels (FROM)
    for i, node in enumerate(nodes):
        y = start_y + (n - 1 - i) * cell_size + cell_size / 2
        ax.text(start_x - 0.3, y, node, ha='right', va='center',
                fontsize=24, weight='bold')

    # Column labels (TO)
    for j, node in enumerate(nodes):
        x = start_x + j * cell_size + cell_size / 2
        ax.text(x, start_y + n * cell_size + 0.3, node,
                ha='center', va='bottom', fontsize=24, weight='bold')

    # Axis labels
    ax.text(start_x - 1, start_y + n * cell_size / 2, 'FROM',
            ha='center', va='center', fontsize=26, weight='bold',
            rotation=90)
    ax.text(start_x + n * cell_size / 2, start_y + n * cell_size + 1, 'TO',
            ha='center', va='bottom', fontsize=26, weight='bold')

    # Title
    ax.text(5, 9.5, 'Directed Graph: Adjacency Matrix',
            ha='center', fontsize=32, weight='bold')
    ax.text(5, 1.5, 'Rows = FROM, Columns = TO, Filled cell = Edge exists',
            ha='center', fontsize=18, style='italic')

    save_figure(fig, 'directed-matrix.png')

# ============================================================================
# 8. Parallel Axes for Directed Graphs
# ============================================================================
def generate_parallel_axes():
    """Parallel axes representation of directed graph."""
    fig, ax = setup_figure()

    nodes = ['A', 'B', 'C', 'D']
    n = len(nodes)

    # Edges (from, to)
    edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'A')]

    # Draw two vertical axes
    left_x = 3
    right_x = 7

    # Left axis (FROM)
    ax.plot([left_x, left_x], [2, 8], 'k-', linewidth=3)
    ax.text(left_x, 8.5, 'FROM', ha='center', fontsize=26, weight='bold')

    # Right axis (TO)
    ax.plot([right_x, right_x], [2, 8], 'k-', linewidth=3)
    ax.text(right_x, 8.5, 'TO', ha='center', fontsize=26, weight='bold')

    # Node positions
    spacing = 6 / (n - 1)
    node_pos = {node: 2 + i * spacing for i, node in enumerate(nodes)}

    # Draw nodes on both axes
    for node, y in node_pos.items():
        # Left axis
        circle = Circle((left_x, y), 0.2, color='lightblue',
                        ec='steelblue', linewidth=2, zorder=10)
        ax.add_patch(circle)
        ax.text(left_x - 0.5, y, node, ha='right', va='center',
                fontsize=22, weight='bold')

        # Right axis
        circle = Circle((right_x, y), 0.2, color='lightcoral',
                        ec='darkred', linewidth=2, zorder=10)
        ax.add_patch(circle)
        ax.text(right_x + 0.5, y, node, ha='left', va='center',
                fontsize=22, weight='bold')

    # Draw edges
    for from_node, to_node in edges:
        y_from = node_pos[from_node]
        y_to = node_pos[to_node]
        ax.plot([left_x, right_x], [y_from, y_to],
                'gray', linewidth=2, alpha=0.6, zorder=5)

    # Title
    ax.text(5, 9.5, 'Parallel Axes: Directed Graph',
            ha='center', fontsize=32, weight='bold')

    save_figure(fig, 'parallel-axes.png')

# ============================================================================
# Main execution
# ============================================================================
if __name__ == '__main__':
    print("Generating network visualization diagrams...")
    print("=" * 60)

    generate_friendship_network()
    generate_force_diagram()
    generate_force_step1()
    generate_force_step4()
    generate_friendship_encoded()
    generate_fixed_layout_patterns()
    generate_directed_matrix()
    generate_parallel_axes()

    print("=" * 60)
    print("✓ All diagrams generated successfully!")
    print("\nGenerated files in figs/week13/:")
    print("  1. friendship-network-example.png")
    print("  2. force-diagram.png")
    print("  3. force-step1-random.png")
    print("  4. force-step4-iterate.png")
    print("  5. friendship-network-encoded.png")
    print("  6. fixed-layout-patterns.png")
    print("  7. directed-matrix.png")
    print("  8. parallel-axes.png")
