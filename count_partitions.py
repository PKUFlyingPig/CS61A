def count_partitions(n, m):
    if n < m:
        return count_partitions(n, n)
    if n <= 1:
        return 1
    if m == 1:
        return 1
    return count_partitions(n-m, m) + count_partitions(n, m-1)
    
