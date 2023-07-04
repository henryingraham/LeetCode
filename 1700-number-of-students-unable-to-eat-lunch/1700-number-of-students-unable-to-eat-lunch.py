class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = 0
        while count < len(students):
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
                count = 0
            else:
                temp = students.pop(0)
                students.append(temp)
                count += 1

        return len(students)