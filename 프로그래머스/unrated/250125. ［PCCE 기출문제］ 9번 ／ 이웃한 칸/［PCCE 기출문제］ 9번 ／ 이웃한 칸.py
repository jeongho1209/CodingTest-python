def solution(board, h, w):
    answer = 0
    color = board[h][w]
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]
        if 0 <= h_check < len(board) and 0 <= w_check < len(board):
            if board[h_check][w_check] == color:
                answer += 1
    
    return answer