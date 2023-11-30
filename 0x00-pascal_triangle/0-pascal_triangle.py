def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # first element in each row is always 1
        if triangle:
            last_row = triangle[-1]
            # Calculate the next row based on the previous row
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)  # last element in each row is always 1
        triangle.append(row)

    return triangle
