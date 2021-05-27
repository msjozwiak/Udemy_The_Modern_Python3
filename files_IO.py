# EX1

'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''


def copy(file_txt, copy_file_txt):
    with open(file_txt, "r") as f1:
        content = f1.read()
    with open(copy_file_txt, "w") as f2:
        f2.write(content)


# copy("story.txt", "story_copy.txt")


# EX2
'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''


def copy_and_reverse(file_txt, reversed_file_txt):
    with open(file_txt, "r") as f1:
        content = f1.read()
    with open(reversed_file_txt, "w") as f2:
        f2.write(content[::-1])


# copy_and_reverse("story.txt", "story_reversed.txt")


# EX3
'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''


def statistics(file_txt):
    with open(file_txt, "r+") as f1:
        lines = len(f1.readlines())
        f1.seek(0)
        words = len(f1.read().split())
        f1.seek(0)
        characters = len(f1.read())
        return {"lines": lines, "words": words, "characters": characters}



# print(statistics("story.txt"))


# EX 4


'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''


def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()


# print(find_and_replace("story.txt", 'Alice', 'Colt'))
