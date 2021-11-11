class Snake {  
  PVector pos;
  boolean hasMoved;
  ArrayList<PVector> bp;  
  int segSize;  
  void constructor(PVector headPos, ArrayList bodyParts, int segSize) {    
    this.pos = headPos;    
    this.bp = bodyParts;    
    this.segSize = segSize;
    this.hasMoved = false;
  }  
  boolean checkIfBoutaDie() {    
    if (this.pos.x == width - (segSize) && moves.get(0).charAt(0) == 'd') {      
      return true;
    } else if (this.pos.x < segSize && moves.get(0).charAt(0) == 'a') {      
      return true;
    } else if (this.pos.y > height - (segSize * 2) && moves.get(0).charAt(0) == 's') {      
      return true;
    } else if (this.pos.y < segSize && moves.get(0).charAt(0) == 'w') {      
      return true;
    }    
    for (int i = 0; i < this.bp.size(); i++) {      
      if (this.pos.x == this.bp.get(i).x - segSize && this.pos.y == this.bp.get(i).y && moves.get(0).charAt(0) == 'd') {        
        return true;
      } else if (this.pos.x == this.bp.get(i).x && this.pos.y == this.bp.get(i).y - segSize && moves.get(0).charAt(0) == 's') {        
        return true;
      } else if (this.pos.x == this.bp.get(i).x + segSize && this.pos.y == this.bp.get(i).y && moves.get(0).charAt(0) == 'a') {        
        return true;
      } else if (this.pos.x == this.bp.get(i).x && this.pos.y == this.bp.get(i).y + segSize && moves.get(0).charAt(0) == 'w') {        
        return true;
      }
    }    
    return false;
  }  
  ArrayList<String> newUpdate(ArrayList<String> moves, int numFrame) {    
    while (moves.size() < 1) {      
      moves.add(" ");
    }    
    if (moves.size() > 1) {      
      moves.remove(0);
    }    
    String currMove = moves.get(0);    
    boolean OHCRAPIMBOUTADIE;    
    if (framesOfBoutaDie < fps) {      
      OHCRAPIMBOUTADIE = checkIfBoutaDie();
    } else {      
      OHCRAPIMBOUTADIE = false;
    }    
    if (OHCRAPIMBOUTADIE) {      
      framesOfBoutaDie += numFrame;
    } else {      
      framesOfBoutaDie = 0;
    }
    if (!OHCRAPIMBOUTADIE) {      
      switch(currMove) {      
      case "w":        
        this.moveBody();        
        this.pos.y -= this.segSize;        
        break;      
      case "a":        
        this.moveBody();        
        this.pos.x -= this.segSize;        
        break;      
      case "s":        
        this.moveBody();        
        this.pos.y += this.segSize;        
        break;      
      case "d":        
        this.moveBody();        
        this.pos.x += this.segSize;        
        break;
      }
    }    
    return moves;
  }  
  boolean checkDead() {    
    if (this.pos.x > width - segSize || this.pos.x < 0 || this.pos.y > height - segSize || this.pos.y < 0) {      
      return true;
    }    
    for (int i = 0; i < this.bp.size(); i++) {      
      if (this.pos.x == this.bp.get(i).x && this.pos.y == this.bp.get(i).y) {        
        return true;
      }
    }    
    return false;
  }
  void moveBody() {
    if (!this.hasMoved) {this.hasMoved = true;}
    for (int i = this.bp.size() - 1; i > 0; i--) {      
      this.bp.get(i).x = this.bp.get(i-1).x;      
      this.bp.get(i).y = this.bp.get(i-1).y;
    }    
    this.bp.get(0).y = this.pos.y;    
    this.bp.get(0).x = this.pos.x;
  }  
  boolean ateApple(Apple apple) {    
    return (this.pos.x == apple.pos.x && this.pos.y == apple.pos.y);
  }  
  void grow() {    
    this.bp.add(new PVector(700, 700));
  }  
  void display() {    
    fill(0, 230, 0);    
    stroke(0);    
    for (int i = 0; i < this.bp.size(); i++) {      
      square(this.bp.get(i).x, this.bp.get(i).y, this.segSize);
    }   
    fill(0, 230, 0);    
    square(this.pos.x, this.pos.y, this.segSize);
  }
}
