def compute_conditional_probabilites(F, S):
    numerator = 0
    denominator = 0
    for i in range(len(A)):
        if(A[i][1] == S):
            denominator = denominator + 1
            if(A[i][0] == F):
                numerator = numerator + 1
    print('P(F = {} | S == {}) = {}/{}'.format(F, S, str(numerator), str(denominator)))

A = [['F1','S1'],['F2','S2'],['F3','S3'],['F1','S2'],['F2','S3'],['F3','S2'],['F2','S1'],['F4','S1'],['F4','S3'],['F5','S1']]

for i in ['F1', 'F2', 'F3', 'F4', 'F5']:
    for j in ['S1', 'S2', 'S3']:
        compute_conditional_probabilites(i, j)