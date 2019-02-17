def colors(fore_color='white', back_color='black', link_color='green', visited_color='blue'):
    return fore_color, back_color, link_color, visited_color


if __name__=='__main__':
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    #print(colors('purple', link_color='red', back_color='blue'))
    print(colors(*regular, **links))