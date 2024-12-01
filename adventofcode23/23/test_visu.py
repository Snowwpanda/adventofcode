import numpy as np
import matplotlib
matplotlib.use("Agg")  # Use the 'Agg' backend
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading
from queue import Queue

def bfs_with_animation(grid, start, goal):
    fig, ax = plt.subplots()
    img = ax.imshow(grid, cmap='coolwarm')
    queue = Queue()

    def update_plot(frame):
        data = queue.get()
        img.set_array(data)
        ax.set_title(f"BFS Step: {frame}")

    def bfs_search(grid, start, goal, update_func, animation_interval):
        queue.put(grid.copy())  # Initial state
        visited = set()

        def get_neighbors(position, grid_shape):
            x, y = position
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            return [(i, j) for i, j in neighbors if 0 <= i < grid_shape[0] and 0 <= j < grid_shape[1]]

        def bfs(position):
            nonlocal grid, visited
            x, y = position
            if grid[x, y] == 0:  # Free space
                queue.put(grid.copy())  # Enqueue the updated grid
                visited.add(position)
                grid[x, y] = 2  # Mark as visited
                time.sleep(animation_interval)  # Simulate some computation time
                for neighbor in get_neighbors(position, grid.shape):
                    if neighbor not in visited:
                        bfs(neighbor)

        bfs(start)

    # Create a thread for BFS search
    bfs_thread = threading.Thread(target=bfs_search, args=(grid, start, goal, update_plot, 0.1))
    bfs_thread.start()

    # Create an animation
    ani = FuncAnimation(fig, update_plot, frames=range(100), interval=1000)

    # Show the plot
    plt.show()

# Example usage:
# Set up your grid, start, and goal
grid_size = (10, 10)
visualize = np.zeros(grid_size, dtype=int)
start_position = (0, 0)
goal_position = (9, 9)
visualize[start_position] = 1  # Mark start as a wall
visualize[goal_position] = 1   # Mark goal as a wall

# Call the function
bfs_with_animation(visualize, start_position, goal_position)

while True:
    pass