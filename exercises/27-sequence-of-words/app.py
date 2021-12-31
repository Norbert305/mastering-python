phrase = input("Input words: ")

phrase_list = phrase.split(",")
phrase_list.sort()
print((', ').join(phrase_list))

#input: without,hello,bag,world

#output: bag,hello,without,world