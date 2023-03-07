# Please subscribe my youtube channel "Problem Solve with Ridoy"
# Also you can follow me on facebook "Problem Solve with Ridoy"
import pikepdf
import time
from colorama import Fore
from string import *
from itertools import product

value = ascii_letters + digits + punctuation

count = 0
start_time = time.time()
for i in range(4,3,-1):
    for j in product(value, repeat = i):
        count += 1
        word = "".join(j)
        print(Fore.RED+ f"\r{count} password trying but didn't match: {word}",end="")
        try:
            pikepdf.open("Your_PDF_File_Name.pdf", password=str(word))
            end_time = time.time()
            print("\n")
            print(Fore.GREEN+f"Password found in {str(end_time-start_time)[:4]} second \nPassword is: ",end= "")
            print(Fore.BLUE+f"{word}")
            break
        except:
            continue

print(Fore.LIGHTYELLOW_EX+ "Thank you")

# If you have any confution then fell free contact with me- entridoy2@gmail.com or linkedin: ridoyhossain
