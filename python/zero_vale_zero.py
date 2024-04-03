if __name__ == '__main__':
    
    def remove_zeros(num):
        return int(str(num).replace('0', ''))

    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break
        result = remove_zeros(m + n)
        print(result)