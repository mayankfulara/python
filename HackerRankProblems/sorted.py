''' SORTED IS A FUNCTION WHICH STORES A GIVEN NUMBERS IN A SPECIFIC ORDRER EITHER ASCENDING OR DESCENDING AND RETURNS THEM AS LIST
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])