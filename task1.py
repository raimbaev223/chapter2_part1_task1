

def percentage_of_letters():
    text = list(input('Input text: '))
    upper_ = 0
    lower_ = 0
    for _ in text:
        if _.isupper() == True:
            upper_ = upper_ + 1
        elif _.islower() == True:
            lower_ = lower_ + 1
        else:
            continue
    all_letters = upper_ + lower_
    print((upper_ / all_letters) * 100, '% of upper letters')
    print((lower_ / all_letters) * 100, '% lower letters')

percentage_of_letters()