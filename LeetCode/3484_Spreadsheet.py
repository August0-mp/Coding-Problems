class Spreadsheet:

    def __init__(self, rows: int):
        self.labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.sheet = {}

        for label in self.labels:
            self.sheet[label] = [0 for _ in range(rows)]
    
    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell[0]][int(cell[1::])-1] = value

    def resetCell(self, cell: str) -> None:
        self.sheet[cell[0]][int(cell[1::])-1] = 0

    def getValue(self, formula: str) -> int:
        f = formula[1::].split('+')

        if f[0][0] in self.labels:
            a = self.sheet[f[0][0]][int(f[0][1::])-1]
        else:
            a = int(f[0])
        if f[1][0] in self.labels:
            return a + self.sheet[f[1][0]][int(f[1][1::])-1]
        else:
            return a + int(f[1])
        
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

# https://leetcode.com/problems/design-spreadsheet