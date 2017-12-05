def say(number):
    if number == 0:
        return('zero')
    if number < 0 or number >= 1e12:
        raise ValueError
    ones = ['', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ',
            'eight ', 'nine ']
    tens = ['ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ', 'sixteen ',
            'seventeen ', 'eighteen ', 'nineteen ']
    twenties = ['', '', 'twenty ', 'thirty ', 'fourty ', 'sixty ', 'seventy ',
                'eighty ', 'ninety ']
    thousands = ['', 'thousand ', 'million ', 'billion ', 'trillion ',
                 'quadrillion ', 'quintillion ', 'sextillion ', 'septillion ',
                 'octillion ',
                 'nonillion ', 'decillion ', 'undecillion ', 'duodecillion ',
                 'tredecillion ', 'quattuordecillion ', 'quindecillion',
                 'sexdecillion ', 'septendecillion ',
                 'octodecillion ', 'novemdecillion ', 'vigintillion ']
    num_split = list()
    num_str = str(int(number))
    for i in range(3, 33, 3):
        slc = num_str[-i:]
        q = len(num_str) - i
        if q <= -3:
            break
        else:
            if q == -1:
                num_split.append(int(slc[:2]))
            elif q == -2:
                num_split.append(int(slc[:1]))
            else:
                num_split.append(int(slc[:3]))
    num_say = ""
    for i, x in enumerate(num_split):
        b1 = x % 10
        b2 = (x % 100) // 10
        b3 = (x % 1000) // 100
        # print('x= ', x, 'b2= ', b2)
        if x == 0:
            continue
        else:
            t = thousands[i]
        if b2 == 0:
            num_say = ones[b1] + t + num_say
        elif b2 == 1:
            num_say = tens[b1] + t + num_say
        elif b2 > 1:
            if b1 != 0:
                num_say = twenties[b2][:-1] + '-' + ones[b1] + t + num_say
            else:
                num_say = twenties[b2] + t + num_say
        if b3 >= 1:
            if b1 == 0 and b2 == 0:
                num_say = ones[b3] + 'hundred ' + num_say
            else:
                num_say = ones[b3] + 'hundred and ' + num_say
    return(num_say)
