class DPLL:
    true_lit = set()
    false_lit = set()
    props, branches = 0, 0
    cnf = []
    literals = []
    
    def __init__(self, formula):
               
        self.literals = [literal for literal in list(set(formula)) if literal.isalpha()]
        self.cnf = formula.split(", ")
        print("Input = \t", self)
        
        
    def __str__(self):
                
        cnf_str = ""
        
        for clause in self.cnf:  
            if len(clause) > 0:
                cnf_str += '(' + clause.replace(' ', ' ∨ ') + ') ∧ '
    
        if cnf_str == "":       
            cnf_str = "()"
            
        if cnf_str[-2] == "∧":  
            cnf_str = cnf_str[:-2:] 
    
        return cnf_str
    
    
    def DPLL_func(self):
    
        new_true_lit  =  []
        new_false_lit =  []
        
        print("\nCurrent Formula:\t", self)
        
        self.true_lit = set(self.true_lit)
        self.false_lit = set(self.false_lit)
        
        self.branches += 1  
        
        cnf = list(set(self.cnf))
        unit_clauses = [clause for clause in cnf if len(clause) < 3]   
        unit_clauses = list(set(unit_clauses))
        
        if unit_clauses:  
            for unit in unit_clauses:
                self.props += 1
                
                if '¬' in unit:  
                    self.false_lit.add(unit[-1])
                    new_false_lit.append(unit[-1])
                    i = 0
                    
                    while True:
                        if unit in cnf[i]:  
                            cnf.remove(cnf[i])
                            i -= 1
                        
                        elif unit[-1] in cnf[i]:  
                            cnf[i] = cnf[i].replace(unit[-1], '').strip()
                    
                        i += 1
                    
                        if i >= len(cnf):
                            break
        
                else:  
                    self.true_lit.add(unit)
                    new_true_lit.append(unit)
                    i = 0
                
                    while True:
                        if '¬' + unit in cnf[i]: 
                            cnf[i] = cnf[i].replace('¬' + unit, '').strip()
                        
                            if '  ' in cnf[i]:  
                                cnf[i] = cnf[i].replace('  ', ' ')
                        
                        elif unit in cnf[i]:  
                            cnf.remove(cnf[i])
                            i -= 1
                            
                        i += 1
                        
                        if i >= len(cnf):
                            break
        
        self.cnf = cnf
        
        print("Current Unit Clauses:\t", unit_clauses)
        print("CNF after Propagation:\t", self)
        
        if len(self.cnf) == 0:  
            return True
        
        if sum(len(clause) == 0 for clause in cnf):  
            for literal in new_true_lit:   
                self.true_lit.remove(literal)
            
            for literal in new_false_lit:  
                self.false_lit.remove(literal)
                
            print("\nBacktrack on encountering Null Clause")
            
            return False  
        
        self.literals = [literal for literal in list(set(''.join(self.cnf))) if literal.isalpha()]
        
        
        first_literal = self.literals[0]  
        
        self.cnf = cnf + [first_literal]  
        print("\nTrying with {0} as True!".format(first_literal))
        
        if self.DPLL_func():  
        
        self.cnf = cnf + ['¬' + first_literal]  
        print("\nTrying with ¬{0} as True!".format(first_literal))
        
        if self.DPLL_func():  
            return True
        
        
        else:  
            self.cnf = cnf
            
            for literal in new_true_lit:   
                self.true_lit.remove(literal)
            
            for literal in new_false_lit:  
                self.false_lit.remove(literal)
            
            return False 
        
    
    def print_result(self, checker):
        
        if checker == True:
            print("\nSatisfiable CNF")
        
            for literal in self.true_lit:
                print("\t"+literal, "= True")
                
            for literal in self.false_lit:
                print("\t"+literal, "= False")
            
        else:
            print("\nUnsatisfiable CNF!")
            
        print("\nBranches:\t\t", self.branches)
        print("\nUnit Propagations:\t", self.props)

'''
dpll_solver = DPLL(input("Enter a formula in CNF: "))
checker = dpll_solver.DPLL_func()
dpll_solver.print_result(checker)
'''