class Solution:
    def average2(self, salary: list[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary) / len(salary)

    def average(self, salary: list[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)

if __name__ == "__main__":
    """
    Ссылка:
    Дано: Дан список уникальных целых чисел `salary`, где salary[i] - зарплата i-го сотрудника
    Необходимо: Посчитать среднюю зарплату сотрудников, убрав самую маленькую и самую большую зарплату
    Примечание:
    Решение:
    Сложность алгоритма:
    """
    solution = Solution()
    salary = [4000, 3000, 1000, 2000]
    print(solution.average(salary))
