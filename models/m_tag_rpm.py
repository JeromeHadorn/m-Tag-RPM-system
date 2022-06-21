from models.m_tag import MTagSystem
from models import MAX_ITERATIONS, DEFAULT_SYMBOL, underline

# create a class that inherits from MTagSystem
class MTagRPM(MTagSystem):

    def __init__(self,symbols, productions,reading_rules, start_state=0, m=2, verbose=True, max_iter=MAX_ITERATIONS):
        super().__init__(symbols=symbols, productions=productions, m=2, verbose=verbose, max_iter=max_iter)
        self.start_state = start_state
        self.reading_rules = reading_rules
        
        self._validate()
    
    def _validate(self):
        pass

    def __len__(self):
        return super().__len__() + len(self.reading_rules) + 1
    
    def __repr__(self):
        return f"""Tag System of size: {len(self)}
        m  : {self.m}
        Σ  : {self.symbols}
        P  : {self.productions}
        q0 : {self.start_state}
        δ  : {self.reading_rules}
        """ # TODO: Add nicer formatting
    
    def run(self, input, pyramid=False):
        input = input.split(" ")
        super()._validate_input(input)
        
        iter = 0
        reading_pos = self.start_state
        
        # 0. Check halting
        while not len(input) < self.m:

            # 1. Read current symbol
            cur_sym = input[reading_pos]

            # Print current state on tape
            underlined_input = input
            underlined_input[reading_pos] = underline(underlined_input[reading_pos])
            spaces = " " * iter * self.m if pyramid else ""
            print(spaces + " ".join(underlined_input))

            # 2. Determine next reading position
            if cur_sym in self.reading_rules[reading_pos]:
                reading_pos = self.reading_rules[reading_pos][cur_sym]
            else:
                reading_pos = self.reading_rules[reading_pos][DEFAULT_SYMBOL]

            # 3. Delete first m symbols
            input = input[self.m:]
            
            # 4. Append production for current symbol
            input.extend(self.productions[cur_sym])
            
            # 5. Increment iteration
            iter = iter + 1
            if iter > self.max_iter:
                print("Reached iteration limit...")
                break
        
        print(f"Halted on: '{' '.join(input)}'")