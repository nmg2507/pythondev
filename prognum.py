#再帰的な関数でのフィボナッチ数列 

def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)
