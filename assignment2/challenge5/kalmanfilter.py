import numpy as np

def prediction(mu,sigma,u,A,B,R):
    mu_=A*mu+B*u
    sigma_=A*sigma*A.T+R
    return mu_,sigma_


def update(mu_,sigma_,z,C,Q):
    K=sigma_*C.T*np.linalg.inv(C*sigma_*C.T+ Q )
    mu=mu_+K*(z-C*mu_)
    sigma=(np.matrix(np.identity(sigma_.shape[0]))-K*C)*sigma_
    return mu, sigma

def kalmanfilter(mu,sigma,u,z,A,B,C,R,Q):
    mu_,sigma_=prediction(mu,sigma,u,A,B,R)
    return update(mu_,sigma_,z,C,Q)

