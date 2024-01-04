"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 

Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
"""

# class UnionFind:
#     def __init__(self, n) -> None:
#         self.parent = [i for i in range(n)] # parent of each group
#         self.grpCnt = n  # total groups 
    
#     def find(self, x):
#         while x != self.parent[x]:
#             x = self.parent[x]
#         return x

#     def union(self, x, y):
#         pre_x = self.find(x)
#         pre_y = self.find(y)
#         if pre_x != pre_y: # if not merged already 
#             # Surely the first [x] would be the lead of group based on first come first serve
#             self.parent[pre_y] = pre_x 
#             self.grpCnt -= 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        def find(n):
            p = parent[n]
            while(parent[p] != p):
                parent[p] = parent[parent[p]]
            return p

        def union(a, b):
            p_a = find(a)
            p_b = find(b)

            if p_a == p_b:
                return False
            if rank[p_a] > rank[p_b]:
                parent[p_b] = p_a
                rank[p_a] += rank[p_b] 
            else:
                parent[p_a] = p_b
                rank[p_b] += rank[p_a] 

            return True

        email_to_idx = {}

        parent = [i for i in range(len(accounts))]
        rank = [1]*len(accounts)

        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_idx:
                    old_idx = email_to_idx[email]
                    union(old_idx, idx)
                else:
                    email_to_idx[email] = idx
    

        finares = {}

        for email,idx in email_to_idx.items():
            p = find(idx)
            if p in finares:
                insort(finares[p], email)
            else:
                finares[p] = [email]


        res = [[accounts[k][0]]+v for k,v in finares.items()]


        return res

        # emailToAcc = {}  # email -> account_idx
        # uf = UnionFind(len(accounts))

        # for idx, account in enumerate(accounts):
        #     for email in account[1:]:
        #         if email in emailToAcc:
        #             # Already account registered in some group
        #             rootGrpId = emailToAcc[email]
        #             uf.union(rootGrpId, idx)   # club current account to registered group
        #         else:
        #             # Account not registered yet
        #             emailToAcc[email] = idx
        
        # # Now the Accounts info is clubbed

        # # counter mechanism to find the pos of unique grp in result list
        # cntr = count()
        # grpToPos = defaultdict(cntr.__next__)
        # merged = [[] for _ in range(uf.grpCnt)]

        # # Combine all emails to specific group
        # for email, accId in emailToAcc.items():
        #     grpId = uf.find(accId)  # this [accId] belongs to which grp ?
        #     pos = grpToPos[grpId]
        #     insort(merged[pos], email)  # Insertion Sort to maintain order

        # # Add name at the start of each merged result
        # for accId, mergePos in grpToPos.items():
        #     name = accounts[accId][0]
        #     merged[mergePos].insert(0, name)

        # return merged








        
