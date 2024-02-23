# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
# priority queue 
class priorityQueue:    
    def __init__(self):
        self.q=[]
    
    def switch(self,a,b):
        temp = self.q[a]
        self.q[a]=self.q[b]
        self.q[b]=temp
        
    def add(self,item):

        self.q.append(item)
        p=len(self.q)-1
        while p>0:
            parent=int((p-1)/2)
            if self.q[p]['p']<self.q[parent]['p']:
                self.switch(p,parent)
                p=parent
            else:
                break
        print(f'after add : {item['p']}, {item['v']}')
        self.print()
        return len(self.q)
    
    def pop(self):
        if len(self.q)==0 :
            return None
        self.switch(0,-1)
        item = self.q.pop()
        size_q = len(self.q)
        idx=0

        # min(cursor, left, right) node make parent node
        while idx*2+1<size_q:
            left=idx*2+1
            right=idx*2+2

            ip=self.q[idx]['p']
            lp=self.q[left]['p']
            
            cursor=idx
            if right>=size_q:
                if ip>lp :
                    self.switch(idx,left)
                    idx=left
            else:
                rp=self.q[right]['p']
                if ip>lp and lp<=rp:
                    self.switch(idx,left)
                    idx=left
                elif ip>rp and lp>rp:
                    self.switch(idx,right)
                    idx=right

            if idx==cursor:
                break
        print(f'after pop:  {item['p']}, {item['v']}')
        self.print()
        return item
    def print(self):
        print(list(map(lambda d: f"{d['p']} {d['v']}",self.q)))

def frequencies(s):
    dict={}
    for i,n in enumerate(s):
        if n in dict:
            dict[n]+=1
        else:
            dict[n]=1
    result = list(dict.items())
    return result

def createTable(freqs):
    pq=priorityQueue()
    for d in list(map(lambda temp : {'p':temp[1],'v':temp[0], 'len':1},freqs)):
        pq.add(d)
        
    while len(pq.q)>1:
        a = pq.pop()
        b = pq.pop()
        print(f'a:{a}\nb:{b}\n')
        c = {'p':a['p']+b['p'],'left':a,'right':b, 'len':a['len']+b['len'], 'v':a['v']+b['v']}
        pq.add(c)
    result = pq.pop()
    table={}
    def search(cursor,path):
        if len(cursor['v'])==1:
            table[cursor['v']]=path
            return 
        search(cursor['left'],path+'0')
        search(cursor['right'],path+'1')
    if result:
        search(result,'')
    return table
# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):

    if len(freqs)<2:
        return None
    print(f'encode : {s}, {list(filter(lambda cf: cf[0] in s,freqs))}')
    print(f'encode : {freqs}')
    table = createTable(freqs)
    result=''
    for c in s:
        if c not in table:
            return None
        result+=table[c]
#     print(table)
    print(f'encode result : {result}')
    return result 
  
# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs,bits):
    print(f'decode: {bits}')

    if len(freqs)<2:
        return None
#     print(f'decode {freqs},{bits}')
    cTable = createTable(freqs)
    l = ''
    result=''
    table = {v:k for k,v in cTable.items()}
    for c in bits:
        l+=c
        if l in table:
            result+=table[l]
            l=''
    return result