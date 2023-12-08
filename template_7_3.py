
class not2DError(Exception):
# Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'

class unevenListError(Exception):
# Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'

class improperMatrixError(Exception):
# Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'


def mul1d(arr1,arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum+=arr1[i]*arr2[i]
    return sum

class list_D2(list):
    def __init__(self,arr):
        
        ### YOUR CODE HERE ###
        
        raise  not2DError()
        raise unevenListError()
    
        ######

        self.extend(arr)

    def __str__(self):

        ### YOUR CODE HERE ###
        
        return 'Hello, world!'

        ######

    def transpose(self):

        ### YOUR CODE HERE ###

        return self
        
        ######


    def __matmul__(self, others):
        
        ### YOUR CODE HERE ###
        
        raise improperMatrixError()
        return self

        ######

    def avg(self):

        ### YOUR CODE HERE ###
        
        return 0.0

        ######
