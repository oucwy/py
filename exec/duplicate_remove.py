def remove_duplicates(s):
    return ''.join(set(s))
 
# 示例使用
original_string = "aabbcddd"
print(set(original_string))
unique_string = remove_duplicates(original_string)
print(unique_string)  # 输出: abcd
print('output: ',''.join({'a', 'c', 'd', 'b'}))
print('output: ', ''.join(set(str(10086))))