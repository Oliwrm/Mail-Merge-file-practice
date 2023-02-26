#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

with open("./Input/Names/invited_names.txt",mode="r") as names:
    name_list=names.readlines()

with open("./Input/Letters/starting_letter.txt",mode="r") as letter:
    lett=letter.read()
    print(lett)

for name in name_list:
    fixed_name=name.replace("\n","")
    final_letter=lett.replace("[name]",fixed_name)
    print(final_letter)
    with open(f"./Output/ReadyToSend/letter_for_{fixed_name}.txt",mode="w") as new_letter:
        new_letter.write(final_letter)


