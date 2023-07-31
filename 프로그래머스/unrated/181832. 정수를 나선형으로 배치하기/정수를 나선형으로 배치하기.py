def solution(n):
    x, y = 0, 0
    direction = 'right'
    lst = [[0 for _ in range(n)] for _ in range(n)]
    
    for num in range(1, n*n+1):
        lst[x][y] = num
        
        if direction == 'right':
            if y+1 == n or lst[x][y+1] != 0:
                direction = 'down'
                x += 1
            else:
                y += 1
            
        elif direction == 'down':
            if x+1 == n or lst[x+1][y] != 0:
                direction = 'left'
                y -= 1
            else:
                x += 1
            
        elif direction == 'left':
            if lst[x][y-1] != 0:
                direction = 'top'
                x -= 1
            else:
                y -= 1
            
        elif direction == 'top':
            if lst[x-1][y] != 0:
                direction = 'right'
                y += 1
            else:
                x -= 1
    return lst