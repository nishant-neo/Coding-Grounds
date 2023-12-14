"""
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
"""
class SnapshotArray:

    def __init__(self, length: int):
        
        self.snap_id = 0
        self.cache = [[[0, 0]] for i in range(length)]
        # self.arr = {self.snap_id:0}*length
        

    def set(self, index: int, val: int) -> None:
        self.cache[index].append([self.snap_id, val])
        

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    @lru_cache(maxsize=None)
    def get(self, index: int, snap_id: int) -> int:
        # print(self.snaps[snap_id])
        # we are getting the rightmost entry for the index, if the snap_id is missing
        # it will give the index of last snap_id, which is stored in last index i.e. idx-1
        idx = bisect.bisect_right(self.cache[index], [snap_id, 10**9]) 
        return self.cache[index][idx-1][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
