#author:alvin
#coding:utf8
import  os
g = os.walk("E:\\codebase\\python\\zg\\testdir")
for path,d,fileList in  g:
    os.path.join(path,fileList)
    print(os.path.join(path,fileList))



# def dirList(path):
#     filelist = os.listdir(path)
#     fpath = os.getcwd()
#     print(fpath)
#     allfilelist = []
#     for filename in filelist:
#         # if os.name == 'nt':n#Windows 操作系统
#         #     allfilelist.append(fpath+filename)
#         # else:
#         #     allfilelist.append(fpath+'/'+filename)
#         filepath = os.path.join(fpath,filename)
#         print(os.path.isdir(filepath))
#         if os.path.isdir(filepath):
#             dirList(filepath)
#         print(filepath)
#         allfilelist.append(filepath)
#
#     return allfilelist
# allfile = dirList("E:\\codebase\\python\\zg\\testdir")