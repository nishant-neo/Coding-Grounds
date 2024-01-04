"""
You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.
"""

class Solution:
    # def __init__(self):
        # self.heap = []  # maxHeap, minHeap (python default)
        
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        # result, heap = [], []
        # cur_task_index = 0
        # cur_time = tasks[0][0]
        
        # while len(result) < len(tasks):
        #     while (cur_task_index < len(tasks)) and (tasks[cur_task_index][0] <= cur_time):
        #         heapq.heappush(heap, (tasks[cur_task_index][1], tasks[cur_task_index][2]))
        #         cur_task_index += 1
        #     if heap:
        #         time_difference, original_index = heapq.heappop(heap)
        #         cur_time += time_difference
        #         result.append(original_index)
        #     elif cur_task_index < len(tasks):
        #         cur_time = tasks[cur_task_index][0]
                
        # return result
        heap = []
        ans = []
        current_time = 0
        tasks = sorted([((t[0], t[1]), i) for i,t in enumerate(tasks)])

        for ((enq, pro), i) in tasks:
            # If there is anything in heap or if there is a task that is awaited in the future
            # If the task has to be started before the current time, then 
            while(len(heap)>0 and current_time<enq):
                pro_j, j, enq_j = heappop(heap)
                current_time = max(current_time, enq_j) + pro_j
                ans.append(j)
            # if len(heap)>0 and current_time>=enq:

            heappush(heap, (pro, i, enq))

        # print(ans)
        ans = ans + [i[1] for i in sorted(heap)]
        # print(ans)

        return ans

        
        # result, heap = [], []
        # cur_task_index = 0
        # cur_time = tasks[0][0]

        #  while len(result) < len(tasks):
        #     while (cur_task_index < len(tasks)) and (tasks[cur_task_index][0] <= cur_time):
        #         heapq.heappush(heap, (tasks[cur_task_index][1], tasks[cur_task_index][2]))
        #         cur_task_index += 1
        #     if heap:
        #         time_difference, original_index = heapq.heappop(heap)
        #         cur_time += time_difference
        #         result.append(original_index)
        #     elif cur_task_index < len(tasks):
        #         cur_time = tasks[cur_task_index][0]
        
