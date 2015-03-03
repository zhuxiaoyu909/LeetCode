class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        #Create an empty dictionary
        Hash={}
        
        #Let key be the element in num, value be the index
        for i, num1 in enumerate(num):
            Hash.setdefault(num1,[]).append(i+1)
         
          
        for num2 in num:
            if (target-num2)!=num2 and target-num2 in Hash:
            	return (Hash[num2][0],Hash[(target-num2)][0])
            if (target-num2)==num2 and len(Hash[num2])>1:
            	return (Hash[num2][0],Hash[num2][1])
