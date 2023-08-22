def compute_triangle_area(len_side_a: float, len_side_b: float, len_side_c: float) -> float:
    """  
    Calculate area using heron's formula
    
    Args: 
        len_side_a (float): length of side A     
        len_side_b (float): length of side B     
        len_side_c (float): length of side C     
    
    Returns:
        area (float): Area of the triangle
    """
    perimeter = len_side_a + len_side_b + len_side_c
    semiperimeter = perimeter / 2 # semiperimeter in heron's formula 
    area = (semiperimeter * (semiperimeter - len_side_a) * (semiperimeter - len_side_b) * (semiperimeter - len_side_c)) ** 0.5

    return area