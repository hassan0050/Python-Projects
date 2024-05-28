def word_counter(text):
    words = text.split()
    return len(words)


task = int(input("Which task do you want to perform? Enter number of the task: \n 1 Words Count \n "
                 "2 Characters Count \n"))
text = input("Enter Text Here: \n")

if task == 1:
    print("The Number of words is: ", word_counter(text))
elif task == 2:
    print("The number of characters is: ", len(text))
