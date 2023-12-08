
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
        
        x = len(arr)
        if x == 0: raise not2DError
        
        for i in range(x):
            try:
                y = len(arr[i])
            except:
                raise not2DError
            
            for j in range(y):
                try:
                    len(arr[i][j])
                    raise not2DError
                except:
                    if y != len(arr[0]):
                        raise unevenListError()
            
        
        ######

        self.extend(arr)

    def __str__(self):

        ### YOUR CODE HERE ###
        
        return ("list_2D: " + str(len(self)) + "*" + str(len(self[0])))

        ######

    def transpose(self):

        ### YOUR CODE HERE ###
        
        trans_x, trans_y = [], []
        for j in range(len(self[0])):
            for i in range(len(self)):
                trans_x.append(self[i][j])
            trans_y.append(trans_x)
            trans_x = []
        
        trans = trans_y
        
        return list_D2(trans)
        
        ######


    def __matmul__(self, others):
        
        ### YOUR CODE HERE ###
        
        othersT = list_D2(others).transpose()
        if len(self) != len(othersT):
            raise improperMatrixError()
        result_x, result_y = [], []
        for i in range(len(self)):
            for j in range(len(othersT)):
                result_x.append(mul1d(self[i], othersT[j]))
            result_y.append(result_x)
            result_x = []
            
        return list_D2(result_y)

        ######

    def avg(self):

        ### YOUR CODE HERE ###
        
        sum = 0.0
        length = 0
        for i in range(len(self)):
            for j in range(len(self[i])):
                sum += self[i][j]
                length += 1
        
        return sum / length

        ######
