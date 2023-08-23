class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = []
        for i, word in enumerate(sentence.split()):
            if word[0] in 'aeiouAEIOU':
                ans.append(word + 'ma' + 'a' * (i + 1))
            else:
                ans.append(word[1:] + word[0] + 'ma' + 'a' * (i + 1))
        return ' '.join(ans)