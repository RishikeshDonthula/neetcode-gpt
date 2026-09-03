class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        def obj(x):
            return x**2
        x = init
        min = obj(x)
        for i in range(iterations):
            slope = 2*x
            x = x - learning_rate*slope
            value = obj(x)
            if value < min:
                min = value
            else:
                return round(x, 5)
        return round(x, 5)
        pass
