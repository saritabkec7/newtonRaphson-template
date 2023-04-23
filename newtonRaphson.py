def newtonRaphson(g, x0, eps, delta, itermax):
	#Determine the root of a function g(x) using an initial guess of x0.
	#
	#	Inputs:
	#		g - the function handle that returns [f, fx] evaluated at x.
	#		x0 - initial guess.
	#		eps - The tolerance to use.
	#		delta - divergence criteria.
	#		itermax - the maximum number of iterations.
	#
	#	Outputs:
	#		x - the root of the function.
	#		iter - the number of iterations required to obtain the root.

	iter = 1 # initial iteration

	while iter < itermax: # condition where iteration is less than maximum iteration
		f,fx = g(x0) # g function defined
		x = x0 - (f/fx) # the Newton Raphson method uses this formula to find next value of x using the previous value(x0)
    
		if abs(x-x0)<eps: # condition for converged
			break
    
		if abs(x-x0)>delta: # condition for divergence
			raise Exception ("Error: Divergence") # raise an exception for divergence
    
		x0 = x
		iter = iter + 1 # incrementing iteration
    
	if(iter>=itermax): # if condition for the maximum number of iteration is exceeded
		raise Exception ( "Error: Maximum Number of Iterations") # raise an exception for maxiteration

	return x, iter # final result
