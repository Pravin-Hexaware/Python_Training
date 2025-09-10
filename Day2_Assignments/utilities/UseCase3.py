import string_ops as str
import math_ops as ma
import file_ops as fi

string=input("enter the string:")
print(str.removePunctuation(string))
print(str.count_vowels(string))

num=list(map(int,input("Enter the number:").split()))
print(ma.mean(num))
print(ma.find_median(num))

file_name=input("Enter the filename:")
print(fi.read_file(file_name))
print(fi.write_file(file_name))