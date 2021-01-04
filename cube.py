#### Guido Dipietro - 2021 ####

import numpy as np
import re

class Cube:
    # Piece def #
    co = np.array([0,0,0,0,0,0,0,0])                # 0 = oriented, 1 = cw, 2 = ccw
    cp = np.array([0,1,2,3,4,5,6,7])                # UBL UBR UFR UFL DFL DFR DBR DBL
    eo = np.array([0,0,0,0,0,0,0,0,0,0,0,0])        # UB UR UF UL BL BR FR FL DF DR DB DL
    ep = np.array([0,1,2,3,4,5,6,7,8,9,10,11])      # 0 = oriented, 1 = not
    xp = np.array([0,1,2,3,4,5])                    # U L F R B D

    # Atoms #
    def R(self):
        self.cp[[1,2,5,6]] = self.cp[[2,5,6,1]]
        self.co[[1,2,5,6]] = self.co[[2,5,6,1]]
        self.eo[[1,5,6,9]] = self.eo[[6,1,9,5]]
        self.ep[[1,5,6,9]] = self.ep[[6,1,9,5]]
        self.co = (self.co + [0,1,2,0,0,1,2,0]) % 3
    def U(self):
        self.cp[[0,1,2,3]] = self.cp[[3,0,1,2]]
        self.co[[0,1,2,3]] = self.co[[3,0,1,2]]
        self.eo[[0,1,2,3]] = self.eo[[3,0,1,2]]
        self.ep[[0,1,2,3]] = self.ep[[3,0,1,2]]
    def x(self):
        self.cp[[0,1,2,3,4,5,6,7]]              = self.cp[[3,2,5,4,7,6,1,0]]
        self.co[[0,1,2,3,4,5,6,7]]              = self.co[[3,2,5,4,7,6,1,0]]
        self.eo[[0,1,2,3,4,5,6,7,8,9,10,11]]    = self.eo[[2,6,8,7,3,1,9,11,10,5,0,4]]
        self.ep[[0,1,2,3,4,5,6,7,8,9,10,11]]    = self.ep[[2,6,8,7,3,1,9,11,10,5,0,4]]
        self.xp[[0,1,2,3,4,5]]                  = self.xp[[2,1,5,3,0,4]]
        self.co                                 = (self.co + [2,1,2,1,2,1,2,1]) % 3
        self.eo                                 = (self.eo + [1,0,1,0,0,0,0,0,1,0,1,0]) % 2
    def y(self):
        self.cp[[0,1,2,3,4,5,6,7]]              = self.cp[[3,0,1,2,5,6,7,4]]
        self.co[[0,1,2,3,4,5,6,7]]              = self.co[[3,0,1,2,5,6,7,4]]
        self.eo[[0,1,2,3,4,5,6,7,8,9,10,11]]    = self.eo[[3,0,1,2,7,4,5,6,9,10,11,8]]
        self.ep[[0,1,2,3,4,5,6,7,8,9,10,11]]    = self.ep[[3,0,1,2,7,4,5,6,9,10,11,8]]
        self.xp[[0,1,2,3,4,5]]                  = self.xp[[0,2,3,4,1,5]]
        self.eo                                 = (self.eo + [0,0,0,0,1,1,1,1,0,0,0,0]) % 2

    # Other moves #
    def L(self):
        self.apply("y2 R y2")
    def D(self):
        self.apply("x2 U x2")
    def F(self):
        self.apply("y' R y")
    def B(self):
        self.apply("y R y'")
    def z(self):
        self.apply("y' x y")
    def Rw(self):
        self.apply("L x")
    def Lw(self):
        self.apply("R x'")
    def Bw(self):
        self.apply("F z'")
    def Fw(self):
        self.apply("B z")
    def Uw(self):
        self.apply("D y")
    def Dw(self):
        self.apply("U y'")

    # Move functions associated to move strings
    func = {    "R": R,     "U": U,     "F": F,     "L": L,     "D": D,     "B": B,
                "Rw": Rw,   "Uw": Uw,   "Fw": Fw,   "Lw": Lw,   "Dw": Dw,   "Bw": Bw,
                "x": x,     "y": y,     "z": z  }
    # Reduces move to simple moves (R' = R R R, etc)
    def parse_move(self, m):
        if (len(m)==2 and m[1]=='w') or len(m)==1:
            return m
        return f"{m[:-1]} {m[:-1]} {m[:-1]}" if m[-1]=="'" else f"{m[:-1]} {m[:-1]}"

    # Applies a string of moves to the Cube object
    def apply(self, seq):
        seq = ' '.join([self.parse_move(m) for m in seq.split()]).split()
        for move in seq:
            self.func[move](self)

    # Check if a single move is valid
    def fit(self, m):
        match = re.match("(([RFULDB]w?)|([xyz]))['2]?", m)
        return True if match.group()==m else False
    # Check if a move string has all valid moves
    def isclean(self, seq):
        return all([self.fit(m) for m in seq.split()])

    # Resets everything to solved
    def flush(self):
        self.co = np.array([0,0,0,0,0,0,0,0])
        self.cp = np.array([0,1,2,3,4,5,6,7])
        self.eo = np.array([0,0,0,0,0,0,0,0,0,0,0,0])
        self.ep = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
        self.xp = np.array([0,1,2,3,4,5])

    # Check if a move string solves the cube
    # Ugly, don't watch
    is_sorted = lambda self, x: (np.diff(x)>=0).all()
    def check(self, scr, sol):
        if not self.isclean(sol):
            self.flush()
            return -1
        self.apply(scr)
        self.apply(sol)
        # choo choo
        if not self.co.all() and not self.eo.all() and self.is_sorted(self.cp) and self.is_sorted(self.ep) and self.is_sorted(self.xp):
          return len(sol.split())
        self.flush()
        return -1

# cube = Cube()
# scramble = "R' U' F L2 B2 U2 B2 R2 D' B2 D' B2 F2 U2 B L B2 R B2 D' B L U2 Lw' Fw' Rw z y x y2 z2 y' y"
# solution = "B R B R2 F2 D2 F U2 F' D2 F2 L2 B' D2 B' R' F2 R' U2 F D' R' B' U'"
# print(cube.check(scramble, solution))
