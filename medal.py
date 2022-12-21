import csv, random, os

table = {}

def unpack(file):
    path = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(path, file)
    with open(file, newline="") as f:
        count = 0
        for row in csv.reader(f, delimiter=" ", quotechar="|"):
            if count > 0:
                row = row[0].split(",")
                table[row[0]] = row[1::]
            else:
                row = row[0].split(",")
                header = row
            count += 1
    print(table)
    return header

def pack(d, file, header):
    array = [header]
    for key in d:
        temp = [key]
        for n in d[key]:
            temp.append(str(n))
        array.append(temp)

    path = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(path, file)
    with open(file, "w", newline="") as f:
        W = csv.writer(f, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        print(array)
        W.writerows(array)

def convertToIntegers(d):
    for key in d:
        for n in range(len(d[key])):
            d[key][n] = int(d[key][n])
    return d

def weight(d):
    for key in d:
        d[key][0] *= 3
        d[key][1] *= 2
    return d

def getSum(d):
    for key in d:
        d[key] = sum(d[key])
    return d

def compare(left, right, n):
    if left[0][1][n] > right[0][1][n]:
        return True
    elif left[0][1][n] < right[0][1][n]:
        return False
    else:
        try:
            return compare(left, right, n + 1)
        except IndexError:
            return False

def mergeArrays(left, right):
    merged = []
    while len(left) > 0 and len(right) > 0:
        compared = compare(left, right, 0)
        if compared:
            merged.append(left[0])
            left = left[1::]
        else:
            merged.append(right[0])
            right = right[1::]  

    while len(left) > 0:
        merged.append(left[0])
        left = left[1::]
    while len(right) > 0:
        merged.append(right[0])
        right = right[1::]
    return merged

def mergeSort(array):
    l = len(array)
    left = []
    right = []
    if l <= 1:
        return array
    for n in range(0, l):
        if n < l / 2:
            left.append(array[n])
        else:
            right.append(array[n])
    print()
    print(left)
    print(right)
    left = mergeSort(left)
    right = mergeSort(right)
    return mergeArrays(left, right)

def sortTable(d):
    array = list([key, d[key]] for key in d)
    new = {}
    if len(d) > 1:
        array = mergeSort(array)
        for row in array:
            new[row[0]] = d[row[0]]
        print()
        print(new)
        return new
    print(d)
    return d

if __name__ == "__main__": 
    header = unpack("medal.csv")
    new_table = sortTable(table)
    pack(new_table, "medal_table.csv", header)

'''
# Feel free to create other helper functions
# def helper_function_name(arguments):
#      pass

def rank_team(file_name):
    # your code starts from here.
    pass

    
# Program main --- Do not change the code below but feel free to comment out 
# Calling Task 1 function

rank_team('medal.csv')
'''