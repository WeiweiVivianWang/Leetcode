class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # queue = collections.deque(beginWord) --> deque(['h', 'i', 't'])
        queue = collections.deque([beginWord]) #--> deque(['hit'])
        wordList = set(wordList) #一定要转换成set 去重，避免time limit exceeded ,list 查找费时间
        distance_dic = {beginWord:1}
        
        
        while queue:
            word = queue.popleft()
            if word ==endWord:
                return distance_dic[word]
            
            for next_word in self.getNextWord(word, wordList):
                if next_word in distance_dic:
                    continue
                    
                queue.append(next_word)             
                distance_dic[next_word]=distance_dic[word] +1
        return 0 #如果queue全pop完了 还没有word==endWord, distance 为0
                
                
                
            
    def getNextWord(self, word, wordList):
        
        nextWord = set()
        for i in range(len(word)):
            left = word[:i]
            right = word[i+1:]
            
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char == word[i]: 
                    continue
                    
                new_word = left+char+right
                
                if new_word in wordList:
                    nextWord.add(new_word)
                    
        return nextWord