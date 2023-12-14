"""
A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.

Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a four-person group in the middle, which means to have two people on each side.
"""

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rowwise_occupied_seats = {}
        set_middle = set([2,3,4,5,6,7,8,9])
        for r, c in reservedSeats:
            if r in rowwise_occupied_seats:
                rowwise_occupied_seats[r].append(c)
            else:
                rowwise_occupied_seats[r] = [c]

        count = 2*n
        for r, cs in rowwise_occupied_seats.items():                
            cs = set(cs)
            tcount = 0
            
            if not (set_middle & cs):
                tcount = 2
            
            elif not (cs & set([4, 5, 6, 7])):
                tcount = 1       

            elif not (cs & set([2, 3, 4, 5])):
                tcount = 1        

            elif not (cs & set([6, 7, 8, 9])):
                tcount = 1 

            count = count - (2-tcount)


        return count





            
