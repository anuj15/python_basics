from cypher_ascii_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def code():
    print(logo)
    repeat = True
    while repeat:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt and 'stop' to exit :\n")
        if direction == 'stop':
            break
        elif direction in ['encode', 'decode']:
            text = input("Type your message:\n").lower()

            if len(text) > 0:
                shift = int(input("Type the shift number:\n"))

                if direction == 'decode':
                    shift *= -1
                result = ''
                for i in text:
                    if i in alphabet:
                        current_index = alphabet.index(i)
                        new_index = (current_index + shift) % 26
                        result += alphabet[new_index]
                    else:
                        result += i
                print(f'The {direction}d text is:\n{result}')
            else:
                print('Invalid input\n')
        else:
            print('Invalid input\n')


code()
