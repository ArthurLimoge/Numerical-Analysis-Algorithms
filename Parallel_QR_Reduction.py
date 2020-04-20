import numpy as np

def parallel_qr_reduction(_input):
    size = _input.shape[0]
    extra_block_size = size % 100
    number_blocks = int((size - extra_block_size)/10)  # divide the matrix into blocks of 10 + the last block
    blocks = []
    if extra_block_size >= _input.shape[1] or extra_block_size == 0:
        for i in range(number_blocks):
            blocks.append(_input[10*i:10*(i+1)])
        if extra_block_size != 0:
            number_blocks += 1
            blocks.append(_input[size - extra_block_size:size])
    else:
        for i in range(number_blocks-1):
            blocks.append(_input[10*i:10*(i+1)])
        blocks.append(_input[10*(number_blocks-1):size])
    col_dim = _input.shape[1]  # dimensions the R' matrix will have
    row_dim = col_dim*number_blocks
    big_r_matrix = np.zeros((row_dim, col_dim))
    orthogonal_blocks = []
    for i in range(number_blocks):  # first step of the sketch
        submatrix = np.array(blocks[i])
        factorization = qr_reduction(submatrix)
        orthogonal_blocks.append(np.ndarray.tolist(factorization[1]))
        sub_r = factorization[2]
        big_r_matrix[col_dim*i:col_dim*(i+1), :col_dim] = sub_r
    factorization = qr_reduction(big_r_matrix)
    q_matrix_2 = factorization[1]
    orthogonal_matrix = np.zeros((1, col_dim))  # pre-allocate
    for i in range(number_blocks):
        orthogonal_block_1 = np.array(orthogonal_blocks[i])
        orthogonal_block_2 = q_matrix_2[2*i:2*(i+1), :2]
        new_block = np.matmul(orthogonal_block_1, orthogonal_block_2)
        orthogonal_matrix = np.vstack((orthogonal_matrix, new_block))
    orthogonal_matrix = orthogonal_matrix[1:, :]
    return orthogonal_matrix  
