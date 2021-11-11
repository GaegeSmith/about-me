import processing.sound.SoundFile;
Pause pauseMenu = new Pause();
Snake snake = new Snake();
Apple apple = new Apple();
SaveGame loadSave = new SaveGame();
SoundFile oof;
SoundFile eat;
int w;
int h;
int segSize = 20;
int startLen = 4;
int fpaf = 10;
int fps = 60;
int numFrames = 0;
boolean pause = false;
boolean showKeys = false;
boolean playSound = true;
String noSave = "";
int framesOfBoutaDie = 0;
PFont font;
ArrayList<String> moves = new ArrayList<String>();
PVector startPos;
ArrayList<PVector> segments = new ArrayList<PVector>();
ArrayList<String> opts = new ArrayList<String>();
ArrayList<String> keys = new ArrayList<String>();
void setup() {  
  font = createFont("PressStart2P.ttf", 2);  
  textFont(font);  
  opts.add("Resume (P)");  
  opts.add("Controls (T)");  
  opts.add("Save Current Game (X)");  
  opts.add("Load Saved Game (L)");  
  opts.add("Exit (ESC)");  
  keys.add("UP (w)");  
  keys.add("LEFT (a)");  
  keys.add("DOWN (s)");  
  keys.add("RIGHT (d)");  
  keys.add("RESET (r)");  
  keys.add("BOOST (space)");  
  keys.add("TOGGLE SOUND (o)");
  keys.add("INCREASE APPLE WORTH (+, =)");
  keys.add("DECREASE APPLE WORTH (-, _)");
  
  moves.add(" ");  
  frameRate(fps);  
  size(600, 600);  
  w = width;  
  h = height;  
  loadSave.create();  
  pauseMenu.constructor(new PVector(width / 2 - 30, height / 2 - 20), new PVector(width / 2 + 30, height / 2 - 20), opts, keys);  
  println("hello");  
  startPos = new PVector(w/2, h/2);  
  apple.constructor(new PVector(0, 0), segSize, 1);  
  segments.add(new PVector(startPos.x - segSize, startPos.y));  
  for (int i = 1; i < startLen; i++) {      
    segments.add( new PVector( segments.get(i-1).x - segSize, startPos.y));
  }  
  oof = new SoundFile(this, "data/oof.mp3");  
  eat = new SoundFile(this, "data/grow.mp3");  
  snake.constructor(startPos, segments, segSize);  
  background(150);  
  apple.newPos();
}
boolean vertical() {  
  if (moves.size() > 1) {    
    return moves.get(1).charAt(0) != 'w' && moves.get(1).charAt(0) != 's';
  }  
  return moves.get(0).charAt(0) != 'w' && moves.get(0).charAt(0) != 's';
}
boolean horizontal() {  
  if (moves.size() > 1) {    
    return moves.get(1).charAt(0) != 'd' && moves.get(1).charAt(0) != 'a';
  }  
  return moves.get(0).charAt(0) != 'd' && moves.get(0).charAt(0) != 'a';
}
void keyPressed() {  
  if (key == 'w' && vertical()/*moves.get(0).charAt(0) != 's'*/) {    
    moves.add(str(key));
  }  
  if (key == 's' && vertical()/*moves.get(0).charAt(0) != 'w'*/) {    
    moves.add(str(key));
  }  
  if (key == 'a' && horizontal() && snake.hasMoved/*moves.get(0).charAt(0) != 'd'*/) {    
    moves.add(str(key));
  }  
  if (key == 'd' && horizontal()/*moves.get(0).charAt(0) != 'a'*/) {    
    moves.add(str(key));
  }  
  switch(key) {  
  case 'x':     
    if (pause) {      
      loadSave.saveGame(snake, apple);
    }    
    break;  
  case 'l':    
    if (pause) {      
      try {        
        loadSave.openGame();        
        noSave = "";
      } 
      catch (Exception e) {        
        noSave = "No saved game found";
      }
    }    
    break;  
  case 'p':    
    if (pause) {      
      pause = false;      
      showKeys = false;      
      noSave = "";
    } else {      
      pause = true;
    }    
    break;  
  case 't':    
    if (pause && !showKeys) {      
      showKeys = true;      
      noSave = "";
    } else {      
      showKeys = false;      
      noSave = "";
    }    
    break;  
  case 'o':    
    if (playSound) {      
      playSound = false;      
      noSave = "";
    } else {      
      playSound = true;      
      noSave = "";
    }    
    break;  
  case ' ':    
    fpaf = 2;    
    break;  
  case 'r':    
    reset();    
    break;
   case '=':
     if (apple.worth < 10) {
       apple.worth++;
     }
     break;
   case '+':
     if (apple.worth < 10) {
       apple.worth++;
     }
     break;
   case '-':
     if (apple.worth > 0) {
       apple.worth--;
     }
     break;
   case '_':
     if (apple.worth > 0) {
       apple.worth--;
     }
     break;
   
  }
}
void keyReleased() {  
  switch(key) {  
  case ' ':    
    fpaf = 10;    
    break;
  }
}
int randomInt(int max) {  
  return int(random(max));
}
void reset() {  
  apple.newPos();  
  snake.pos.x = width / 2;  
  snake.pos.y = height / 2;  
  pause = false;  
  showKeys = false;  
  noSave = "";  
  moves = new ArrayList<String>();  
  moves.add(" ");  
  framesOfBoutaDie = 0;  
  while (snake.bp.size() > 0) {    
    snake.bp.remove(snake.bp.size() - 1);
  }  
  snake.bp.add(new PVector(startPos.x - segSize, startPos.y));  
  for (int i = 1; i < startLen; i++) {       
    snake.bp.add(new PVector(segments.get(i-1).x - segSize, startPos.y));
  }
  snake.hasMoved = false;
}
void draw() {  
  numFrames++;  
  if (numFrames >= fpaf) {    
    background(0);    
    textAlign(LEFT);    
    fill(0, 0, 255);    
    textSize(20);    
    text(snake.bp.size() + 1, 1, 25);    
    if (!pause) {      
      moves = snake.newUpdate(moves, numFrames);      
      apple.display();      
      snake.display();      
      if (snake.ateApple(apple)) {
        for (int i = 0; i < apple.worth; i++){
          snake.grow();
        }
        if (playSound) {          
          eat.play();
        }        
        apple.newPos();
      }      
      if (snake.checkDead()) {        
        println(snake.bp.size() + 1);        
        if (playSound) {          
          oof.play();
        }        
        reset();
      }
    } else {      
      if (showKeys) {        
        pauseMenu.showKeys();
      } else {        
        pauseMenu.show();
      }
    }    
    numFrames = 0;
  }
}
