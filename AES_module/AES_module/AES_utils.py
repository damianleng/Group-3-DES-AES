class AES_utils:
    def add(self, A, B):
    # make sure A, B have the same length
        while len(A) > len(B):
            B = '0' + B
        while len(B) > len(A):
            A = '0' + A
        C = ''
        for i in range(len(A)):
            if A[i] == B[i]:
                C += '0'
            else:
                C+= '1'
        # Get rid of zeros in front of C
        i = 0
        while i<len(C) and C[i] == '0':
            i += 1
        if i == len(C):
            C = '0' # all 0s
        else:
            C = C[i:]
        return C
    
    def multiply(self, A, B):
        C = '0' # result
        for i in range(len(B)-1, -1, -1):
            if B[i] == '1':
                C = self.add(C, A)
            A = A + '0'
        return C
    
    def mod(self, A, P):
        # 101110 substr -> 10111 then add 10111 + P, then addpend it to the leftover substr
        # use substr, then add it, and then append it to the leftover substr
        result = A
        while len(result) >= len(P):
            left = self.add(result[:len(P)], P)
            right = result[len(P):]
            result = left + right
        return result