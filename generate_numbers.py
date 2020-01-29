'''
Sample generation of a range of member numbers

'''
from member_number import create_id

current_id = "123000006460"

with open('sample_numbers.txt', 'w') as output_file:

    for x in range(0,10000):
        member_number = create_id(current_id)
        output_file.write(("%d,%s\n") % (x,member_number))
        current_id = member_number


