"""
911. Online Election
Solved
Medium
Topics
Companies
You are given two integer arrays persons and times. In an election, the ith vote was cast for persons[i] at time times[i].

For each query at a time t, find the person that was leading the election at time t. Votes cast at time t will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

Implement the TopVotedCandidate class:

TopVotedCandidate(int[] persons, int[] times) Initializes the object with the persons and times arrays.
int q(int t) Returns the number of the person that was leading the election at time t according to the mentioned rules.
 

Example 1:

Input
["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
Output
[null, 0, 1, 1, 0, 0, 1]

Explanation
TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
topVotedCandidate.q(3); // return 0, At time 3, the votes are [0], and 0 is leading.
topVotedCandidate.q(12); // return 1, At time 12, the votes are [0,1,1], and 1 is leading.
topVotedCandidate.q(25); // return 1, At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
topVotedCandidate.q(15); // return 0
topVotedCandidate.q(24); // return 0
topVotedCandidate.q(8); // return 1

 

Constraints:

1 <= persons.length <= 5000
times.length == persons.length
0 <= persons[i] < persons.length
0 <= times[i] <= 109
times is sorted in a strictly increasing order.
times[0] <= t <= 109
At most 104 calls will be made to q.
"""


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):

        self.persons = persons
        self.times = times
        self.standings = defaultdict(int)
        self.winner = []
        max_votes = 0

        for person, time in zip(persons, times):
            self.standings[person] += 1

            if max_votes <= self.standings[person]:
                max_votes = self.standings[person]
                self.winner.append(person)
            else:
                self.winner.append(self.winner[-1])

    
    def q(self, t: int) -> int:

        def get_idx_from_times(t):
            n = len(self.times)
            l, r = 0, n-1

            while l<=r:
                m = l + (r-l)//2
                if self.times[m] == t:
                    return m
                elif self.times[m] > t:
                    r = m-1
                else:
                    l = m+1
            return l-1
        # print(self.times)
        # print(self.winner)
        # return self.winner[bisect.bisect(self.times, t)-1]
        idx = get_idx_from_times(t)
        return self.winner[idx]

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
