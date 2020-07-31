if __name__ == '__main__':

    n = int(input())
    array= list(map(int, input().split()))

array.sort(reverse = True)

for i in range(n):
    if array[i]>array[i+1]:
       break
    
print(array[i+1])
