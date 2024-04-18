import sys

terminal = sys.stdin.readline().split('.')
del terminal[-1]
text = terminal[-1]
del terminal[-1]

eight_letter = ['0','도','레','미','파','솔','라','시']
eight_letter_react = [0, 1, 2, 3, 4, 5, 6, 7]

result_sum = ""
sums = []

leng = len(terminal)

for i in range(leng):
    a = terminal[i]
    for j in range(3):
        b = eight_letter_react[eight_letter.index(a[j])]
        sums.append(str(b))
    sums += "."
    
del sums[-1]
result_sum = ''.join(i for i in sums)
result_sum = result_sum.split('.')

last = ""

for i in range(len(result_sum)):
    last += chr(int('0o'+result_sum[i], 8))
    
def judgment():
    if last == 'print':
        print(text)

    
    
    
    
    
    # for j in range(3):
        # if terminal[i][j] == eight_letter[0]: terminal[i][j] = eight_letter_react[0]
        # if terminal[i][j] == eight_letter[1]: terminal[i][j] = eight_letter_react[1]
        # if terminal[i][j] == eight_letter[2]: terminal[i][j] = eight_letter_react[2]
        # if terminal[i][j] == eight_letter[3]: terminal[i][j] = eight_letter_react[3]
        # if terminal[i][j] == eight_letter[4]: terminal[i][j] = eight_letter_react[4]
        # if terminal[i][j] == eight_letter[5]: terminal[i][j] = eight_letter_react[5]
        # if terminal[i][j] == eight_letter[6]: terminal[i][j] = eight_letter_react[6]
        # if terminal[i][j] == eight_letter[7]: terminal[i][j] = eight_letter_react[7]
        
        
print(result_sum)
print(sums)
print(terminal)
judgment()