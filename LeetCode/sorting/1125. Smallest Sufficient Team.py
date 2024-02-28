"""
1125. Smallest Sufficient Team
Solved
Hard
Topics
Companies
Hint
In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

It is guaranteed an answer exists.

 

Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:

Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]
 

Constraints:

1 <= req_skills.length <= 16
1 <= req_skills[i].length <= 16
req_skills[i] consists of lowercase English letters.
All the strings of req_skills are unique.
1 <= people.length <= 60
0 <= people[i].length <= 16
1 <= people[i][j].length <= 16
people[i][j] consists of lowercase English letters.
All the strings of people[i] are unique.
Every skill in people[i] is a skill in req_skills.
It is guaranteed a sufficient team exists.
"""

class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        # 1. Assign indexes for each skill string
        skills = {
            skill: i for i, skill in enumerate(req_skills)
        }
        # 2. Create sets with skill indexes for each person
        people = [(i, {skills[skill] for skill in person}) for i, person in enumerate(people)]
        # 3. Sort people by length of skillset
        people.sort(key=lambda x: len(x[1]))

        valid_people = []
        # 4. Iterate over people list and check if person's skill set 
        # is a subset of other person's skill set. If it is, ignore it,
        # otherwise, add it to `valid_people` list
        for idx, person in enumerate(people):
            i, skillset = person
            is_valid = True

            for j, s in people[idx + 1:]:
                if skillset.issubset(s):
                    is_valid = False
                    break

            if is_valid:
                valid_people.append((i, skillset))

        m = len(valid_people)
        # 5. BFS: init deque with combinations of length 1 for every valid person index
        d = deque([((i,)) for i in range(m)])

        while d:
            idxs = d.popleft()
            # Receive skill set for current combination of people
            skillset = set().union(*[valid_people[i][1] for i in idxs])

            # 6. Check if current combination of people contains all the skills.
            # If it does, return it as our answer.
            # Since we're using BFS and go from shortest to longest combination,
            # this combination is guaranteed to be the right answer.
            if len(skillset) == n:
                return [valid_people[i][0] for i in idxs]

            # Iterate for all the remaining people in `valid_people`
            for i in range(idxs[-1] + 1, m):
                # Check if we'll gain new skills by adding this person to combination.
                # If we won't, there's no point in adding such a combination to deque.
                if valid_people[i][1] - skillset:
                    d.append((idxs + (i, )))

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        # skill_map = { skill:idx for idx, skill in enumerate(req_skills)}
        skill_have = [0] * len(req_skills)
        self.res = []

        n = len(req_skills)
        # 1. Assign indexes for each skill string
        skills = {
            skill: i for i, skill in enumerate(req_skills)
        }
        # 2. Create sets with skill indexes for each person
        people = [(i, {skills[skill] for skill in person}) for i, person in enumerate(people)]
        # 3. Sort people by length of skillset
        people.sort(key=lambda x: len(x[1]))


        valid_people = []
        # 4. Iterate over people list and check if person's skill set 
        # is a subset of other person's skill set. If it is, ignore it,
        # otherwise, add it to `valid_people` list
        for idx, person in enumerate(people):
            i, skillset = person
            is_valid = True

            for j, s in people[idx + 1:]:
                if skillset.issubset(s):
                    is_valid = False
                    break

            if is_valid:
                valid_people.append((i, skillset))

        m = len(valid_people)

        print(valid_people)


        # @cache
        def find_subset(idx, skill_have, people_to_have):
            # print(idx, skill_have, people_to_have)

            flag = True
            for v in skill_have:
                if v == 0:
                    flag = False
            if flag:
                if len(self.res) == 0:
                    self.res = people_to_have.copy()
                else:
                    if len(self.res) > len(people_to_have.copy()):
                        self.res = people_to_have.copy()
                return 

            
            if idx == len(valid_people):
                return 

            for skill in valid_people[idx][1]:
                skill_have[skill] += 1
            people_to_have.append(valid_people[idx][0])
            find_subset(idx+1, skill_have, people_to_have)
            
            for skill in valid_people[idx][1]:
                skill_have[skill] -= 1
            people_to_have.pop()
            find_subset(idx+1, skill_have, people_to_have)
            
            
        
        find_subset(0, skill_have, [])
        # print(self.res)

        return self.res




        
