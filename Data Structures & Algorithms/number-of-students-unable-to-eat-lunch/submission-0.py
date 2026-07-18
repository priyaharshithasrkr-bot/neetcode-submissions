class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]

        # Count student preferences
        for student in students:
            count[student] += 1

        # Process sandwiches
        for i, sandwich in enumerate(sandwiches):
            if count[sandwich] == 0:
                return len(sandwiches) - i
            count[sandwich] -= 1

        return 0