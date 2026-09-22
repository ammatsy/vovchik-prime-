def area_by_base_height(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("must be positive")
    return 0.5 * base * height