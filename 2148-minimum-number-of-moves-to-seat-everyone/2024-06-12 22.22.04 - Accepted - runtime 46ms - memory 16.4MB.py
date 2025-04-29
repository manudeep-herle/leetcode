class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0

        for student, seat in zip(students, seats):
            res += abs(student - seat)
        
        return res
        