


class Board:
    def __init__(self, input_board):
        self.board = []
        for row in input_board:
            temp = [[x, False] for x in row]
            self.board.append(temp)

    def has_won(self):
        # check row
        for row in self.board:
            if len(list(filter(lambda x: x[1] == True, row))) == 5:
                return True

        # check column
        for x in range(len(self.board[0])):
            column = [row[x] for row in self.board]
            if len(list(filter(lambda x: x[1] == True, column))) == 5:
                return True
        return False

    def get_score(self):
        score = 0
        for row in self.board:
            for col in row:
                if not col[1]:
                    score += col[0]
        return score

    def mark_number(self, num):
        for row in self.board:
            for col in row:
                if col[0] == num:
                    col[1] = True


def make_board(inp):
    board = []
    for line in inp.split("\n"):
        row = line.split(" ")
        if len(row) < 5:
            continue
        no_spaces_row = list(filter(lambda x: x, row))
        final_row = [int(x) for x in no_spaces_row]
        board.append(final_row)
    return Board(board)

with open('01.txt') as f:
    inp = f.read().split("\n\n")
    drawings = [int(x) for x in inp[0].split(",")]
    rest = inp[1:]

    bingo_cards = [make_board(x) for x in rest] 
    last_won = []
    last_won_num = -1
    for num in drawings:
        for card in bingo_cards:
            card.mark_number(num)

        for card_num in range(len(bingo_cards)):
            if card_num not in last_won and bingo_cards[card_num].has_won():
                last_won.append(card_num)
                last_won_num = num
                print("SCORE: ", bingo_cards[card_num].get_score() * num)

