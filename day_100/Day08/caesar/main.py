import string
import art

alphabet = list(string.ascii_letters)
# print(alphabet)
print(art.logo)



# 4 菜单
def ceasar(original_text, shift_amount, encode_or_decode):
        output_text = ""
        if encode_or_decode == "decode":
            shift_amount *= -1
        for letter in original_text:
            if letter not in alphabet:
                output_text += letter
            else:
                shift_position = alphabet.index(letter) + shift_amount
                shift_position %= len(alphabet)
                # print(shift_position)
                output_text += alphabet[shift_position]
        print(f"Here is the {encode_or_decode} result: {output_text}")



# 1 User Input
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    ceasar(original_text=text,shift_amount=shift,encode_or_decode=direction)

    restart = input("Type 'Yes' if you want to go again. Otherwise, type 'no' \n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")

# # 2 加密
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shift_position = alphabet.index(letter) + shift_amount #1 -> 3
#         shift_position %= len(alphabet) # 比如25%28那么还是25，比如25%24那么就前移到1，滑滑梯原理。
#         # print(shift_position)
#         cipher_text += alphabet[shift_position]
#     print(f"Here is the encoded result: {cipher_text}")

# encrypt(text,shift)

# # 3 解密
# def decrypt(cipher_text, shift_amount):
#     output_text = ""
#     for letter in cipher_text:
#         shift_position = alphabet.index(letter) + shift_amount
#         shift_position %= len(alphabet)
#         # print(shift_position)
#         output_text += alphabet[shift_position]
#     print(f"Here is the decoded result: {output_text}")

# decrypt(text,shift)


