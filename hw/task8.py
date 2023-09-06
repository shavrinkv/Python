def acronym(text):
    words = text.split(' ')
    acro = ''
    for i in range(len(words)):
        print('The first letter {} is {}'.format(i+1, words[i]))
        acro += words[i][0].upper()
    print('{}'.format(acro))


text = 'Hello World'
acronym(text)