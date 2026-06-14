


import random
import pygame

# Growth animation speed in milliseconds
GROWTH_SPEED = 500

def check_collision(bigger: dict, smaller: dict) -> bool:
    
    if bigger["size"] <= smaller["size"]:
        return False

    bx = bigger["x"] + bigger["size"] / 2
    by = bigger["y"] + bigger["size"] / 2
    sx = smaller["x"] + smaller["size"] / 2
    sy = smaller["y"] + smaller["size"] / 2
    dist = ((bx - sx) ** 2 + (by - sy) ** 2) ** 0.5
    # returns true in case of collision
    
    return dist < (bigger["size"] + smaller["size"]) / 2



def calculate_distance(pos1: tuple[float, float], pos2: tuple[float, float]) -> float:
    """Calculate the distance between two positions."""
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    return (dx**2 + dy**2) ** 0.5



def is_close_enough(square1: dict, square2: dict, radius: float) -> bool:
    x1 = square1["x"] + square1["size"] / 2
    y1 = square1["y"] + square1["size"] / 2

    x2 = square2["x"] + square2["size"] / 2
    y2 = square2["y"] + square2["size"] / 2

    dx = x1 - x2
    dy = y1 - y2

    distance = (dx * dx + dy * dy) ** 0.5

    return distance <= radius


def flee_away(small_square: dict, big_square: dict) -> None:
    """
    Update the small square's velocity to move away from the big square.
    TODO: Change small_square's direction away from big_square.
    """
    small_pos = (small_square["x"] + small_square["size"] / 2, small_square["y"] + small_square["size"] / 2)
    big_pos = (big_square["x"] + big_square["size"] / 2, big_square["y"] + big_square["size"] / 2)

    dx = small_pos[0] - big_pos[0]
    dy = small_pos[1] - big_pos[1]

    distance = calculate_distance(small_pos, big_pos)
    if distance == 0:
        return

    norm_dx = dx / distance
    norm_dy = dy / distance

    speed = ((MAX_SIZE - small_square["size"]) / (MAX_SIZE - MIN_SIZE)) * (MAX_SPEED - 1) + 1
    small_square["vx"] = norm_dx * speed
    small_square["vy"] = norm_dy * speed


"""Dictionary-based Pygame demo: 10 squares move randomly on a canvas.

This version uses dictionaries instead of classes/dataclasses.
"""


def is_expired(square: dict) -> bool:
    current_time = pygame.time.get_ticks()
    return current_time - square["created_at"] > square["lifespan"]


def chase_towards(bigger_square, smaller_square):
    # move bigger square towards smaller square
    bigger_pos = (bigger_square["x"] + bigger_square["size"] / 2,
                  bigger_square["y"] + bigger_square["size"] / 2)
    smaller_pos = (smaller_square["x"] + smaller_square["size"] / 2,
                   smaller_square["y"] + smaller_square["size"] / 2)

    dx = smaller_pos[0] - bigger_pos[0]
    dy = smaller_pos[1] - bigger_pos[1]

    distance = calculate_distance(bigger_pos, smaller_pos)
    if distance == 0:
        return

    norm_dx = dx / distance
    norm_dy = dy / distance

    base_speed = ((MAX_SIZE - bigger_square["size"]) / (MAX_SIZE - MIN_SIZE)) * (MAX_SPEED - 1) + 1
    speed = base_speed * 1.1  # chase boost

    bigger_square["vx"] = norm_dx * speed
    bigger_square["vy"] = norm_dy * speed


# Window and simulation constants
WIDTH = 800
HEIGHT = 600
FPS = 100
SQUARE_COUNT = 25
MIN_SIZE = 20
MAX_SIZE = 80
MAX_SPEED = 8
BACKGROUND_COLOR = (25, 25, 35)
SQUARE_LIFESPAN = 1000



def random_color() -> tuple[int, int, int]:
    """Return a random RGB color."""
    return (
        random.randint(80, 255),
        random.randint(80, 255),
        random.randint(80, 255),
    )


def create_square() -> dict:
    """Create one square as a dictionary."""
    size = random.randint(MIN_SIZE, MAX_SIZE)
    created_at = pygame.time.get_ticks()
    lifespan = random.randint(500, 10000)

    x = random.uniform(0, WIDTH - size)
    y = random.uniform(0, HEIGHT - size)

    speed = ((MAX_SIZE - size) / (MAX_SIZE - MIN_SIZE)) * (MAX_SPEED - 1) + 1
    vx = random.choice([-1, 1]) * speed
    vy = random.choice([-1, 1]) * speed

    return {
        "x": x,
        "y": y,
        "vx": vx,
        "vy": vy,
        "size": size,
        "color": random_color(),
        "created_at": created_at,
        "lifespan": lifespan,
    }



def create_squares(count: int) -> list[dict]:
    return [create_square() for _ in range(count)]


def create_mixed_squares():
    squares = []
    # 5 squares of size 25
    for i in range(5):
        sq = create_square()
        sq["size"] = 25
        squares.append(sq)
    # 10 squares of size 10
    for i in range(10):
        sq = create_square()
        sq["size"] = 10
        squares.append(sq)
    # 30 squares of size 4
    for i in range(30):
        sq = create_square()
        sq["size"] = 4
        squares.append(sq)
    return squares


def update_square(square: dict) -> None:
    square["x"] += square["vx"]
    square["y"] += square["vy"]

    # Screen wrapping horizontally
    if square["x"] + square["size"] < 0:
        square["x"] = WIDTH
    elif square["x"] > WIDTH:
        square["x"] = -square["size"]

    # Screen wrapping vertically
    if square["y"] + square["size"] < 0:
        square["y"] = HEIGHT
    elif square["y"] > HEIGHT:
        square["y"] = -square["size"]


def draw_square(screen: pygame.Surface, square: dict) -> None:
    pygame.draw.rect(
        screen,
        square["color"],
        pygame.Rect(
            int(square["x"]),
            int(square["y"]),
            int(square["size"]),
            int(square["size"]),
        ),
    )


def handle_events() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True



def run() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mixed Size Squares (Dictionary Version)")
    clock = pygame.time.Clock()

    squares = create_mixed_squares()

    font = pygame.font.SysFont("Arial", 20)  # FIXED: moved outside loop

    running = True

    while running:
        running = handle_events()

        new_squares = []
        for square in squares:
            if not is_expired(square):
                new_squares.append(square)

        while len(new_squares) < SQUARE_COUNT:
            new_squares.append(create_square())

        squares = new_squares

        

        eaten_indices = set()
        respawn_list = []
        eaten_pairs = []
        for i, big in enumerate(squares):
            for j, small in enumerate(squares):
                if i == j:
                    continue
                if check_collision(big, small):
                    eaten_indices.add(j)
                    respawn_list.append(small["size"])
                    eaten_pairs.append((i, small["size"]))

        # Predator grows after eating, but animated over GROWTH_SPEED
        now = pygame.time.get_ticks()
        for predator_idx, prey_size in eaten_pairs:
            predator = squares[predator_idx]
            growth = 0.5 * prey_size
            target_size = min(predator["size"] + growth, MAX_SIZE)
            # Start animated growth
            predator["growth_start_size"] = predator["size"]
            predator["growth_target"] = target_size
            predator["growth_start_time"] = now

        # Animate growth for all squares with a growth_target
        for square in squares:
            if "growth_target" in square:
                start_size = square["growth_start_size"]
                target_size = square["growth_target"]
                start_time = square["growth_start_time"]
                elapsed = now - start_time
                if elapsed >= GROWTH_SPEED:
                    square["size"] = target_size
                    del square["growth_target"]
                    del square["growth_start_size"]
                    del square["growth_start_time"]
                else:
                    t = elapsed / GROWTH_SPEED
                    square["size"] = start_size + (target_size - start_size) * t
                # Adjust speed: bigger = slower
                speed = ((MAX_SIZE - square["size"]) / (MAX_SIZE - MIN_SIZE)) * (MAX_SPEED - 1) + 1
                v_norm = (square["vx"] ** 2 + square["vy"] ** 2) ** 0.5
                if v_norm != 0:
                    scale = speed / v_norm
                    square["vx"] *= scale
                    square["vy"] *= scale

        
        new_squares2 = []
        for idx, square in enumerate(squares):
            if idx not in eaten_indices:
                new_squares2.append(square)
        for orig_size in respawn_list:
            sq = create_square()
            sq["size"] = orig_size
            # Ensure respawned squares do not have growth state
            for k in ["growth_target", "growth_start_size", "growth_start_time"]:
                if k in sq:
                    del sq[k]
            new_squares2.append(sq)
        squares = new_squares2

        # Flee/chase logic (unchanged)
        for small in squares:
            for big in squares:
                if small is big:
                    continue
                if small["size"] < big["size"]:
                    if is_close_enough(small, big, 120):
                        flee_away(small, big)
                    elif is_close_enough(big, small, 200):
                        chase_towards(big, small)

        for square in squares:
            update_square(square)

        screen.fill(BACKGROUND_COLOR)

        for square in squares:
            draw_square(screen, square)

        fps = clock.get_fps()
        fps_text = font.render(f"FPS: {fps:.1f}", True, (255, 255, 255))
        count_text = font.render(f"Squares: {len(squares)}", True, (255, 255, 255))

        screen.blit(fps_text, (10, 10))
        screen.blit(count_text, (10, 30))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    run()