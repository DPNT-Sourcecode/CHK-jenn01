
class SumSolution:
    
    def compute(self, x, y):
        try:
            
            if 0 <= x <= 100 and 0 <= y <= 100:
                return x + y
            else:
                raise ValueError("Argument should be between 0 and 100")
        except ValueError:
            raise ValueError("Argument should be between 0 and 100")
