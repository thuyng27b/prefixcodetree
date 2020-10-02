
class Node:
    stt=0;
    def __init__(self, val,stt):
        self.l = None
        self.r = None
        self.v = val
        self.stt=stt
class PrefixCodeTree:
    ''
    root =Node('@s',1)
    def __init__(self):
        pass
    def insert(self,codeword,symbol):
        node=self.root
       # print("nút bắt đầu                  "+str(node.stt))
        for i in range(0,len(codeword)):
            if i==len(codeword)-1:
                if codeword[i]==0:
                    node.l=Node(symbol,node.stt*2)
                   # print(str(node.stt)+" 0e")
                else:
                    node.r=Node(symbol,node.stt*2+1)
                   # print(str(node.stt)+" 1e")

            else:
                if codeword[i]==0:
                    if node.l==None:
                        node.l=Node('@s',node.stt*2)
                   # print(str(node.stt)+" 0+")
                    node=node.l

                else:
                    if node.r==None:
                        node.r=Node('@s',node.stt*2+1)
                  #  print(str(node.stt)+" 1+")
                    node=node.r

        #print(symbol)
    def decode(self, encodedData,datalen):
        message=""
        node=self.root
        bits=bin(int(encodedData.hex(),base=16))[2:]
        for i in range(0,datalen):
               # print(str(bits[i])+ "    bit thứ "+str(i))
                if bits[i]==bin(0)[2:]:
                    node=node.l
                   # print(node.v+"                   0      "+str(node.stt))
                else:
                    node=node.r
                   # print(node.v+"                   1      "+str(node.stt))
                if node.l==None and node.r==None:
                   # print(node.v+"    sym      "+str(node.stt))
                    message=message+node.v
                    node=self.root
        return message
