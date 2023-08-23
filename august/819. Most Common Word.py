'''
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.
'''

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').replace(';',' ').replace("'",' ')
        paragraph = paragraph.lower()
        paragraph = paragraph.split()
        # print(paragraph)
        dic = {}
        for i in paragraph:
            if i not in banned:
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] += 1
        # print(dic)
        return max(dic, key=dic.get)