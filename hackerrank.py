############
# Author: George Hanna
# Author's email: ghanna610@gmail.com
# © George Hanna
# This file serves as my HackerRank solutions progress.
############

import math
import re


def solveMeFirst(a,b):
    # Challenge name: Solve Me First
    # Challenge problem statment: https://www.hackerrank.com/challenges/solve-me-first/problem
    return a + b

def simpleArraySum(ar):
    # Challenge name: Simple Array Sum
    # Challenge problem statment: https://www.hackerrank.com/challenges/simple-array-sum/problem
    sum = 0
    for i in ar:
        sum += i
    return sum

def aVeryBigSum(ar):
    # Challenge name: A Very Big Sum
    # Challenge problem statment: https://www.hackerrank.com/challenges/a-very-big-sum/problem
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
    # Challenge name: Diagonal Difference
    # Challenge problem statment: https://www.hackerrank.com/challenges/diagonal-difference/problem
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
    # Challenge name: Plus Minus
    # Challenge problem statment: https://www.hackerrank.com/challenges/plus-minus/problem
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
    # Challenge name: Staircase
    # Challenge problem statment: https://www.hackerrank.com/challenges/staircase/problem
    if (0 < n <= 100):
        for i in range(n):
            print((' ' * (n - i - 1)) + '#' * (i + 1))
    else:
        return

def miniMaxSum(arr):
    # Challenge name: Mini-Max Sum
    # Challenge problem statment: https://www.hackerrank.com/challenges/mini-max-sum/problem
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
    # Challenge name: Birthday Cake Candles
    # Challenge problem statment: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
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
    # Challenge name: Time Conversion
    # Challenge problem statment: https://www.hackerrank.com/challenges/time-conversion/problem
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
    # Challenge name: Compare the Triplets
    # Challenge problem statment: https://www.hackerrank.com/challenges/compare-the-triplets/problem
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
    # Challenge name: Grading Students
    # Challenge problem statment: https://www.hackerrank.com/challenges/grading/problem
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
    # Challenge name: Apple and Orange
    # Challenge problem statment: https://www.hackerrank.com/challenges/apple-and-orange/problem
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
    # Challenge name: Number Line Jumps
    # Challenge problem statment: https://www.hackerrank.com/challenges/kangaroo/problem
    if ((0 <= x1 < x2 <= 10000) and (1 <= v1 <= 10000) and (1 <= v2 <= 10000)):
        if (v1 > v2 and ((x2 - x1) % (v1 - v2) == 0)):
            return "YES"
        return "NO"
    else:
        return

def pangrams(s):
    # Challenge name: Pangrams
    # Challenge problem statment: https://www.hackerrank.com/challenges/pangrams/problem
    if ( 0 < len(s) <= 10**3):
        s = s.lower().split()
        s = ''.join(s)
        ascii_set = set([ord(l) for l in s])

        if (len(ascii_set) == 26):
            return "pangram"
        else:
            return "not pangram"
    else:
        return

def minimumNumber(n, password):
    # Challenge name: Strong Password
    # Challenge problem statment: https://www.hackerrank.com/challenges/strong-password/problem
    if (1 <= n <= 100):
        count = 0

        if (not re.search('[a-z]', password)):
            count += 1
        if (not re.search('[A-Z]', password)):
            count += 1
        if (not re.search('[0-9]', password)):
            count += 1
        if (not re.search('[!@#$%^&*()-+]', password)):
            count += 1

        return max(count, 6 - n)
        
    else:
        return

def breakingRecords(scores):
    # Challenge name: Breaking the Records
    # Challenge problem statment: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
    elements_constraint = all(0 <= score <= 10**8 for score in scores) 
    if ((1 <= len(scores) <= 1000) and elements_constraint):
        changes = [0, 0]
        max_score, min_score = scores[0], scores[0]
        
        for i in range(1, len(scores)):
            if (scores[i] < min_score):
                min_score = scores[i]
                changes[1] += 1
            elif ((scores[i] > max_score)):
                max_score = scores[i]
                changes[0] += 1
            else:
                continue

        return changes
        
if __name__ == "__main__":
    pass
