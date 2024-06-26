def pascal_triangle(n):
    """
        returns a list of integers representing the Pascal's
        triangle of n.
        Returns an empty list if n <= 0
        
         1
        1  1
       1  2  1
      1  3  3  1
     1  4  6  4  1
     [1]
     [1,1]
     [1,2,1]
    [1,3,3,1]
    [1,4,6,4,1]
    
    [[1]]
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    
    """
    if n <= 0:
        return []
    pascal_tri = [[1 for _ in range(i+1)] for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            pascal_tri[i][j] = pascal_tri[i-1][j-1] + pascal_tri[i-1][j]
    return pascal_tri
