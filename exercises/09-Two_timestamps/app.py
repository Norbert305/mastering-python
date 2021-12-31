#Complete the funtion to compute how many seconds passed between the two timestamp.
def two_timestamp(hr1,min1,sec1,hr2,min2,sec2):
    
    hr1 = hr1 * 3600
    min1 = min1 * 60
    sec1 = sec1 * 1
    hr2 =  hr2 * 3600
    min2 = min2 * 60
    sec2 = sec2 * 1
    timestamp1 = hr1 + min1 + sec1
    timestamp2 = hr2 + min2 + sec2
    return  timestamp2 - timestamp1


#Invoke the fuction and pass two timestamps(6 intergers) as its argument.
print(two_timestamp(1,1,1,2,2,2))