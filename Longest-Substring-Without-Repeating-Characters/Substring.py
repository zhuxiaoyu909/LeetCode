class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        list_str = map(ord,s)
        if len(list_str)==0: 
    	    return 0

        list_pos = [-1 for i in range(1,128)]
        list_pos[list_str[0]]=0

        maxi=1
        end = 1
        star = 0
        while (end < len(list_str)):
    	    if (list_pos[list_str[end]]>=star):
    		    star = list_pos[list_str[end]]+1

    	    list_pos[list_str[end]]=end
    	    maxi = max(maxi,end-list_pos[list_str[star]]+1)
    	    end+=1

        return maxi
