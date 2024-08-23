class Solution(object):
    def gcd(self,a,b): 
        if (b == 0):
            return a
        return self.gcd(b, a%b)
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        num_dinom_list = []
        i=0
        while i<len(expression):
            sign = 1
            if expression[i]=='-':
                sign=-1
                i+=1
            elif expression[i]=='+':
                i+=1
            #calculating the numerator
            num = 0
            while i<len(expression) and expression[i].isdigit():
                num = num*10+ int(expression[i])
                i+=1
            #skipping the div sign
            i+=1
            # calculating the denominator 
            den = 0
            while i<len(expression) and expression[i].isdigit():
                den = den*10 + int(expression[i])
                i+=1
            num_dinom_list.append((sign*num, den))
        # print(num_dinom_list)
        
        hcf = num_dinom_list[0][1]
        lcm = num_dinom_list[0][1]
        for i in range(1,len(num_dinom_list)):
            hcf = self.gcd(hcf,num_dinom_list[i][1])
            lcm = lcm*num_dinom_list[i][1]//hcf
        # print(hcf,lcm)
        init_num = 0
        for num,den in num_dinom_list:
            init_num+=(num*lcm//den)
        # print(init_num)
        divi = self.gcd(init_num,lcm)
        # print(divi)
        init_num//=divi
        lcm//=divi
        return str(init_num)+'/'+str(lcm)
