#!/usr/bin/env python3

''' *****************
    *               *
    * Ugly Code by  *
    *               *
    *  Cisco, 2021  *
    *               *
    ***************** '''

import re
from sympy import Matrix, lcm

class BalanceChemicalEquation:
    def __init__(self):
        self.elementList = []
        self.elementMatrix = []

    def addToMatrix(self, element, index, count, side):
        if element not in self.elementList:
            self.elementList.append(element)
            for row in self.elementMatrix:
                row.append(0)
        column = self.elementList.index(element)
        self.elementMatrix[index][column] += count * side

    def findElements(self, segment, index, multiplier, side):
        elements_and_numbers = re.findall('([A-Z][a-z]?)([0-9]*)', segment)
        for element, count in elements_and_numbers:
            count = int(count) if count else 1
            self.addToMatrix(element, index, count * multiplier, side)

    def compoundDecipher(self, compound, index, side):
        segments = re.findall('(\([A-Za-z0-9]+\)([0-9]+)|[A-Za-z0-9]+)', compound)
        for segment, multiplier in segments:
            if segment.startswith("("):
                multiplier = int(multiplier)
                segment = segment[1:-1]
            else:
                multiplier = 1
            self.findElements(segment, index, multiplier, side)

    def balance(self, reactants, products):
        num_reactants = len(reactants)
        self.elementMatrix = [[0] * len(self.elementList) for _ in range(num_reactants + len(products))]

        for i, reactant in enumerate(reactants):
            self.compoundDecipher(reactant, i, 1)
        for i, product in enumerate(products):
            self.compoundDecipher(product, i + num_reactants, -1)

        elementMatrix = Matrix(self.elementMatrix).transpose()
        solution = (lcm([val.q for val in elementMatrix.nullspace()[0]]) * elementMatrix.nullspace()[0]).tolist()
        return ' + '.join(f'{coef[0]}{comp}' for coef, comp in zip(solution, reactants)) + ' -> ' + ' + '.join(f'{coef[0]}{comp}' for coef, comp in zip(solution[num_reactants:], products))

def main():
    print("Please input your reactants, this is case sensitive")
    print("Your input should look like: H2O+Ag3(Fe3O)4")
    reactants = input("Reactants: ").replace(' ', '').split("+")
    products = input("Products: ").replace(' ', '').split("+")
    
    balancer = BalanceChemicalEquation()
    balanced_equation = balancer.balance(reactants, products)
    print(balanced_equation)

if __name__ == "__main__":
    main()
