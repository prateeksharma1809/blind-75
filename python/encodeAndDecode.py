from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for str1 in strs:
            for i in str1:
                result += chr(ord(i) + ord('a'))
            result += '@@@@'
        # print(result[:-4])
        return result

    def decode(self, s: str) -> List[str]:
        result=[]
        temp = s.split('@@@@')
        for ind in temp:
            str1=''
            for i in ind:
                str1+=chr(ord(i)-ord('a'))
            result.append(str1)
        # print(result[:-1])
        return result[:-1]