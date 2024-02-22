function HolidayPriorityQueue(){
  //Priority queue Constructor  
  this.tr=[]
}
HolidayPriorityQueue.prototype.switch= function(a,b){
  console.log(a,b)
  temp = this.tr[a];
  this.tr[a]=this.tr[b];
  this.tr[b]=temp;
}
HolidayPriorityQueue.prototype.addGift = function(gift){
  //Insert gift into priority queue and return new length
  this.tr.push(gift)
  p=this.tr.length
  while(p>1){
    
    if(this.tr[p-1].priority<this.tr[parseInt(p/2)-1].priority){
      this.switch(p-1,parseInt(p/2)-1)
      p=parseInt(p/2)
    }else{
      break;
    }
  }
  console.log(this.tr)
  return this.tr.length;
}

HolidayPriorityQueue.prototype.buyGift = function(){
  //Return gift with highest priority (lowest integer value)
  if(this.tr.length==0){
    return ''
  }
  gift = this.tr.shift()
  p=1
  while(p*2<=this.tr.length){
    if(this.tr[p-1].priority>this.tr[p*2-1].priority){
      this.switch(p-1,p*2-1)
      p*=2
    }else if(p*2<this.tr.length && this.tr[p-1].priority>this.tr[p*2].priority){
      this.switch(p-1,p*2)
      p*=2
    }else{
      break
    }
  }
  return gift.gift;
}