class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] будет хранить минимальное количество монет для суммы i
        # Инициализируем значением, которое больше любого возможного ответа (amount + 1)
        max_val = amount + 1
        dp = [max_val] * (amount + 1)
        
        # Базовый случай: для суммы 0 нужно 0 монет
        dp[0] = 0
        
        # Итерируемся по всем суммам от 1 до target amount
        for i in range(1, amount + 1):
            # Для каждой суммы i, пробуем использовать каждую монету c
            for coin in coins:
                if i >= coin:
                    # Обновляем dp[i]: минимальное из текущего значения или (1 + dp[i - coin])
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        # Если dp[amount] все еще равно max_val, значит сумму составить невозможно
        return dp[amount] if dp[amount] != max_val else -1
