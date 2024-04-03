from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = self.get_first(board, word)
        if len(start) == 0:
            return False
        if len(word) > len(board[0]) * len(board):
            return False
        visited = set()
        ok = self.finding_loop(board, word, start, 1, visited)
        return ok

    def finding_loop(self, board, word, next_loc, i, visited):
        if i == len(word):
            return True
        for cur_loc in next_loc:
            if cur_loc not in visited:
                visited.add(cur_loc)
                ok = self.find_neighbour_exists_and_location(board, cur_loc, word[i], visited)
                if len(ok) != 0:
                    answer = self.finding_loop(board, word, ok, i + 1, visited)
                    if answer:
                        return True
                visited.remove(cur_loc)
        return False

    def get_first(self, board, word):
        chr = word[0]
        answers = []
        set2 = []
        set_word = set(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                set2.append(board[i][j])
                if board[i][j] == chr:
                    answers.append((i, j))
        if set(set2).issubset(set_word) and len(word) > len(set2):
            return []
        return answers

    def find_neighbour_exists_and_location(self, board, location, char, visited):
        answers = []
        i, j = location
        if i - 1 >= 0:
            if board[i - 1][j] == char and (i - 1, j) not in visited:
                answers.append((i - 1, j))
        if j - 1 >= 0:
            if board[i][j - 1] == char and (i, j - 1) not in visited:
                answers.append((i, j - 1))
        if i + 1 < len(board):
            if board[i + 1][j] == char and (i + 1, j) not in visited:
                answers.append((i + 1, j))
        if j + 1 < len(board[0]):
            if board[i][j + 1] == char and (i, j + 1) not in visited:
                answers.append((i, j + 1))
        return answers
