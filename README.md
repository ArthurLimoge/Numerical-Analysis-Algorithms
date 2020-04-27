This repository contains various algorithms I have had the opportunity to code. Most of them were done for the course *Introduction to Numerical Analysis* by [Peter Schmid](https://www.imperial.ac.uk/people/peter.schmid) :

:large_orange_diamond: **Householder_QR_Reduction.py**: produces a QR factorization of an arbitrary matrix, using Householder transformations.

:large_orange_diamond: **Parallel_QR_Reduction.py**: algorithm which consists in subdivising big matrices into smaller blocks, to optimize QR decomposition; as described in [this paper](https://web.stanford.edu/group/ctr/Summer/SP14/08_Transition_and_turbulence/08_sayadi.pdf). The algorithm is summarized in the sketch page 2. It uses the regular QR-reduction algorithm from Householder_QR_Reduction.

*Note:* Parallel QR reduction only works for (m×n) matrices such that m ≥ n. If m < n, use regular QR reduction.

:large_orange_diamond: **Least_Squares.py**: algorithm which solves the least squares problem (ie: minimizes the norm of the residual in an overconditioned system) by using QR reduction. 
*By default, the solver uses the regular QR reduction algorithm. If necessary, can replace it by parallel QR reduction, in a case where the number of rows is far superior than that of columns, for instance.*
