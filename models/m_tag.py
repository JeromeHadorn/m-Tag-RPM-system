# A class that performs m-Tag System like computation
from models import underline, MAX_ITERATIONS

class MTagSystem():
    def __init__(self, symbols, productions, m=2, verbose=True, max_iter=MAX_ITERATIONS):
        self.m = m
        self.symbols = symbols
        self.productions = productions
        self.verbose = verbose
        self.max_iter = max_iter

        self._validate()

    def _validate(self):
        if self.verbose:
            print("Validating...")
        pass
    
    def _validate_input(self, input):
        for sym in input:
            if sym not in self.symbols:
                raise ValueError(f"Symbol '{sym}' is not in Σ")
    
    def __repr__(self):
        return f"""Tag System of size: {len(self)}
        m : {self.m}
        Σ : {self.symbols}
        P : {self.productions}
        """ # TODO: Add nicer formatting

    def __len__(self):
        return self.m * len(self.symbols)

    def run(self, input, pyramid=False):
        input = input.split(" ")
        self._validate_input(input)
        
        iter = 0

        # 0. Check halting
        while not len(input) < self.m:

            # 1. Read current symbol
            cur_symbol = input[0]
            
            # Print current state on tape
            spaces = " " * iter * self.m if pyramid else ""
            print(spaces + underline(cur_symbol) + " " + " ".join(input[1:]))

            # 2. Delete first m symbols
            input = input[self.m:]

            # 3. Append production for current symbol
            input.extend(self.productions[cur_symbol])
            
            # 4. Increment iteration
            iter = iter + 1
            if iter > self.max_iter:
                print("Reached iteration limit...")
                break
        
        spaces = " " * iter * self.m if pyramid else ""
        print(spaces + " ".join(input)) 
        print(f"Halted on: '{' '.join(input)}'")
        