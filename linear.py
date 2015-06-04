def Hypothesis(theta,x):
	h = x[0] * theta[0] + (x[1] * theta[1])
	return h

def Cost_Function(X,Y,theta,m):
	sumOfSqErr = 0
	for i in xrange(m):
		x = X[i]
		hi = Hypothesis(theta,x)
		yi = Y[i]
		diff = (hi - yi)
		sqErr = diff**2
		sumOfSqErr += sqErr
	m = len(Y)
	constant = float(1) / float(2*m)
	J = constant * sumOfSqErr
	return J


def Cost_Function_Derivative(X,Y,theta,j,m):
	sumOfErr = 0
	for i in xrange(m):
		x = X[i]
		hi = Hypothesis(theta,x)
		yi = Y[i]
		diff = (hi - yi)
		err = diff*x[j]
		sumOfErr += err
	m = len(Y)
	constant = float(1) / float(m)
	J = constant * sumOfErr
	return J


def Gradient_Descent(X,Y,theta, m, alpha):
	new_theta =[]
	constant = float(alpha) / float(m)
	for j in xrange(len(theta)):
		CFDerivative = Cost_Function_Derivative(X,Y,theta,j,m)
		new_theta_j = theta[j] - constant * CFDerivative
		new_theta.append(new_theta_j)
	return new_theta



def Linear_Regression(X,Y,alpha,theta,num_iters):
	m = len(X)
	for x in xrange(num_iters):
		new_theta = Gradient_Descent(X,Y,theta, m, alpha)
		theta = new_theta
		if x % 100 == 0:
			print 'theta ', theta
			print 'cost is ', Cost_Function(X,Y,theta,m)
	return new_theta



# data to pass into the function as paramters 
# returns theta [18.28413213512223, 0.7465589666893538] after fitting the data

#y_raw = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
#x_raw = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9]]
#theta = [4,3]
#alpha = 0.1
#iterations = 2000
#Linear_Regression(x_raw,y_raw,alpha,theta,iterations)


