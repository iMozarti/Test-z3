HumanSide = [Or(Human[i] == 0, Human[i] == 1) for i in range(Num)]
from z3 import *

s = Solver()
Num = 10

Human = [Int('Human_%i' % (i + 1)) for i in range(Num)]
Wolf = [Int('Wolf_%i' % (i + 1)) for i in range(Num)]
Goat = [Int('Goat_%i' % (i + 1)) for i in range(Num)]
Cabbage = [Int('Cabbage_%i' % (i + 1)) for i in range(Num)]

# 0 - левый берег, 1 - правый берег
WolfSide = [Or(Wolf[i] == 0, Wolf[i] == 1) for i in range(Num)]
GoatSide = [Or(Goat[i] == 0, Goat[i] == 1) for i in range(Num)]
CabbageSide = [Or(Cabbage[i] == 0, Cabbage[i] == 1) for i in range(Num)]
Side = HumanSide + WolfSide + GoatSide + CabbageSide

Start = [Human[0] == 0, Wolf[0] == 0, Goat[0] == 0, Cabbage[0] == 0]
Finish = [Human[9] == 1, Wolf[9] == 1, Goat[9] == 1, Cabbage[9] == 1]

# Допустимые условия задачи
Safe = [And(Or(Wolf[i] != Goat[i], Wolf[i] == Human[i]), Or(Goat[i] != Cabbage[i], Goat[i] == Human[i])) for i in
        range(Num)]

Travel = [Or(
    And(Human[i] == Human[i + 1] + 1, Wolf[i] == Wolf[i + 1] + 1, Goat[i] == Goat[i + 1], Cabbage[i] == Cabbage[i + 1]),
    And(Human[i] == Human[i + 1] + 1, Goat[i] == Goat[i + 1] + 1, Wolf[i] == Wolf[i + 1], Cabbage[i] == Cabbage[i + 1]),
    And(Human[i] == Human[i + 1] + 1, Cabbage[i] == Cabbage[i + 1] + 1, Wolf[i] == Wolf[i + 1], Goat[i] == Goat[i + 1]),
    And(Human[i] == Human[i + 1] - 1, Wolf[i] == Wolf[i + 1] - 1, Goat[i] == Goat[i + 1], Cabbage[i] == Cabbage[i + 1]),
    And(Human[i] == Human[i + 1] - 1, Goat[i] == Goat[i + 1] - 1, Wolf[i] == Wolf[i + 1], Cabbage[i] == Cabbage[i + 1]),
    And(Human[i] == Human[i + 1] - 1, Cabbage[i] == Cabbage[i + 1] - 1, Wolf[i] == Wolf[i + 1], Goat[i] == Goat[i + 1]),
    And(Wolf[i] == Wolf[i + 1], Goat[i] == Goat[i + 1], Cabbage[i] == Cabbage[i + 1])) for i in range(Num - 1)]

solve(Side + Start + Finish + Safe + Travel)
