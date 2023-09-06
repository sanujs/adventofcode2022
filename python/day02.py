def part_one():
    def round_outcome(opp, you):
        convert_opp = {
            "A": "X",
            "B": "Y",
            "C": "Z",
        }
        opp = convert_opp[opp]
        if you == opp:
            return 3
        if opp == "X" and you == "Y" or \
            opp == "Y" and you == "Z" or \
            opp == "Z" and you == "X":
            return 6
        return 0

    with open("input.txt") as f:
        # A/X = Rock (1)
        # B/Y = Paper (2)
        # C/Z = Scissors (3)
        score_determinator = {
            "X": 1,
            "Y": 2,
            "Z": 3,
        }
        your_score = 0
        for line in f:
           opp, you = line.strip().split(" ")
           your_score += score_determinator[you]
           your_score += round_outcome(opp, you)
    return your_score


def part_two():
    def shape_points(opp, outcome):
        score_determinator = {
            "A": 1,
            "B": 2,
            "C": 3,
        }
        if outcome == "Y":
            return score_determinator[opp]
        if outcome == "X" and opp == "C" or \
            outcome == "Z" and opp == "A":
            return score_determinator["B"]
        if outcome == "X" and opp == "B" or \
            outcome == "Z" and opp == "C":
            return score_determinator["A"]
        return score_determinator["C"]

    with open("input.txt") as f:
        # X = lose
        # Y = draw
        # Z = win
        round_outcome = {
            "X": 0,
            "Y": 3,
            "Z": 6,
        }
        your_score = 0
        for line in f:
            opp, outcome = line.strip().split(" ")
            your_score += round_outcome[outcome]
            your_score += shape_points(opp, outcome)
        return your_score
            
if __name__ == "__main__":
    print(part_one())
    print(part_two())