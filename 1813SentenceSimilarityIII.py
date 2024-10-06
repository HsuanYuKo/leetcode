class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) > len(sentence2):
            s1 = sentence1
            s2 = sentence2
        else:
            s2 = sentence1
            s1 = sentence2
        
        s1_list = s1.split(" ")
        s2_list = s2.split(" ")

        if len(s1_list) == len(s2_list):
            if s1_list != s2_list:
                return False

        if s1.startswith(s2): #prefix
            if s2_list == s1_list[0:len(s2_list)]:
                return True
        if s1.endswith(s2): #suffix
            if s2_list == s1_list[len(s1_list) - len(s2_list):len(s1_list)]:
                return True
        else:
            prefix = []
            suffix = s2_list[:]

            for i in range(0, len(s2_list) - 1):
                prefix.append(s2_list[i])
                suffix.pop(0)
                prefix_str = " ".join(prefix)
                suffix_str = " ".join(suffix)
                print(prefix_str)
                print(suffix_str)
                if s1.startswith(prefix_str) and s1.endswith(suffix_str) and s2_list[-1] == s1_list[-1] and s2_list[0] == s1_list[0]:
                    return True
            return False

                
        
