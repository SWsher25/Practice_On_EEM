class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(remaining_target: int, current_combination: List[int], start_index: int):
            if remaining_target == 0:
                result.append(list(current_combination))
                return

            if remaining_target < 0 or start_index >= len(candidates):
                return

            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                
                # Выбор
                current_combination.append(candidate)
                
                # Рекурсивный вызов: передаем i, так как числа можно использовать повторно
                backtrack(remaining_target - candidate, current_combination, i)
                
                # Отмена выбора (Backtrack)
                current_combination.pop()

        backtrack(target, [], 0)
        return result

