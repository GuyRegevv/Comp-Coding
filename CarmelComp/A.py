import sys
# question A

def Q_A():
    
    sum = 0

    userInput = input()
    data = userInput.split(' ')
    n, k = int(data[0]), int(data[1])

    for i in range (n):
        userInput = input()
        data = userInput.split(' ')
        l, r = int(data[0]), int(data[1])
        length = (r - l) + 1
        sum += length

    if (k > sum):
        return (sum - k)
    elif (sum % k) == 0: 
        return 0
    else:
        return k - (sum % k)
    
def main():
    print(Q_A())

if __name__ == "__main__":
    main()