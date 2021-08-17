
def areInterwoven(one, two, three, i, j, table):
    if table[i][j] is not None:
        return table[i][j]

    k = i + j
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        table[i][j] = areInterwoven(one, two, three, i + 1, j, table)
        if table[i][j]:
            return True

    if j < len(two) and two[j] == three[k]:
        table[i][j] = areInterwoven(one, two, three, i, j+1, table)
        if table[i][j]:
            return True

    table[i][j] = False
    return False


class Solution:
    def isInterleave(self, one: str, two: str, three: str) -> bool:
        if len(three) != len(one) + len(two):
            return False

        table = [[None for _ in range(len(two) + 1)]
                 for _ in range(len(one) + 1)]

        return areInterwoven(one, two, three, 0, 0, table)
