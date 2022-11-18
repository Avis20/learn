

class Solution:
    def checkRecord(self, s: str) -> bool:
        count_absent = 0
        count_late = 0
        for c in s:
            if c == "A":
                count_absent += 1
            if c == "L":
                count_late += 1
            else:
                count_late = 0
            
            if count_absent >= 2:
                return False
            if count_late >= 3:
                return False
        return True


if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/student-attendance-record-i/description/
        Дано: Дана строка посещения студента
        Необходимо: Вернуть True если он пропустил 1 день, и не опаздывал 3 дня подряд
        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    solution = Solution()
    s = "LALL"
    print(solution.checkRecord(s))
