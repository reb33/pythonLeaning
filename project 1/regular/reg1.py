import re

str1 = "noininhieritiance"
# print(len(re.match("(.*?)i", str1).group()))
# for x in enumerate(str1):
#     if x[1] == "i":
#         ret.append(x[0])
ret = [x[0] for x in enumerate(str1)
       if x[1] == "i"]
print(ret)
