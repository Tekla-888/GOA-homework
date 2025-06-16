def is_square(n):
    if n < 0: return False

    if int(n0.5)*int(n0.5)==n: return True
    return False
#You're a square!



def get_middle(s):
    if len(s)%2 == 0:
        return s[len(s)//2-1:len(s)//2+1]
    else:
        return s[len(s)//2]

#Get the Middle Character



def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))

#Isograms



def xo(s):
    s = s.lower()
    return s.count("o") == s.count("x")

#1Exes and Ohs



def to_jaden_case(string):
    string = [i.capitalize() for i in string.split(" ")]
    return " ".join(string)

#Jaden Casing Strings


def find_short(s):
    s = s.split(" ")
    res = 1000000

    for i in s:
        if len(i) < res:
            res = len(i)
    return res

#Shortest Word


def solution(text, ending):
    return text[len(ending)*-1:] == ending



def accum(st):
    res = []

    for i in range(len(st)):
        chr = st[i]
        new_str = chr*(i+1)
        res.append(new_str.capitalize())

    return "-".join(res)

#Mumbling





def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0]+numbers[1]

#Sum of two lowest positive integers

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers, reverse=True)[-2:])




def DNA_strand(dna):
    res = ""

    for base in dna:
        if base == "A": res+="T"
        elif base == "T": res+="A"
        elif base == "C": res+="G"
        else: res+="C"

    return res

#Complementary DNA

def friend(x):
    res = []
    for i in x:
        if len(i) == 4:
            res.append(i)
    return res


def friend(x):
    return [i for i in x if len(i)==4]





def maskify(cc):
    if len(cc) <= 4:
        return cc
    res = ""
    for i in range(len(cc)):
        if i < len(cc) - 4:
            res+="#"
        else: res+=cc[i]
    return res