def is_leap_year(year: int) -> bool:
    """ 
    Check if year is a leap year

    Args:
        year (int): any valid year

    returns:
        (bool): True if leap year; False if non-leap year
    """
    if ((year % 100) == 0 and (year % 400 != 0)) or (year % 4 != 0):
        return False
    else: 
        return True

