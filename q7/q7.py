f = open(
    'C:\\Users\\Bob Dang\\Desktop\\Uni Winter 2021\\side project\\Advant of code\\q7\\input.txt', "r")
data = f.read()
data = data.split("\n")
total = 0
allFit = []


class Node():
    def __init__(self,
                 next=None,
                 prev=None,
                 fileName=None,
                 fileSize=None,
                 isDir=None,
                 NodeHead=None) -> None:
        self.NodeHead = NodeHead
        self.next, self.prev = next, prev
        self.fileSize = fileSize
        self.fileName = fileName
        self.isDir = isDir
        self.head = None

        self.contain = {}
        pass

    def addBack(self, node):
        curr = self.head
        while curr.next != None:
            curr = curr.next

        curr.next = node

    def printAll(self):
        print("dir ", self.fileName, self.fileSize)
        if self.fileSize < 100000:
            global total
            total += self.fileSize

        curr = self.head
        while curr != None:
            if curr.isDir == True:
                curr.printAll()
            else:
                print("WTd ", curr.fileName, curr.fileSize)

            curr = curr.next

    # def sumByte(self):

    def sumByte(self):

        allCurr = list(self.contain.keys())
        sumAll = 0
        for i in range(len(allCurr)):
            curr = self.contain[allCurr[i]]
            if curr.isDir:
                sumAll += curr.sumByte()
            else:
                sumAll += int(curr.fileSize)

        self.fileSize = sumAll
        return sumAll

    def fitSize(self, need):
        if self.fileSize >= need:
            global allFit
            allFit.append(self.fileSize)

        curr = self.head
        while curr != None:
            if curr.isDir == True:
                curr.fitSize(need)
            

            curr = curr.next


tOpLayer = Node(fileName="/", isDir=True)
# readline

curr = tOpLayer

for i in range(2, len(data), 1):
    if "$ cd" in data[i]:
        temp = data[i].split()
        if ".." in data[i]:
            curr = curr.NodeHead

        else:
            curr = curr.contain[temp[-1]]
            pass
    elif "$ ls" in data[i]:
        pass
    elif "dir" in data[i]:
        temp = data[i].split()

        fileName = temp[1]
        NodeContainer = Node(NodeHead=curr, fileName=fileName, isDir=True)
        if curr.head != None:
            curr.addBack(NodeContainer)
        else:
            curr.head = NodeContainer
        curr.contain[fileName] = NodeContainer
        # curr.head.printLv()
    else:
        temp = data[i].split()
        fileSize, fileName = temp[0], temp[1]

        NodeContainer = Node(NodeHead=curr, isDir=False,
                             fileName=fileName, fileSize=fileSize)

        if curr.head != None:
            curr.addBack(NodeContainer)

        else:
            curr.head = NodeContainer

        # curr.next = NodeContainer
        curr.contain[fileName] = NodeContainer
        # curr.head.printLv()
        # curr.fileSize += NodeContainer.fileSize

tOpLayer.sumByte()
# print(tOpLayer.printAll())
# print(total)
need = 70000000-tOpLayer.fileSize
need2=30000000-need
tOpLayer.fitSize(need2)
allFit.sort()
print(allFit[0])