def colors(fore_color='white', back_color='black', link_color='green', visited_color='blue'):
    return fore_color, back_color, link_color, visited_color

test_vals = {'link_color':'red', 'back_color':'blue'}
print(colors(**test_vals))