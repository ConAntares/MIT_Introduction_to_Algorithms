#### Elementary Vector

using LinearAlgebra

re = range(1; stop = 10)
println(re)
    # 1:10
re = range(1.0; stop = 10)
println(re)
    # 1.0:1.0:10.0

re = range(1; stop = 10, step = 2)
println(re)
    # 1:2:9

re = range(1; stop = 10, length = 5)
println(re)
    # 1.0:2.25:10.0

A = [0,1,2,3,4,5,6,7,8,9]

println(A)          # [1, 2, 3, 4, 5]
println(A[1])       # 0
println(A[1:5])     # [0, 1, 2, 3, 4]
println(A[5:1])     # int64()
println(typeof(A))  # Array{Int64,1}
println(eltype(A))  # Int64
println(length(A))  # 10
println(ndims(A))   # 1
println(size(A))    # (10,)
println(size(A,1))  # 10
println(size(A,2))  # 1
println(size(A,3))  # 1

re = float(A)
println(re)         # [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

re = float([0,1,2,3])
println(re)         # [0.0, 1.0, 2.0, 3.0]

re = range(1, stop = 10, step = 2)
println(re)         # 1:2:9

re = range(1, stop = 11, length = 51)
println(re)         # 1.0:0.2:11.0

re = zeros(10)
println(re)         # [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

re = ones(10)
println(re)         # [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

re = rand(4)
println(re)         # [0.0478584, 0.144831, 0.836978, 0.251658]

re = randn(4)
println(re)         # [-0.62092, 0.552435, -0.0910689, -1.03891]

A = [1,2,3,4]
B = [0,2,4,6]

re = A .+ 2
println(re)         # [3, 4, 5, 6]

re = A * 2
println(re)         # [2, 4, 6, 8]

re = A .* 2
println(re)         # [2, 4, 6, 8]

re = A .^ 2
println(re)         # [1, 4, 9, 16]

re = A + B
println(re)         # [1, 4, 7, 10]

re = A .* B
println(re)         # [0, 4, 12, 24]

re = A' * B
println(re)         # 40

re = A * B'
println(re)         
    # [0 2  4  6; 
    #  0 4  8 12; 
    #  0 6 12 18; 
    #  0 8 16 24]

re = dot(A',B)
println(re)         # 40

re = dot(A,B')
println(re)         # 40

U = [1,2,3]
V = [0,2,4]

re = cross(U,V)
println(re)         
    # [2, -4, 2]
