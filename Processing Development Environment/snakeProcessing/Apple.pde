class Apple {  
  PVector pos;  
  int size;
  int worth;
  void constructor(PVector pos, int size, int worth) {    
    this.pos = pos;    
    this.size = size;
    this.worth = worth;
  }  
  void newPos() {    
    this.pos.x = (round(random((width / this.size) - 2)) + 1) * this.size;    
    this.pos.y = (round(random((height / this.size) - 2)) + 1) * this.size;
  }  
  void display() {    
    noStroke();    
    fill(255, 0, 0);    
    square(this.pos.x, this.pos.y, this.size);
  }
}
