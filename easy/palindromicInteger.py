

N = int(input())

data = list(map(str, input().split()))
def isPalindromic(data):

    for d in data:
        if d[::-1] == d:
            return True
    return False

l = list()
for i in range(N):
    l.append( int(data[i]) >= 0)

if all(l) == False:
    print(False)
else:
    print(isPalindromic(data))



