import numpy as np

def least_squares(_input, target):
    _input = np.array(_input)
    row_dim = _input.shape[0]
    col_dim = _input.shape[1]
    table = qr_reduction(_input)  # if the matrix has significantly more rows, use parallel QR reduction instead
    _input, orthogonal, matrix = table[0], table[1], table[2]
    rhs = np.matmul(np.transpose(orthogonal), target)  # right-hand side Q^t * b
    sol_criterion = np.prod(rhs[col_dim:])  # exact solution iff Q^t * b only has non-zero components in the first 'col_dim' rows
    if sol_criterion == 0:
        solution = np.matmul(np.linalg.inv(matrix), rhs[:col_dim])
        return f"The system has an exact solution {solution}"
    else:
        rhs[col_dim:row_dim] = np.zeros(row_dim - col_dim)
        solution = np.round(np.matmul(np.linalg.inv(matrix), rhs[:col_dim]), 3)
        norm = np.round(np.linalg.norm(target - np.matmul(_input, solution)), 4)  # residual norm
        return f"{solution} minimizes the residual norm, which is: {norm}"
