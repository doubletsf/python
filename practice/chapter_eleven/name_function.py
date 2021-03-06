def get_formatted_name(first, last,  middle=''):
    '''接收名和姓并返回整洁的姓名
     :type first: char
     :type middle: char
     :type last: char
    '''
    if middle:
        full_name = first + ' ' + middle + ' '+ last
    else:
        full_name = first + ' ' + last
    return full_name.title()
