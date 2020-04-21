This repository contains various algorithms I have had the opportunity to code (in Python). Most of them were done for the course *Introduction to Numerical Analysis* by [Peter Schmid](https://www.imperial.ac.uk/people/peter.schmid) :

• **Householder_QR_Reduction.py**: produces a QR factorization of an arbitrary rectangular (m > n) matrix, using Householder transformations.

• **Parallel_QR_Reduction.py**: algorithm which consists in subdivising big matrices into smaller blocks, to optimize QR decomposition; as described in [this paper](https://web.stanford.edu/group/ctr/Summer/SP14/08_Transition_and_turbulence/08_sayadi.pdf). The algorithm is based on the sketch page 2. It uses the regular QR-reduction algorithm from Householder_QR_Reduction.

• **Least_Squares.py**: algorithm which solves the least squares problem (ie: minimizes the norm of the residual in an overconditioned system) by using QR reduction. 
*By default, the solver uses the regular QR reduction algorithm. If necessary, can replace it by parallel QR reduction, in a case where the number of rows is far superior than that of columns, for instance.*
