class ChangeCoin:
    def __init__(self,sum,coins=[]):
        self.sum=sum
        #sort a list in descending order
        self.coins=coins.sort(reverse=True)
        self.result=[]
    def naive_version(self):
        i=0
        s=self.sum
        while i<len(self.coins):
            if self.coins[i]<=s:
                self.result.append(self.coins[i])
                s-=self.coins[i]
            else:
                i+=1
    def get_coins(self):
        n=int(input('Enter nomber of coins : '))
        self.coins=list()
        for i in range(n):
            self.coins.append(int(input('Enter the coin number %d value'%(i+1))))
        self.coins.sort(reverse=True)    

#testing
#create the instance
s=int(input('Enter a positive integer value : '))
cc=ChangeCoin(s)
cc.get_coins()
cc.naive_version()
print(f"the minimum change coins for {cc.sum} = {cc.result}")

                


    
