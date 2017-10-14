def is_leap_year(year):
    four = year % 4
    hund = year % 100
    four_hund = year % 400

    if four == 0 and (four_hund == 0 or hund != 0):
        return True
    return False
