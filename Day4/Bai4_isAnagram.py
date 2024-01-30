# Time complexity: O(nlogn) với n là độ dài của chuỗi dài hơn (nếu 2 chuỗi không cùng độ dài)
def isAnagram(str1, str2):
    if (len(str1) != len(str2)):
        return False
    # So sánh 2 chuỗi (cụm từ) đã được sắp xếp xem chúng có giống nhau hay không
    # Hàm sorted không làm thay đổi giá trị của 2 chuỗi, nó tạo 2 chuỗi riêng biệt và so sánh
    if sorted(str1) == sorted(str2):
        return True
    return False

# inp = input("Enter two strings, separated by spaces: ")

# s = inp.split()
# print(s)
# if len(s) == 2 and isAnagram(s[0], s[1]):
#     print('The strings are anagrams')
# else:
#     print("The strings aren't anagrams or input not correct")

s1, s2 = 'restful', 'fluster'
if isAnagram(s1, s2):
    print('The strings are anagrams')
else:
    print("The strings aren't anagrams")
