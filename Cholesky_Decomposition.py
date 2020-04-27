import numpy as np

def cholesky(_input):
    boole1 = is_pos_def(_input)
    boole2 = np.all(_input == np.transpose(_input))
    boole = boole1*boole2  # check that both hypotheses are satisfied
    if boole == 0:
        print("A needs to be symmetric and positive-definite.")
    else:
        R = np.ndarray.astype(np.array(_input), float)
        m = R.shape[0]
        for k in range(m):
            for j in range(k+1, m):
                coeff = R[k, j]/R[k, k]
                R[j, j:] = R[j, j:] - coeff*R[k, j:]
            R[k, k:] = R[k, k:]/np.sqrt(R[k, k])
            R[k+1:, k].fill(0)
            L = np.transpose(R)
    return L  # L is lower triangular and the input matrix is expressed as L*L^t
