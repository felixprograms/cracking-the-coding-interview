# # input string, output boolean
# import abc


# # def allUniqueChars(string):
# #     letters = {} # 1
# #     for letter in string: #2
# #         if letter in letters: #2.1
# #             return False
# #         else:
# #             letters[letter] = True
# #     return True# 3

# # # 1. create an empty dictionary
# # # 2. iterate over each letter of the string
# # # 2.1 check if the letter 
# # #     is already part of the dictionary
# # #     if it is, then return False
# # #     if it is not, then add it to dictionary
# # # 3. return True

# # abc
# # 'a'
# #     compare with 'a', 'b' and 'c'
# #     return false here because of 'a' == 'a'
# # 'a'
# #     compare with 'b' and 'c'
# # 'b'
# #     compare 'c'
# # 'c'
    
# # aabc

# # time complexity
# # O(n) -> O(n**2)

# # space complexity
# # O(n) -> O(1)
# # 1. iterate over each letter
# # 2. inside the iteration of step 1, iterate over the rest of the letters
# # 2.1 compare the letter of iteration 1 with iteration 2
# #     if the letters match, return False
# # 3. return True

# # print(allUniqueChars('abc') == True)
# # print(allUniqueChars('aabc') == False)
# # print(allUniqueChars('Aabc') == True)
# def eliminate_trailing_spaces(string):
#     # base case (when recursion stops)
#     if len(string) == 0 or (string[-1] != ' ' and string[0] != ' '): #'     abc'
#         return string
#     elif string[0] == ' ':
#         return eliminate_trailing_spaces(string[1:])
#     else:
#         # recursive case (when recursion continues)
#         return eliminate_trailing_spaces(string[:-1])

# print(eliminate_trailing_spaces('    abc    '))
# print(eliminate_trailing_spaces('abc'))
# print(eliminate_trailing_spaces(''))


# def URLify(string):
#     string = eliminate_trailing_spaces(string)
#     new_string = ''
#     for letter in string:
#         if letter == ' ':
#             new_string += '%20'
#         else:
#             new_string += letter
#     return new_string

# print(URLify(' Mr. John Smith   '))

# def reverse(string):
#     return string[::-1]

# #print(reverse('abc'))


# def check_permutation(string1, string2):
#     dictionary1 = {}
#     dictionary2 = {}
#     for letter in string1: # n n is the length of the string. space complexity is big of n
#         if letter in dictionary1:
#             dictionary1[letter] += 1  
#         else:
#             dictionary1[letter] = 1

#     for letter in string2:
#         if letter in dictionary2:
#             dictionary2[letter] += 1
#         else:
#             dictionary2[letter] = 1

#     return dictionary1 == dictionary2

# def check_permutation2(string1, string2):
#     a = list(string1)
#     b = list(string2)
#     a.sort() # time complexity? space complexity? n log n the space complexity is constant
#     b.sort() # time complexity? space complexity? 
#     return a == b

# print(check_permutation('abc', 'bca') == True)
# print(check_permutation('aabc', 'abbc') == False)

# print(check_permutation2('abc', 'bca') == True)
# print(check_permutation2('aabc', 'abbc') == False)


def oneaway(string1, string2):
    first_set = set(string1)
    second_set = set(string2)
    difference = first_set.symmetric_difference(second_set)

    return len(difference) <= 2
    
def oneaway2(str1, str2):
    if len(str1) == len(str2):
        return can_be_replaced_by_1(str1, str2)
    else:
        return can_be_replaced_by_1_2(str1, str2)

def can_be_replaced_by_1(str1, str2):
        number_of_differences = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                number_of_differences += 1
        return number_of_differences < 2

def can_be_replaced_by_1_2(str1, str2):
        if len(str1) - len(str2) < -1 or len(str1) - len(str2) > 1:
            return False
        i1 = 0
        i2 = 0
        number_of_differences = 0
        while i1 < len(str1) and i2 < len(str2):
            if str1[i1] != str2[i2]:
                if number_of_differences > 1:
                    return False
                number_of_differences += 1
                if len(str1) > len(str2):
                    i1 += 1
                else:
                    i2 += 1
            else:
                i1 += 1
                i2 += 1
        return True


print(oneaway('pale', 'ple'))
print(oneaway('pale', 'pales'))
print(oneaway('pale', 'bale'))
print(oneaway('pale', 'bake'))
print(oneaway('paake', 'baake'))


print(oneaway2('pale', 'ple'))
print(oneaway2('pale', 'pales'))
print(oneaway2('pale', 'bale'))
print(oneaway2('pale', 'bake'))
print(oneaway2('paake', 'baake'))

#problem1.1

def is_unique(string):
    dictionary = {}
    for letter in string:
        if letter in dictionary:
            return False
        else:
            dictionary[letter] = 1
    return True


# compare 'a' to 'b', 'c', 'd'
# compare 'b' to 'c', 'd'
# compare 'c' to 'd'


def is_unique2(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True           

print('problem 1.1')
print(is_unique2('abc') == True)
print(is_unique2('aabc') == False)
print(is_unique2('Aabc') == True)

def check_permutation(string1, string2):
    a = list(string1)
    b = list(string2)
    a.sort()
    b.sort()
    return a == b
print('problem 1.2')
print(check_permutation('abc', 'bca') == True)
print(check_permutation('aabc', 'abbc') == False)

#print(check_permutation2('abc', 'bca') == True)
#print(check_permutation2('aabc', 'abbc') == False)        


# 1.8

# def zero_matrix(arr1, arr2):
#     pass

# argument = [
#     [2,5,8,0,1],
#     [6,8,1,2,4],
#     [2,8,3,2,5]
# ]
# result = [
#     [0,0,0,0,0],
#     [6,8,1,0,4],
#     [2,8,3,0,5]
# ]

# print(zero_matrix(argument) == result)
def remove_spaces(string):
    if string =='':
        return ''
    if string[0] == ' ':
        return remove_spaces(string[1:])
    elif string[-1] == ' ':
        return remove_spaces(string[:-1])
    else:
        return string

def urlify2(string):
    string = remove_spaces(string)
    new_string = ''

    for letter in string:
        if letter == ' ':
            new_string += '%20'
        else:
            new_string += letter
    return new_string        


print(urlify2("Mr John Smith") == "Mr%20John%20Smith")
print(urlify2("  Mr John Smith   ") == "Mr%20John%20Smith")


def perm_palindrome(string):
    dictionary = {}
    for letter in string:
        if letter == ' ':
            continue
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    count = 0
    for letter in dictionary.values():
        if letter % 2 != 0:
            count += 1
    return count <= 1



print(perm_palindrome("tact coa") == True)
print(perm_palindrome("leelmadam") == True)

#problem 1.6

def string_compression(uncompressed_string):
    compressed_string = ''
    count = 1
    last_letter = ''
    for letter in uncompressed_string:
        if last_letter != letter:
            if last_letter != '':
                compressed_string += last_letter + str(count)
            last_letter = letter
            count = 1    
        else:
            count += 1
    compressed_string += last_letter + str(count)
    return compressed_string

print(string_compression('aabcccccaaa'))