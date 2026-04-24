class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) != 1:
            stone1 = max(stones)
            stones.remove(stone1)
            stone2 = max(stones)
            stones.remove(stone2)

            new_stone = stone1 - stone2
            stones.append(new_stone)
        return stones[0]