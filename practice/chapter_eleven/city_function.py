def city_country(city, country, population=''):
    '''接收名和姓并返回整洁的姓名
     :type city: char
     :type country: char
    '''
    if population:
        city_country = city + ', ' + country + ' - population ' + population 
    else
        city_country = city + ', ' + country
    return city_country.title()