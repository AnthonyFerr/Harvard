def convert(integers):
    nums = set(integers)
    dic = dict.fromkeys(nums)
    for i in dic:
        dic[i] = integers.count(i)
    print(dic)
convert([1, 1, 4, 6, 3, 3, 3, 9, 10, 1, 2, 7, 2])
