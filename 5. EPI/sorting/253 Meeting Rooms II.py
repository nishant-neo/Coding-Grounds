class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        meeting_end = []
        room_count = 0

        room_rqd = 0

        for start,end in intervals:
            # freeing up any rooms that is availaible
            while(len(meeting_end)>0 and meeting_end[0]<= start):
                heapq.heappop(meeting_end)
                room_count -= 1

            # starting a room with a new room
            heapq.heappush(meeting_end,end)
            room_count += 1

            room_rqd = max(room_rqd,room_count)


        return room_rqd
