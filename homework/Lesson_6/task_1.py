# Задание 1

phrase = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, " \
         "facilisis vitae semper at, dignissim vitae libero"

slova_vo_phrase = phrase.split()
# print(slova_vo_phrase)

novaya_phrasa = []

for word in slova_vo_phrase:
    if (word[-1] == ',') or (word[-1] == '.'):
        novaya_phrasa.append(word[:-1] + 'ing' + word[-1])
    else:
        novaya_phrasa.append(word + 'ing')

print(novaya_phrasa)
