# eas501-newtonRaphson

Write a python function with a call of `x = newtonRaphson(g, x0, eps, delta, itermax)` which used the Newton-Raphson method which returns the root of a function `g`. The inputs are:
 - `g`: A function which returns `f, fx = g(x)` where `f` is the function value and `fx` is the function derivative evaluated at `x`.
 - `x0`: The initial guess at the root.
 - `eps`: The tolerance to use. Consider the method converged when the magnitude of the full step is less than this value.
 - `delta`: Criteria for divergence. Consider the method as diverging when the magnitude of the full step is more than this value. If the method is diverging raise an exception with this exact error message: `Error: Maximum Number of Iterations`</li>
 - `itermax`: The maximum number of iterations. If the maximum number of iteration is exceeded raise an exception with this exact error message: `Error: Divergence`
 
You can test your code by running `python newtonRaphson_unit.py` in the same directory as your `newtonRaphson.py` file.

*NOTE:* This is an individual programming project.
