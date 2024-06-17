import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

# dataframe to dict
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def nato_word():
    word = input('Enter a word: ')
    word_list = [x.upper() for x in word]
    # list to dict
    try:
        word_dict = {x: new_dict[x] for x in word_list}
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
    else:
        print(word_dict)
    finally:
        nato_word()


nato_word()
