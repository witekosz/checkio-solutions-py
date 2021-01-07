MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code: str) -> str:
    # words_list: list = code.split("   ")
    # words_list_decrypted: list = list()
    # words_list_decrypted_2: list = ["".join([MORSE[i] for i in word.split(" ")]) for word in words_list]

    # for word in words_list:
    #     words_list_decrypted.append("".join([MORSE[i] for i in word.split(" ")]))
    # decrypted: str = " ".join(["".join([MORSE[i] for i in word.split(" ")]) for word in code.split("   ")])

    # if decrypted[0].isalpha(): decrypted = "".join([decrypted[0].upper(), decrypted[1:]])

    return " ".join(["".join([MORSE[i] for i in word.split(" ")]) for word in code.split("   ")]).capitalize()


print(morse_decoder("... --- ..."))
print(morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"))

# if __name__ == '__main__':

#     assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
#     assert morse_decoder("..--- ----- .---- ---..") == "2018"
#     assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"