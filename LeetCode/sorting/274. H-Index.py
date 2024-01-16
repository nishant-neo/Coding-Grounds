class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_index = len(citations)
        cit_dict = {}
        for citation in citations:
            cit_dict[min(citation, max_index)] = cit_dict.get(min(citation, max_index),0)+1

        last = 0
        for i in reversed(range(1, max_index+1)):
            last += cit_dict.get(i, 0)

            if last >= i:
                return i

        # print(cit_dict)

        # # onlgn
        # citations.sort(reverse = True)
        # h_index = 0
        # for i, citation in enumerate(citations):
        #     if citation >= i+1:
        #         h_index = i+1
        # print(citations)

        #on^2

        # max_index = len(citations)
        # h_index = 0
        # for i in range(0, max_index+1):
        #     count = 0
        #     for citation in citations:
        #         if citation >= i:
        #             count += 1
        #     if count >= i:
        #         h_index = i


        return 0
