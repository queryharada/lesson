N = 10
Sum = 0
K = 0

while (K < N):
    K = K + 1
    Sum = Sum + K
    print('loop invariant:N({0}) < K({1}) = {2}'.format(K, N, K < N))

print('Sum = ', Sum)
