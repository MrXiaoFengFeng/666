# 算法：是高效解决问题的办法
# 算法之二分法

# 需求：有一个按照从小到大顺序排列的数字列表
# 需要从该数字列表中找到我们想要的数字
# 如何做更高效？


# nums = [-3,4,7,10,13,21,43,77,89]
# find_num = 10

# 传统方式1：整体遍历效率太低

# for num in nums:
#     if num == find_num:
#         print('find it')
#         break

# 方式2：二分法
# 思路：
# def binary_search(find_num ,列表):
#     mid_val = k
#     if find_num > mid_val:
#         #接下来查找应该是在列表的右半部分
#         列表=列表切片右半部分
#
#         binary_search(find_num,列表)
#     elif find_num < mid_val:
#         #接下来查找应该是在列表的右半部分
#         列表=列表切片左半部分
#         binary_search(find_num, 列表)
#     else:
#         print('find your num%s'%find_num)
#
# binary_search(40,l)


nums = [-3, 4, 7, 10, 13, 21, 43, 77, 89]
find_num = 10


def binary_search(find_num, l):
    print(l)
    if len(l) == 0:  # 切片查找到值不在列表中。len长度为0，结束函数
        print('你找的值不在列表中')
        return

    mid_index = len(l) // 2  # 列表长度整除得到索引

    if find_num > l[mid_index]:  # l[mid_index]即取到索引值
        # 接下来查找应该是在列表的右半部分
        # 列表=列表切片右半部分
        l = l[mid_index + 1:]  # 从中间值的后一位开始切片到列表末尾
        # 如果要返回值，就加return
        return binary_search(find_num, l)  # 循环查找。再切片列表中再取中

    elif find_num < l[mid_index]:
        # 接下来查找应该是在列表的右半部分
        # 列表=列表切片左半部分
        l = l[:mid_index]  # 顾头不顾尾，从列表第一个取值到中间值前一个
        return  binary_search(find_num, l)
    else:
        print('find your num%s' % find_num)
        return True

res = binary_search(find_num, nums)
print(res)
