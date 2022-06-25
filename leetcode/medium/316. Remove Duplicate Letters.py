class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        character_count = {}
        character_seen = {}
        stack = []
        
        for i in range(len(s)):
            character_count[s[i]] = character_count.get(s[i],0) + 1
            character_seen[s[i]] = False
        
        for i in range(len(s)):
            character_count[s[i]] -= 1
            if character_seen[s[i]] == True:
                continue
                
            while len(stack) > 0 and character_count[stack[-1]] > 0 and stack[-1] > s[i]:
                character_seen[stack.pop()] = False
                    
            stack.append(s[i])
            character_seen[s[i]] = True
            
        
        string = ""
        
        for i in range(len(stack)):
            string += stack[i]
        
        return string
            