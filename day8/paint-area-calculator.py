import math
wall_height = float(input("How tall is the wall"))
wall_width = float(input("How wide is the wall?"))

one_can_covers = 5


def paint_needed(height, width, coverage):
    return print(f"You will need {math.ceil((height * width) / coverage)} cans of paint.")


paint_needed(height=wall_height, width=wall_width, coverage=one_can_covers)
