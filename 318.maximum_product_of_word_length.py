class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                #here we are doing the operation such that a character is present in the string or not 
                #and after that when we compare this numbers for the strings if we do bit-wise and operations for 
                #these numbers if we get a number greater than 0 we say there must be atleast one character that is same
                #in both the strings and we will not concider that pair of strings here.
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])
        
        #the below code  is much naive approach for this 
        '''
        
        m=0
        for i in words:
            for j in words:
                if len(set(i).intersection(set(j))) == 0:
                    m=max(m,len(i)*len(j))
        return m '''