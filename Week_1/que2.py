import random

A = [0, 5 ,27 ,6 ,13 ,28, 100 ,45 ,10, 79]
def pick_a_number_from_list(A):
    sum=0
    cum_sum=[]
    for i in range(len(A)):
        sum = sum + A[i]
        cum_sum.append(sum)
    r = int(random.uniform(0,sum))
    number=0
    for index in range(len(cum_sum)):
        if(r>=cum_sum[index] and r<cum_sum[index+1]):
            return A[index+1]
    return number


def sampling_based_on_magnitued():
    for i in range(1,100):
        number = pick_a_number_from_list(A)
        print(number, end=', ')

sampling_based_on_magnitued()