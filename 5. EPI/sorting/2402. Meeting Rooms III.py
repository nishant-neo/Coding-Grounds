"""
You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

 

Example 1:

Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
Explanation:
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0. 
Example 2:

Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1
Explanation:
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 

"""


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings_sorted = sorted(meetings)
        rooms = [(i) for i in range(n)]
        heapq.heapify(rooms)
        room_count = {}
        meeting_ends = []

        for start,end in meetings_sorted:
            # releasing any availaible rooms before the meeting starts
            while len(meeting_ends) > 0 and meeting_ends[0][0] <= start:
                heapq.heappush(rooms, heapq.heappop(meeting_ends)[1])
            
            # assigning room
            if len(rooms) > 0:
                current_time = start
                room  = heapq.heappop(rooms)   
            # assigning a room that frees in future             
            else:
                current_time, room = heapq.heappop(meeting_ends)

            # print(f"star={start} end={end} current_time={current_time} room={room}")
            room_count[room] = room_count.get(room,0)+1
            heapq.heappush(meeting_ends, (max(start, current_time)+(end-start), room))


        max_meetings = max(room_count.values())
        print(room_count)
        for i in range(n):
            if max_meetings == room_count[i]:
                return i

        # print(room_count)

        # return 1
        # while (len(events)>0):
        #     # current_time = meeting[0]
        #     # for k,v in room_freetime.items():
        #     event  = heapq.heappop(events)
        #     # current_time = event[0]
        #     # if event[1] == 1:

        #     #     if len(rooms) > 0:
        #     #         room  = heapq.heappop(rooms)
        #     #         room_count[room] = room_count.get(room,0)
        #     #         # room_freetime[room] = current_time + meeting[1]
        #     #         heapq.heappush(events, (current_time + meeting[1], 0))
        #     #     else:
        #     if len(rooms)>0:
        #         room  = heapq.heappop(rooms)
        #         room_count[room] = room_count.get(room,0)

        #         event  = heapq.heappop(events)
        #         current_time = event[0][1]


    
