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
    return sum(ar)

def aVeryBigSum(ar):
    # Challenge name: A Very Big Sum
    # Challenge problem statment: https://www.hackerrank.com/challenges/a-very-big-sum/problem
    return sum(ar)    


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
    pos, neg, zer = 0, 0, 0
    for i in arr:
        if (i > 0):
            pos += 1
        elif (i < 0):
            neg += 1
        else:
            zer += 1

    size = len(arr)
    print("{:.6f}".format(pos / size))
    print("{:.6f}".format(neg / size))
    print("{:.6f}".format(zer / size))

def staircase(n):
    # Challenge name: Staircase
    # Challenge problem statment: https://www.hackerrank.com/challenges/staircase/problem
    for i in range(n):
        print((' ' * (n - i - 1)) + '#' * (i + 1))

def miniMaxSum(arr):
    # Challenge name: Mini-Max Sum
    # Challenge problem statment: https://www.hackerrank.com/challenges/mini-max-sum/problem
    arr.sort()
    min_sum, max_sum = 0, 0

    for i ,a in enumerate(arr):
        if (i < len(arr) - 1):
            min_sum += a
        if (i != 0):
            max_sum += arr[len(arr) - i]

    print("{} {}".format(min_sum, max_sum))

def birthdayCakeCandles(candles):
    # Challenge name: Birthday Cake Candles
    # Challenge problem statment: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
    candles.sort()
    tallest = candles[len(candles) - 1]
    count = 0

    for candle in reversed(candles):
        if (candle == tallest):
            count += 1

    return count

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
        if a[i] > b[i]:
            result[0] = result[0] + 1
        if (a[i] < b[i]):
            result[1] = result[1] + 1
        
    return result 

def gradingStudents(grades):
    # Challenge name: Grading Students
    # Challenge problem statment: https://www.hackerrank.com/challenges/grading/problem
    for i ,grade in enumerate(grades):
        next_multiple = math.ceil(grade / 5) * 5
        if (grade >= 38):
            if (next_multiple - grade < 3):
                grades[i] = next_multiple

    return grades

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Challenge name: Apple and Orange
    # Challenge problem statment: https://www.hackerrank.com/challenges/apple-and-orange/problem
    fa, fo = 0, 0

    for apple in apples:
        if (s <= apple + a <= t):
            fa += 1
        
    for orange in oranges:
        if (s <= orange + b <= t):
            fo += 1
        
    print(fa)
    print(fo)

def kangaroo(x1, v1, x2, v2):
    # Challenge name: Number Line Jumps
    # Challenge problem statment: https://www.hackerrank.com/challenges/kangaroo/problem
    if (v1 > v2 and ((x2 - x1) % (v1 - v2) == 0)):
        return "YES"
    return "NO"

def pangrams(s):
    # Challenge name: Pangrams
    # Challenge problem statment: https://www.hackerrank.com/challenges/pangrams/problem
    s = s.lower().split()
    s = ''.join(s)
    ascii_set = set([ord(l) for l in s])
        
    if (len(ascii_set) == 26):
        return "pangram"
    else:
        return "not pangram"

def minimumNumber(n, password):
    # Challenge name: Strong Password
    # Challenge problem statment: https://www.hackerrank.com/challenges/strong-password/problem
    count = 0

    if (not re.search('[a-z]', password)):
        count += 1
    if (not re.search('[A-Z]', password)):
        count += 1
    if (not re.search('[0-9]', password)):
        count += 1
    if (not re.search('[!@#$%^&*()+-]', password)):
        count += 1

    return max(count, 6 - n)

def breakingRecords(scores):
    # Challenge name: Breaking the Records
    # Challenge problem statment: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

    changes = [0, 0]
    max_score, min_score = scores[0], scores[0]
        
    for i in range(1, len(scores)):
        if (scores[i] < min_score):
            min_score = scores[i]
            changes[1] += 1
        if ((scores[i] > max_score)):
            max_score = scores[i]
            changes[0] += 1

    return changes

def birthday(s, d, m):
    # Challenge name: Sub-array Division
    # Challenge problem statment: https://www.hackerrank.com/challenges/the-birthday-bar/problem
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
    if n % 2 == 0:
        return int(max(1, 2 ** ((n / 2) + 1) - 1))
    if n % 2 != 0:
        return int(max(1, 2 ** ((n + 3) / 2) - 2))

def angryProfessor(k, a):
    # Challenge name: Angry Professor
    # Challenge problem statment: https://www.hackerrank.com/challenges/angry-professor/problem
    a.sort()
    stud  = 0
    for i in range(k):
        if (a[i] <= 0):
            stud += 1
    return "NO" if stud >= k else "YES"

def queensAttack(n, k, r_q, c_q, obstacles=[[]]):
    # Challenge name: Queen's Attack II
    # Challenge problem statment: https://www.hackerrank.com/challenges/queens-attack-2/problem
    top = n - r_q
    bottom = r_q - 1
    right = n - c_q
    left = c_q - 1

    top_left = min(n - r_q, c_q - 1)
    top_right = n - max(c_q, r_q)
    bottom_left = min(r_q, c_q) - 1
    bottom_right = min(r_q - 1, n - c_q)
    
    if k != 0:
        for obstacle in obstacles:
            if obstacle[0] == r_q:
                if obstacle[1] > c_q:
                    top = min(top, obstacle[1] - c_q - 1)
                else:
                    bottom = min(bottom, c_q - obstacle[1] - 1)
            elif obstacle[1] == c_q:
                if obstacle[0] > r_q:
                    right = min(right, obstacle[0] - r_q - 1)
                else:
                    left = min(left, r_q - obstacle[0] - 1)
            elif abs(obstacle[1] - c_q) == abs(obstacle[0] - r_q):
                if obstacle[1] > c_q and obstacle[0] > r_q:
                    top_right = min(top_right, obstacle[1] - c_q - 1)
                elif obstacle[1] > c_q and obstacle[0] < r_q:
                    bottom_right = min(bottom_right, obstacle[1] - c_q - 1)
                elif obstacle[1] < c_q and obstacle[0] > r_q:
                    top_left = min(top_left, c_q - obstacle[1] - 1)
                elif obstacle[1] < c_q and obstacle[0] < r_q:
                    bottom_left = min(bottom_left, c_q - obstacle[1] - 1)

    return top + bottom + right + left + top_left + top_right + bottom_left + bottom_right

def formingMagicSquare(s):
    # Challenge name: Forming a Magic Square
    # Challenge problem statment: https://www.hackerrank.com/challenges/magic-square-forming/problem 
    magic_combination = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]
    
    if s in magic_combination:
        return 0

    cost = [0] * 8
    for i, ele in enumerate(magic_combination):
        for j in range(3):
            for k in range(3):
                cost[i] += abs(s[j][k] - ele[j][k])
        
    return min(cost)

def catAndMouse(x, y, z):
    # Challenge name: Cats and a Mouse
    # Challenge Problem Statement: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
    if abs(x - z) < abs(y - z):
        return "Cat A"
    elif abs(x - z) > abs(y - z):
        return "Cat B"
    else:
        return "Mouse C"

def getMoneySpent(keyboards, drives, b):
    # Challenge name: Electronics Shop
    # Challenge Problem Statement: https://www.hackerrank.com/challenges/electronics-shop/problem
    keyboards.sort()
    drives.sort()
    l = []
    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive <= b:
                l.append(keyboard + drive)
    
    if l:
        return max(l)
    return -1

def pickingNumbers(a):
    # Challenge name: Picking Numbers
    # Challenge Problem Statement: https://www.hackerrank.com/challenges/picking-numbers/problem
    a.sort()
    picked = []
    for i in a:
        picked.append(a.count(i) + a.count(i + 1))
    return max(picked_)

if __name__ == "__main__":
    pass
