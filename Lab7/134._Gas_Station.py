class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Находит стартовую станцию, откуда можно обойти весь круг.
        Использует подход с одним проходом (O(n)).
        """
        n = len(gas)

        # Проверка общего баланса: если суммарный газ меньше суммарной стоимости,
        # то обойти круг невозможно.
        if sum(gas) < sum(cost):
            return -1
        current_tank = 0
        start_index = 0

        for i in range(n):
            # Разница между газом и стоимостью на данном отрезке
            diff = gas[i] - cost[i]
            current_tank += diff

            # Если баланс становится отрицательным, значит, мы не смогли доехать до станции i+1 
            # из текущей start_index. Поэтому нам нужно начать проверку со следующей станции (i+1).
            if current_tank < 0:
                current_tank = 0
                start_index = i + 1
        
        return start_index

