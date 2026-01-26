def camelcase (sentence):
    title_case = sentence.title() # Uppercase the first letter of each word
    upper_camel_cased = title_case.replace(' ', '') # Remove spaces between words

    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def banner():
    """ Display program name """
    message = 'CamelCase Converter'
    stars = '*' * len(message)
    print(f'{stars} \n{message} \n{stars}\n')


def main():
    banner()
    sentence = input('Enter a sentence: ')
    output = camelcase(sentence)
    print('CamelCase:', output)

if __name__ == '__main__':
    main()