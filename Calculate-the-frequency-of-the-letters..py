text = input('Enter your text: ')
let = input('Enter the letter you want to counting: ')

def count_letter(string , letter):
    count = 0
    for i in string:
        if i == letter:
            count += 1
    print(count)

count_letter(text , let)