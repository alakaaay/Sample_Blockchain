import datetime
import hashlib

class block:
    blockNum = 0
    count = 0
    hash = None
    data = None
    next = None
    prevHash = 0x0
    time = datetime.datetime.now()

    def hash(self):
        hex = hashlib.sha256()
        hex.update(
            str(self.blockNum).encode('utf-8')+
            str(self.count).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.prevHash).encode('utf-8') +
            str(self.time).encode('utf-8')
        )
        return hex.hexdigest()

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "Block Number: " + str(self.blockNum) + "\nData: " +str(self.data)+"\nHash: " +str(self.hash())+"\nNumber of Hashes: "+ str(self.count) +"\n======================================================================\n"


class BlockChain:
    difficulty = 10
    countMax = 2**32
    range = 2**(256-difficulty)

    block = block("Genesis")
    genesis = head = block

    def addBlock(self, block):
        block.prevHash = self.block.hash()
        block.blockNum = self.block.blockNum + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.countMax):
            if int(block.hash(), 16) <= self.range:
                self.addBlock(block)
                break
            else:
                block.count = block.count+1

case=9
data=None
numBlocks=0
blockchain = BlockChain()
totalNum=0



while case!=0:
    print("Please type 1, 2, 3 or 0 to choose one of the options")
    print("1)Add a block to Blockchain\n2)Add number of blocks to the Blockchain")
    print("3)Get data from txt file")
    print("4)Show mined blocks\n5)Show mined blocks in txt file\n0)Exit")
    case = int(input())
    if case==1:
        print("Please write a data that you want to store in Blockchain: ")
        data=str(input())
        blockchain.mine(block(data))
        totalNum+=1
        print("=============================================================")

    elif case==2:
        print("Please write number of blocks you want to add: ")
        numBlocks=int(input())
        counter=0
        for n in range(numBlocks):
            print("Please write a data that you want to store in Block "+str(counter)+": ")
            data = str(input())
            blockchain.mine(block(data))
            counter+=1
            totalNum += 1
            print("=============================================================")

    elif case ==3:
        inputFile=open("input.txt")
        while True:
            line = inputFile.readline()
            if not line:
                break
            blockchain.mine(block(line))
            totalNum += 1

        inputFile.close()


    elif case==4:
        for n in range(totalNum+1):
            print(blockchain.head)
            blockchain.head=blockchain.head.next
        case = 0

    elif case==5:
        file = open("blockchain.txt", "w")
        for n in range(totalNum+1):
            file.write(str(blockchain.head))
            blockchain.head = blockchain.head.next
        file.close()
        print("Please check the file blockchain.txt!")
        case = 0


    elif case==0:
        case =0
    else:
        print("Your input is wrong!")




