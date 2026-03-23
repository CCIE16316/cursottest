import string
from unittest import TestResult
alphabet = list(string.ascii_letters)

def all_in_one(orginal_text,shift,encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift *= -1
    for letter in orginal_text: # e.g. CCC
        # C
        position = alphabet.index(letter) + shift
        position %= len(alphabet)
        output_text += alphabet[position] # 这里目标对象是str，所以不能用append，只能用+= 
    print(output_text)

all_in_one("eee",2,"decode")


should_continue = True
while should_continue:
    method = input("Encode or Decode? \n").lower()
    choice = input("Yes or No\n").lower()
    if choice == "no":
        should_continue = False

