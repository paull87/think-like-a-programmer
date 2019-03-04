
char = '#'
end_char = '\n'


def create_half_square(number, char=char, end_char=end_char):
    output_format = '{}{}'
    output = ''
    for idx in range(number, 0, -1):
        output += output_format.format(str(char) * idx, end_char)
    return output



def create_triangle(number, char=char, end_char=end_char):
    output_format = '{}{}'
    output = ''
    for idx in range(1, number * 2):
        idx_number = number - abs(number - idx)
        output += output_format.format(str(char) * idx_number, end_char)
    return output


for i in range(100):
    print('create_half_square >> {}'.format(i))
    print(create_half_square(i, i))

    print('create_triangle >> {}'.format(i))
    print(create_triangle(i, i))
