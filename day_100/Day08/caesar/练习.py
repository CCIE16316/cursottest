from main import alphabet

def all_in_one(orginal_text,shift,encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift *= -1
    for letter in orginal_text: # e.g. CCC
        # C
        position = alphabet.index(letter) + shift
        alphabet[position].append(output_text)
    print(output_text)

all_in_one("ccc",2,"encode")