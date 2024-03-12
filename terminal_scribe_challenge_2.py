class SquareDrawer:
    def __init__(self, size):
        self.size = size

    def draw_square(self):
        for _ in range(self.size):
            print('*' * self.size)

# Example usage:
size = 20
drawer = SquareDrawer(size)
drawer.draw_square()

    
    