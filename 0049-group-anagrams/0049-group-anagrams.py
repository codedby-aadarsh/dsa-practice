class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_word={}
        for word in strs:
            sort_word=''.join(sorted(word))
            if sort_word not in ana_word:
                ana_word[sort_word]=[]
            ana_word[sort_word].append(word)
        return list(ana_word.values())