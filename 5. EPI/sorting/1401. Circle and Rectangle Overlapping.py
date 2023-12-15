"""
1401. Circle and Rectangle Overlapping
Medium

Companies
You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any point (xi, yi) that belongs to the circle and the rectangle at the same time.


"""


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        # square_points = [[x1, y1], [x2, y2], [x1, y2], [x2, y1]]

        nearest_x  = max(x1, min(x2, xCenter))
        nearest_y  = max(y1, min(y2, yCenter))

        return (nearest_x-xCenter)**2 + (nearest_y-yCenter)**2 - radius**2  <= 0
