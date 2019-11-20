# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 13:19
# @Author  : alvin
# @File    : Palindrome_str.py
# @Software: PyCharm

class Par_str(object):


    def get_palindrome_str(self,str1,n):
        '''
        记串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba"
        :param str1:
        :param n:
        :return:
        '''
        print("len(str1)",len(str1))
        if len(str1) - n == 0:
            print("求当前长度%d"%(n))
            print("str1---->",str1)
            print("str1_palind---->",str1[::-1])
            if str1 == str1[::-1]:
                print("YES")
                print(str1)
            else:
                print("NO")
        else:
            save_list_zx = []
            save_list_nx = []
            print("求当前长度%d"%(n))
            counts = len(str1)-n
            # print("counts",counts)
            for x in range(counts):
                b = str1[x:x+n]
                print("正序b",b)
                c = b [::-1]
                print( "逆序c", c )
                save_list_zx.append(b)
                save_list_nx.append(c)
                # if b == c:
                #     print('YES')
                #     print( "b == c --->b", b )
                #
                #     print( "b == c --->c", c )
                #     break
                # else:
                #     print("NO")
                for i in save_list_zx:
                    for j in save_list_nx:
                        if i == "aba":
                            print("aba",i)
                        print("i-j",i,j)
                        if i == j:
                            print("回文串值是",i)

        print( "求当前长度%d结束！" % (n) )

if __name__ == "__main__":
    raw_str = "cbcabadc12122231111"
    n = Par_str()
    lens = len(raw_str)
    for i in range (lens+1):
        if i == 0:
            continue
        # print("i",i)
        n.get_palindrome_str( raw_str, i )
