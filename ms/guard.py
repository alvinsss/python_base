
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 14:20
# @Author  : alvin
# @File    : guard.py
# @Software: PyCharm

# -*- coding:utf-8 -*-

# palindrome str : 回文字符串：一个字符串，不论是从左往右，还是从右往左，字符的顺序都是一样的（如abba，等）


def is_palindrome_1(tmp_str):
    for i in range( len( tmp_str ) ):
        if tmp_str[i] != tmp_str[-(i + 1)]:
            return False
    return True


def is_palindrome_2(tmp_str):
    tmp_str_reverse = tmp_str[::-1]
    if tmp_str == tmp_str_reverse:
        # return True
        print("is_palindrome_2---->",tmp_str)
    else:
        # return False
        pass
    # return tmp_str == tmp_str[::-1]


# 递归
def is_palindrome_3(tmp_str):
    if len( tmp_str ) <= 1:
        # return True
        pass
    else:
        if tmp_str[0] == tmp_str[-1]:
            print("is_palindrome_3",is_palindrome_3( tmp_str[1:-1] ))
            return is_palindrome_3( tmp_str[1:-1] )
        else:
            # return False
            pass



if __name__ == "__main__":
    test_str1 = "abcba"
    test_str2 = "123456a"
    raw_str = "cbcabadc12122231111"
    # print (is_palindrome_1( test_str1 ))
    # print (is_palindrome_2( test_str1 ))
    # print (is_palindrome_3( test_str1 ))
    #
    # print (is_palindrome_1( test_str2 ))
    # print (is_palindrome_2( test_str2 ))
    # print (is_palindrome_3( test_str2 ))

    # for i in range(len(raw_str)):
    #     if i == 0 or i == 1:
    #         continue
    #     new_str = raw_str[0:i]
    #     print(new_str)
    #     # print( is_palindrome_2( new_str ) )

    for i in range(len(raw_str)):
        new_str = raw_str[i:]
        print("new_str---->",new_str)
        for j in range(len(new_str)):
            if j == 0 or j == 1:
                continue
            new2_str = new_str[:j]
            print(new2_str)
            print( is_palindrome_2( new2_str ) )
