

class Solution:
    def words_in_dict(self, thesaurus, text):
        # создаем словарь из "хороших" слов
        good_words = set(thesaurus)
        for word in thesaurus:
            # Для каждого слова и словаря добавляем "плохое" слово - слово без 1 буквы
            for del_pos in range(len(word)):
                # делаем срез до индекса
                start_word = word[:del_pos]
                # делаем срез от индекса + 1 до конца слова
                end_word = word[del_pos + 1:]
                # print(f"->> DEBUG '{start_word}', '{end_word}'")
                # Склеиваем и добавляем в словарь
                good_words.add(start_word + end_word)
        print(good_words)
        result = []
        for word in text.split(' '):
            if word in good_words:
                result.append(word)
        return result



if __name__ == "__main__":
    """
        Ссылка: 
        Дано: Дан словарь из N слов, длина каждого не превосходит K
        Необходимо:
            В записи каждого из M слов текста (каждое длиной K) может быть пропущена одна буква.
            Для каждого слова сказать, входит ли оно (возможно с одной пропущенной буквой) в словарь
        Примечание: 
        Решение:
            Выбросим из каждого слова словаря по одной букве, всеми возможными способами за O(NK).
            Для каждого слова из текста, проверим если ли оно в словаре
        Сложность алгоритма: O(NK^2 + M)
    """
    solution = Solution()
    print(solution.words_in_dict(['привет'], 'привет мир, пивет'))
