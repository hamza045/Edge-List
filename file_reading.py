

file = 'busstops0.txt'

with open(file, mode = 'r') as myfile:
    print(type(myfile))
    EX = list(myfile)


with open('OUTFILE.csv', mode = 'w+') as output:
    for v in EX:
        try:
            ls = v.split(',')
            for index, value in enumerate(ls):

                f = value+ '\t'+ ls[index+1] + '\n'

                output.writelines(f)
            output.writelines('\n\n')
        except:
            pass
        
