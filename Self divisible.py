m = int(input("Enter the lower range: "))
n = int(input("Enter the upper range: "))
n +=  1

nums = []

for x in range (m,n):
    
    def NumberOfDigits(self):
        c = 0
        while(self > 1):
            self = self / 10
            c += 1
        return c
             
        
    def Check(x):
        
        lst = []
        n = int(NumberOfDigits(x))
        m = n - 1
        t1 = x
        
        while(n >= 1):
            t2 = int(t1/(10**(n-1)))
            lst.append(t2)
            n = n - 1
       
        while(m > 0):
            lst[m] = lst[m] - lst[m-1]*(10)
            m -= 1
            
        flag = 0
        
        for i in lst:
            if(i == 0):
                flag += 1
                break
            else:
                continue
            
        if(flag == 1):
            return False
        else:
            return lst
        
    def execute():
        
        if(Check(x) != False):
            f = 0
            for i in list:
                if(x % i != 0):
                    f += 1
                    break
                else:
                    continue
                        
            if(f == 0):
                nums.append(x)
                        
            else:
                pass
                
        else:
            pass
        
                            
    list = Check(x)
    execute()
    
print("Self dividing numbers in the given range are: ", nums)
    
