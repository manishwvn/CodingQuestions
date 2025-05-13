class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        students = deque(students)
        sandwiches = deque(sandwiches)
        cycle = 0

        while sandwiches and cycle < len(students):
            if students[0] == sandwiches[0]:
                sandwiches.popleft()
                students.popleft()
                cycle = 0
            else:
                students.append(students.popleft())
                cycle += 1
        
        return len(students)
        