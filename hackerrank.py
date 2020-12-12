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

def birthday(s, d, m):
    # Challenge name: Sub-array Division
    # Challenge problem statment: https://www.hackerrank.com/challenges/the-birthday-bar/problem
    elements_constraint = all(1 <= bar <= 5 for bar in s) 
    if ((1 <= len(s) <= 100) and (1 <= d <= 31) and (1 <= m <= 12) and (elements_constraint)):
        ways = 0

        for i in range(len(s)):
            sum_of_bars = s[i]
            for j in range(i + 1, i + m):
                if (j < len(s)):
                    sum_of_bars += s[j]
            
            if (sum_of_bars == d):
                ways += 1

        return ways

def divisibleSumPairs(n, k, ar):
    # Challenge name: Divisible Sum Pairs
    # Challenge problem statment: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
    elements_constraint = all(1 <= a <= 100 for a in ar) 
    if ((2 <= n <= 100) and (1 <= k <= 100) and (elements_constraint)):
        pairs = 0

        for i in range(len(ar)):
            for j in range(i + 1, len(ar)):
                if (ar[i] + ar[j]) % k == 0:
                    pairs += 1
        
        return pairs

def migratoryBirds(arr):
    # Challenge name: Migratory Birds
    # Challenge problem statment: https://www.hackerrank.com/challenges/migratory-birds/problem
    freq = [0, 0, 0, 0, 0] # Denoting [Type 1, Type 2, Type 3, Type 4, Type 5]
    if (5 <= len(arr) <= 2*10**5):
        for bird in arr:
            freq[bird - 1] += 1
        
        return freq.index(max(freq)) + 1

def dayOfProgrammer(year):
    # Challenge name: Day of the Programmer
    # Challenge problem statment: https://www.hackerrank.com/challenges/day-of-the-programmer/problem
    if 1700 <= year <= 2700:
        total_days = 243
        
        if 1700 <= year <= 1917: # Julian Calander
            if year % 4 == 0:
                print(year, "is a Leap Year")
                total_days += 1
        elif (1919 <= year <= 2700): # Gregorian Calander
            if (year % 4) == 0:
                if (year % 100) == 0:
                    if (year % 400) == 0:
                        print(year, "is a leap year")
                        total_days += 1
                    else:
                        print(year, "is not a leap year")
                else:
                    print(year, "is a leap year")
                    total_days += 1
            else:
                print(year, "is not a leap year")
        else: # Transition peroid
            total_days -= 13

        return "{}.09.{}".format(256 - total_days, month, year)

def bonAppetit(bill, k, b):
    # Challenge name: Bill Division
    # Challenge problem statment: https://www.hackerrank.com/challenges/bon-appetit/problem
    bill_constraint = all(0 <= b <= 10**4 for b in bill)
    bill_sum = sum(bill)
    
    if (2 <= len(bill) <= 10**5) and (0 <= k < len(bill)) and bill_constraint and (0 <= b <= bill_sum):
        s = 0
        for i in range(len(bill)):
            if (i != k):
                s += bill[i]
        
        b_actual = s // 2

        if b_actual == b:
            print("Bon Appetit")
        else:
            print(b - b_actual)

def pageCount(n, p):
    # Challenge name: Drawing Book
    # Challenge problem statment: https://www.hackerrank.com/challenges/drawing-book/problem
    if (1 <= n <= 10**5) and (1 <= p <= n):

        if (p == n // 2):
            return n // 4

        if p == n:
            return 0
        
        if p == n - 1:
            return 1
        
        if (p > n // 2):
            return n // 2 - p // 2

        if (p < n // 2):
            return p // 2 

def countingValleys(steps, path):
    # Challenge name: Counting Valleys
    # Challenge problem statment: https://www.hackerrank.com/challenges/counting-valleys/problem
    path.strip()
    seaLevel = valley = 0

    for p in path:
        if p == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1
        
        if p == 'U' and seaLevel == 0:
            valley += 1
    
    return valley

def extraLongFactorials(n):
    # Challenge name: Extra Long Factorials
    # Challenge problem statment: https://www.hackerrank.com/challenges/extra-long-factorials/problem
    result = 1
    
    for i in range(n, 1, -1):
        result *= i

    print(result)

def climbingLeaderboard(ranked, player):
    # Challenge name: Climbing the Leaderboard
    # Challenge problem statment: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
    scores_set = list(set(ranked))
    scores_set.sort(reverse=True)
    result = []
    l = len(scores_set)
    for s in player:
        while (l > 0) and (s >= scores_set[l - 1]):
            l -= 1
        result.append(l + 1)
    return result

def hurdleRace(k, height):
    # Challenge name: The Hurdle Race
    # Challenge problem statment: https://www.hackerrank.com/challenges/the-hurdle-race/problem
    result = max(height) - k
    return max(0, result)

def designerPdfViewer(h, word):
    # Challenge name: Designer PDF Viewer
    # Challenge problem statment: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
    word = word.lower()
    ascii_list = [h[ord(l) - 97] for l in word]
    return max(ascii_list) * len(word)


def utopianTree(n):
    # Challenge name: Utopian Tree
    # Challenge problem statment: https://www.hackerrank.com/challenges/utopian-tree/problem    
    # if n % 2 == 0:
    #     return abs((n * 2) - 1)
    # if n % 2 != 0:
    #     return abs((((n - 1) * 2) - 1) * 2)
    if n % 2 == 0:
        return int(max(1, 2 ** ((n / 2) + 1) - 1))
    if n % 2 != 0:
        return int(max(1, 2 ** ((n + 3) / 2) - 2))

if __name__ == "__main__":
    pass