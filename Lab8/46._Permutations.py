class Solution:    
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current_permutation = []
        used = [False] * len(nums)

        def backtrack():
            # Добавляем перестановку только тогда, когда она полная
            if len(current_permutation) == len(nums):
                result.append(list(current_permutation))
                return # Прерываем дальнейшую рекурсию для этой ветки

            for i in range(len(nums)):
                # Если число nums[i] еще не использовано
                if not used[i]:
                    # 1. Выбор: используем это число
                    used[i] = True
                    current_permutation.append(nums[i])

                    # 2. Рекурсивный вызов
                    backtrack()

                    # 3. Отмена выбора (Backtrack): возвращаем состояние
                    current_permutation.pop()
                    used[i] = False

        backtrack()
        return result

