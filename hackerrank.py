import math
import re
import string


def solveMeFirst(a,b):
    return a + b

def simpleArraySum(ar):
    sum = 0
    for i in ar:
        sum += i
    return sum

def aVeryBigSum(ar):
    if (1 <= len(ar) <= 10):
        sum = 0
        applicable = True
        
        for a in ar:
            if (0 <= a <= 10**10):
                sum += a
            else:
                applicable = False
        
        if applicable:
            return sum
        else:
            return
    else:
        return

def diagonalDifference(arr):
    lr, rl, c = 0, 0, 1

    for i ,row in enumerate(arr):
        passed = True
        for col in row:
            if (-100 <= col <= 100 and passed):
                    lr += row[i]
                    rl += row[len(row) - c]
                    passed = False
            else:
                break
        c += 1

    return abs(lr - rl)

def plusMinus(arr):
    if (0 < len(arr) <= 100):
        pos, neg, zer = 0, 0, 0
        for i in arr:
            if (-100 <= i <= 100):
                if (i > 0):
                    pos += 1
                elif (i < 0):
                    neg += 1
                else:
                    zer += 1
            else:
                break
        size = len(arr)
        print("{:.6f}".format(pos / size))
        print("{:.6f}".format(neg / size))
        print("{:.6f}".format(zer / size))
    else:
        return

def staircase(n):
    if (0 < n <= 100):
        for i in range(n):
            print((' ' * (n - i - 1)) + '#' * (i + 1))
    else:
        return

def miniMaxSum(arr):
    arr.sort()
    min_sum, max_sum = 0, 0
    applicable = True

    for i ,a in enumerate(arr):
        if (1 <= a <= 10**9):
            if (i < len(arr) - 1):
                min_sum += a
            if (i != 0):
                max_sum += arr[len(arr) - i]
        else:
            applicable = False

    if applicable:
        print("{} {}".format(min_sum, max_sum))
    else:
        return

def birthdayCakeCandles(candles):
    candles.sort()
    if (1 <= len(candles) <= 10**5):
        tallest = candles[len(candles) - 1]
        count = 0
        applicable = True
        
        for candle in reversed(candles):
            if (1 <= candle <= 10**7): 
                if (candle == tallest):
                    count += 1
                else:
                    applicable = False
                    break

        if applicable:
            return count
        else:
            return
    else:
        return

def timeConversion(s):
    am = 'AM'
    pm = 'PM'

    m = s[len(s) - 2:].upper()
    h = s[:2]

    if (m == pm):
        hour = int(h)
        if (h != '12'):
            try:
                hour += 12
                return "{}{}".format(hour, s[2:len(s) - 2])
            except TypeError:
                print("Error")
        else:
            return "{}{}".format(hour, s[2:len(s) - 2])
    
    if (m == am and h == '12'):
        return "00{}".format(s[2:len(s) - 2])
    else:
        return "{}".format(s[:len(s) - 2])

def compareTriplets(a, b):
    result = [0, 0]
    for i in range(3):
        if ((1 <= a[i] <= 100) and (1 <= b[i] <= 100)):
            if a[i] > b[i]:
                result[0] = result[0] + 1
            elif (a[i] < b[i]):
                result[1] = result[1] + 1
            else:
                continue
        else:
            break
        
    return result 

def gradingStudents(grades):
    if (1 <= len(grades) <= 100):
        applicable = True

        for i ,grade in enumerate(grades):
            next_multiple = math.ceil(grade / 5) * 5
            
            if (0 <= grade <= 100):
                if (grade >= 38):
                    if (next_multiple - grade < 3):
                        grades[i] = next_multiple
            else:
                applicable = False

        return (grades if applicable else None)
    else:
        return

def countApplesAndOranges(s, t, a, b, apples, oranges):
    if ((1 <= s <= 10**5) and (1 <= t <= 10**5) and (1 <= a <= 10**5) 
            and (1 <= b <= 10**5) and (1 <= len(apples) <= 10**5) 
            and (1 <= len(oranges) <= 10**5) and (-10**5 <= s-t <= 10**5)
            and (a < s < t < b)):
        
        fa, fo = 0, 0

        for apple in apples:
            if (s <= apple + a <= t):
                fa += 1
        
        for orange in oranges:
            if (s <= orange + b <= t):
                fo += 1
        
        print(fa)
        print(fo)
    else:
        return

def kangaroo(x1, v1, x2, v2):
    if ((0 <= x1 < x2 <= 10000) and (1 <= v1 <= 10000) and (1 <= v2 <= 10000)):
        if (v1 > v2 and ((x2 - x1) % (v1 - v2) == 0)):
            return "YES"
        return "NO"
    else:
        return

def minimumNumber(n, password):
    if (1 <= n <= 100):
        count = 0

        if (not re.search('[a-z]', password)):
            print('Doesnt include lower case letters')
            count += 1
        if (not re.search('[A-Z]', password)):
            print('Doesnt include upper case letters')
            count += 1
        if (not re.search('[0-9]', password)):
            print('Doesnt include numbers')
            count += 1
        if (not re.search('[!@#$%^&*()+-]', password)):
            print('Doesnt include special case characters')
            count += 1

        if (count + n) < 6:
            count += 6 - (count + n)

        return count

    else:
        return

if __name__ == "__main__":
    print(minimumNumber(3, "Ab1"))
    print(minimumNumber(11, "#HackerRank"))
    print(minimumNumber(7, 'AUzs-nV'))
