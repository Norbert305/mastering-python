

def compute_factorila(num):

    for i in range(1,num):
        num = num*i
    
    return num
print(compute_factorila(8))

#https://www.programiz.com/python-programming/examples/factorial

#iteration	factorial*i(returned value)
#i = 1	    1 * 1 = 1
#i = 2	    1 * 2 = 2
#i = 3	    2 * 3 = 6
#i = 4	    6 * 4 = 24
#i = 5	    24 * 5 = 120
#i = 6	    120 * 6 = 720
#i = 7	    720 * 7 = 5040