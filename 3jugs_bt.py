class ThreeJugs():
    def __init__(self):
        self.state = [0, 0, 5]
        self.maximum = [2, 3, 5]
        self.operators = [ [0,1], [0,2], [1,0], [1,2], [2,0], [2,1] ]
        self.applicable = [ ]
        self.node = []

    def isValid(self):
        sum = 0
        for i in range(len(self.state)):
            sum += self.state[i]
            if self.state[i] < 0 or self.state[i] > self.maximum[i]:
                return False
        return sum == self.maximum[2]
    
    def isGoalState(self):
        return self.state[2] == 4

    def isValidOperation(self, from_where, to_where):
        return (from_where > -1) and (from_where < 3) and (to_where > -1) and (to_where < 3) and (from_where != to_where) and (self.state[from_where] != 0) and (self.state[to_where] != self.maximum[to_where])

    def pour(self, from_where, to_where):
        if not(self.isValidOperation(from_where, to_where)):
            print("The requested operation is not valid...")
            return

        value = min(self.state[int(from_where)], self.maximum[int(to_where)] - self.state[int(to_where)])

        self.state[int(from_where)] -= value
        self.state[int(to_where)] += value

    def printState(self):
        print("")
        print("{", end="")
        for i in range(0,3):
            if i > 0:
                print(", ", end="")
            print(self.state[i], end="")
        print("}")

    def solve(self):
        while not(self.isGoalState()):
            
            # az allapotot rogzitjuk az utvonalban
            self.node.append(list(self.state))
            self.applicable.clear()

            # megkeressuk az osszes hasznalhato operatort az allapotra
            # es elmentjuk egy veremben
            for f in range(3):
                for t in range(3):
                    if self.isValidOperation(f, t):
                        self.applicable.append([f, t])
            #print("node:", self.node, "operators:", self.applicable) # 2,1 - 2,0

            # valasztunk egy operatort a hasznalhatoak kozul
            # megjegyzes: ebben a for ciklusban mindig az utolso elemet fogja valasztani
            for op in self.applicable:
                from_where = op[0]
                to_where = op[1]

                #print("selected operator:", from_where, to_where)

                # alkalmazzuk az ontest, ami egy uj allapotot eredmenyez
                self.pour(from_where, to_where)
                print("new state:", self.state)
                
                # ha az uj allapot benne van mar az utvonalban, akkor
                # valasztunk egy masik operatort
                # mivel az utolsot hasznaltuk a legutobb, ezert
                # kivesszuk az utolso operatort a hasznalhatoak kozul
                ################################################################
                # ha nincs benne, akkor rogzitjuk az allapotot es az alkalmazott operatort
                if self.state in self.node:
                    self.applicable.pop()
                    self.state = self.node[-1]
                    continue
                else:
                    self.node.append(list([from_where, to_where]))
                    self.node.append(list(self.state))
                    
            
            print("node:", self.node, "operators:", self.applicable) # 2,1 - 2,0
            break



def main():
    jugs = ThreeJugs()
    jugs.solve()


##################################################################################

if __name__ == "__main__":
    main()
