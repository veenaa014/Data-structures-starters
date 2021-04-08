def sorted_matrix_search(mat, item):
    if len(mat) == 0:
        return None
    return bounds(mat, item, 0, len(mat[0]), 0, len(mat))

def bounds(mat, item, x1, x2, y1, y2):
    if x1 == x2 or y1 == y2:
        return None
    row, col = (y1 + y2)/2, (x1 + x2)/2
    middle = mat[row][col]
    if middle == item:
        return (row, col)
    if middle > item:
        found = bounds(mat, item, x1, col, y1, row) or \
                bounds(mat, item, col, col+1, y1, row) or \
                bounds(mat, item, x1, col, row, row+1)
        if found:
            return found
    else:
        found = bounds(mat, item, col+1, x2, row+1, y2) or \
                bounds(mat, item, col, col+1, row+1, y2) or \
                bounds(mat, item, col+1, x2, row, row+1)
        if found:
            return found
    return bounds(mat, item, x1, col, row+1, y2) or \
            bounds(mat, item, col+1, x2, y1, row)
