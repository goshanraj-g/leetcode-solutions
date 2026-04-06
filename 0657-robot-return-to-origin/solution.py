class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # counter for l, r, u , p
        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")

