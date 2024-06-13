# Create a letter using starting_letter.txt
# for each name in inviting_letter.txt replace the name placeholder with actual name
# Save the letters in teh folder ready_to_send
with open('./input/letters/starting_letter.txt', 'r') as f:
    letter_content = f.read()

with open('./input/names/invited_names.txt', 'r') as f:
    names = f.readlines()
    names = [x.strip('\n') for x in names]

for name in names:
    custom_letter = letter_content.replace('[name]', name)
    with open(f'./output/ready_to_send/letter_to_{name}.txt', 'w') as f:
        f.write(custom_letter)
