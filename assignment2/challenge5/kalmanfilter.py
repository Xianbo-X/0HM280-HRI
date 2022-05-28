import numpy as np

def prediction(mu:np.matrix,sigma:np.matrix,u,A:np.matrix,B:np.matrix,R:np.matrix):
    """
    Prediction part of the kalman filter
    Params:
    ----------
    mu, sigma: np.matrix, the mean and variance of the state variables
    u: control input
    A,B: np.matrix, The transformation matrix in the dynamic model of state variables x=Ax+Bu+epsilon
    R: np.matrix, The covariance matrix for the gaussian noise in the processing.

    Returns:
    ----------
    mu_, sigma_: the estimated mu and sigma
    """
    mu_=A*mu+B*u
    sigma_=A*sigma*A.T+R
    return mu_,sigma_


def update(mu_:np.matrix,sigma_:np.matrix,z:np.matrix,C:np.matrix,Q:np.matrix):
    """
    Correction part of the kalman filter
    
    Params:
    -----------
    mu_, sigma_: estimated mean and variance of the state variable.
    z: np.matrix, measurement
    C: np.matrix, measurement matrix (z=Cx+delta)
    Q: np.matrix, covariance matrix of the gaussian noise in the measurement.

    Returns:
    -----------
    mu, sigma: np.matrix, corrected estimated mean and variance of the state variable.
    """

    K=sigma_*C.T*np.linalg.inv(C*sigma_*C.T+ Q )
    mu=mu_+K*(z-C*mu_)
    sigma=(np.matrix(np.identity(sigma_.shape[0]))-K*C)*sigma_
    return mu, sigma

def kalmanfilter(mu:np.matrix,sigma:np.matrix,u,z:np.matrix,A:np.matrix,B:np.matrix,C:np.matrix,R:np.matrix,Q:np.matrix):
    """
    Kalman filter

    Params:
    ------------
    mu, sigma: np.matrix, the mean and variance of the state variables
    u: control input
    z: np.matrix, measurement
    A,B: np.matrix, The transformation matrix in the dynamic model of state variables x=Ax+Bu+epsilon
    C: np.matrix, measurement matrix (z=Cx+delta)
    R: np.matrix, The covariance matrix for the gaussian noise in the processing.
    Q: np.matrix, covariance matrix of the gaussian noise in the measurement.


    Returns:
    --------
    mu, sigma: np.matrix, corrected estimated mean and variance of the state variable.
    """
    mu_,sigma_=prediction(mu,sigma,u,A,B,R)
    return update(mu_,sigma_,z,C,Q)

