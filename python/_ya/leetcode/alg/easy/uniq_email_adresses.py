

class Solution:
    def numUniqueEmails(self, emails: list[str]):
        uniq = set()
        for email in emails:
            email.strip()
            local_name, domain = email.split("@")
            local_name = "".join(local_name.split("."))
            local_name = local_name.split("+")[0]
            uniq.add(local_name + "@" + domain)
        return len(uniq)


if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/unique-email-addresses/
        Дано: Дан список имейл адресов
        Необходимо: Вернуть кол-во уникальных имейл адресов на которые будет отправлены письма
        Пример: alice@leetcode.com, "alice" - это локальное имя `local name`. "leetcode.com" - домен, `domain`
        Примечание:
            1) Если в local name встречается точка ".", то она будет проигнорированна
                Т.е. "a.lice@leetcode.com" = "alice@leetcode.com"
                Не работает на домене "e@leetcode.com" != "a@leet.code.com"
            2) Если в домене встречается плюс "+", то все символы после него пропускаются
                Т.е. "a+lice@leetcode.com" = "a@leetcode.com"
        Решение: 
        Сложность алгоритма:
    """
    solution = Solution()
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"
    ]
    emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
    print(solution.numUniqueEmails(emails))
