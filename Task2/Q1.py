def solve(n): 
   if n <= 2: 
      return n - 1 
   else: 
      return solve(n - 1) + solve(n - 2)

def isfibonacci(n):
    a = 0
    b = 1
    while a <= n:
        if n == a:
            return True
        a, b = b, a + b
    return False

def nearestFibonacci(n):
    if (n == 0):
        return 0
    first = 0
    second = 1
    third = first + second
    while third <= n:
        first = second
        second = third
        third = first + second
    if abs(third - n) >= abs(second - n):
        ans = second
    else:
        ans = third
    return ans

if __name__:
    n = int(input("Enter the number: "))
    nth = solve(n)
    print("The " + str(n) +"th number in the fibonacci sequence for is: " + str(nth))


    n = int(input("Enter the number: "))
    
    isfib = isfibonacci(n)
    nearestdib = nearestFibonacci(n)
    if isfib:
        print(str(n) + " is a fibonancci number")
    else:
        print(str(n) + " is not a fibonancci number and closed fibonnancci number is " + str(nearestdib))


