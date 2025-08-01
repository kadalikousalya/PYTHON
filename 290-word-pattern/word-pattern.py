class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss=s.split()
        if len(ss)!=len(pattern):
            return False
        char_to_word={}
        word_to_char={}
        for c,w in zip(pattern,ss):
            if c in char_to_word:
                if char_to_word[c]!=w:
                    return False
            else:
                char_to_word[c]=w
            
            if w in word_to_char:
                if word_to_char[w]!=c:
                    return False
            else:
                word_to_char[w]=c
        return True
        