import sys
# question A

def Q_B():
        
    userInput = input()
    data = userInput.split(' ')
    n, k = int(data[0]), int(data[1])

    table = table = [[0 for _ in range (n)] for _ in range (n)]
    
    for i in range (n):
        for j in range (n):
            if i == j:
                table[i][j] = k - (n-1) * (k//n)
            else:
                table[i][j] = (k//n)
    
    for row in table:
        print(' '.join(map(str,row)))
    
def main():
    Q_B()

if __name__ == "__main__":
    main()