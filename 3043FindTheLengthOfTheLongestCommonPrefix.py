class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        hash_set1 = set(arr1)
        hash_set2 = set(arr2)

        for i in arr1:
            for j in range(0, len(str(i)) - 1):
                if i < 10:
                    # print(i)
                    hash_set1.add(i)

                else:
                    # print (i // 10)
                    i = i // 10
                    hash_set1.add(i)

        # print(hash_set1)

        for i in arr2:
            for j in range(0, len(str(i)) - 1):
                if i < 10:
                    # print(i)
                    hash_set2.add(i)

                else:
                    # print (i // 10)
                    i = i // 10
                    hash_set2.add(i)


        # return (max_count)

        common_elements = hash_set1.intersection(hash_set2)
        largest_common = max(common_elements) if common_elements else None
        if largest_common == None:
            return 0
        else:
            return len(str(largest_common))
