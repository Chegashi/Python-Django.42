def number():
    with open('numbers.txt' , 'r') as f:
        line =  f.readline()
    for c in line:
        if c == ',':
            print('\n')
        else:
            print(c, end = '')
    f.close()

if __name__ == '__main__':
    number()