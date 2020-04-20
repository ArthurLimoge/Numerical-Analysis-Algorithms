import numpy as np
from scipy.linalg import block_diag


def qr_reduction(_input):
    _input = np.array(_input).astype(float)
    matrix = np.array(_input).astype(float)  # this will be the R of the QR-decomposition
    row_dim = matrix.shape[0]
    col_dim = matrix.shape[1]
    orthogonal = np.eye(row_dim)
    for i in range(col_dim):
        column = matrix[i:row_dim, i]
        norm = np.linalg.norm(column)
        if norm == 0:
            break
        else:
            reflector = np.array(column)  # define the Householder reflector
            if reflector[0] == 0:
                sign = 1
            else:
                sign = abs(reflector[0]) / reflector[0]
            reflector[0] += sign*norm  # project onto the "x-axis", the farthest away from x, for computational reasons
            norm_squared = np.dot(reflector, reflector)
            projector = np.eye(row_dim - i) - 2*(np.outer(reflector, reflector))/norm_squared  # Householder projector
            matrix[i:row_dim, i:col_dim] = np.matmul(projector, matrix[i:row_dim, i:col_dim])
            full_projector = block_diag(np.eye(i), projector)
            orthogonal = np.matmul(orthogonal, np.transpose(full_projector))  # Q of the QR-decomposition

            _input = np.round(_input, 4)
            orthogonal = np.round(orthogonal, 4)
            matrix = np.round(matrix, 4)

            output = [_input, orthogonal[:row_dim, :col_dim], matrix[:col_dim, :col_dim]]  # note how we reduce q and r
    return output
