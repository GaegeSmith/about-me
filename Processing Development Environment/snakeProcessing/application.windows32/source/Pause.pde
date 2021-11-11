class Pause {    
  PVector pos;  
  PVector size;  
  String options = "";  
  String keyBinds = "";    
  void constructor(PVector pos, PVector size, ArrayList<String> opts, ArrayList<String> controls) {    
    this.pos = pos;    
    this.size = size;    
    for (int i = 0; i < opts.size(); i++) {      
      this.options = this.options + opts.get(i) + "\n";
    }        
    for (int i = 0; i < controls.size(); i++) {      
      this.keyBinds = this.keyBinds + controls.get(i) + "\n";
    }
  }       
  void show() {    
    textAlign(CENTER, CENTER);    
    text(this.options + "\n" + noSave, width / 2, height / 2);
  }    
  void showKeys() {    
    textAlign(CENTER, CENTER);    
    text(this.keyBinds, width / 2, height / 2);
  }
}
