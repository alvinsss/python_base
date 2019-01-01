#author:alvin
#coding:utf8
import  re
r1 = r"csvt.net"
rs=re.findall(r1,'csvt.net')
rs1=re.findall(r1,'csvtxnet')
rs2=re.findall(r1,'csvt\nnet')
rs3=re.findall(r1,'csvt\nnet',re.S)

print(rs,"---",rs1,"---",rs2,"---",rs3)

s= """hello csvt 
    csvt hello
    hello csvt hello
    csvt hehe"""
print(s)
r = r"^csvt"
print(re.findall(r,s))
print(re.findall(r,s,re.X))

tel = r"""
    \d{3,4}
    -?
    \d{8}
    """
rs = re.findall(tel,'010-12345678')
rs1 = re.findall(tel,'010-12345678',re.X)
print(tel,rs,rs1)

email = r"\w{3}@\w+(\.com|\.cn)"
print(re.match(email,'aaa@csvt.com'))
print(re.match(email,'aaa@csvt.org'))
print(re.findall(email,'aaa@csvt.com')) #findall优先返回分组的数据

s = r"dadas  hello src=csvt yes jjjd  src=123 yes fdkfkdk hello src=python yes fdlf"
rs1= r"hello src=.+ yes"
rs2= r"hello src=(.+) yes"
res1 = re.findall(rs1,s)
res2 = re.findall(rs2,s)
print(res1,"\n",str(res2))