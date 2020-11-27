# function to check if queen location is valid (not in the same column and not in the same diagonal)
def isValid(k):
    placement = True
    i = 1
    while i < k:
        if x[i-1] == x[k-1] or abs(x[i-1] - x[k-1]) == abs(i-k):
            placement = False
            break
        else:
            i += 1
    return placement

# function to find all possible N queens locations on N x N board
# Note: k is a row of the board
#       x[k] is a column of the board
def nQueens(x, k):
    stop = False
    while not stop:
        x[k-1] += 1
        while x[k-1] <= N and not isValid(k):
            x[k-1] += 1
        if x[k-1] <= N:
            if k == N:
                print("======== possible queens locations ========")
                print_board(x, len(x))
            else:
                nQueens(x, k+1)
        else:
            stop = True
            x[k-1] = 0

def print_board(x, N):
    for i in range(N):
        for k in range(len(x)):
            if k == x[i]-1:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()

# Main function to test the algorithm
if __name__ == '__main__':
    N = 4
    x = [0 for i in range(N)]
    print("N: ", N)
    nQueens(x, 1)
