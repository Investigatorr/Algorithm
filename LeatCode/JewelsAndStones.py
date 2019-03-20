class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # J보석 / S돌멩이
        # 결과를 담을 변수 선언
        number = 0
        for i in J:
            number += S.count(i)
        # 인덴트 잘못하면 틀린문제 된다.
        return number