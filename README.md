
# Open Password Protected File Using Python.

In this project, you can crack any PDF file without password and wordlist.

let's start...............

To make this project you need to follow this step:-










## Installation

Install package with pip

```bash
pip install pikepdf
pip install colorama 
pip install itertools 

```
    
## Deployment

To deploy this project run

```bash
#please subscribe "Problem Solve With Ridoy" youtube channel

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
```


## 







## You can follow me

Facebook:- https://www.facebook.com/problemsolvewithridoy/

Linkedin:- https://www.linkedin.com/in/ridoyhossain/

YouTube:- https://www.youtube.com/@problemsolvewithridoy

Gmail:- entridoy2@gmail.com

If you have any confusion, please feel free to contact me. Thank you

