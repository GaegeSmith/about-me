import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import processing.sound.SoundFile; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class snakeProcessing extends PApplet {


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
public void setup() {  
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
public boolean vertical() {  
  if (moves.size() > 1) {    
    return moves.get(1).charAt(0) != 'w' && moves.get(1).charAt(0) != 's';
  }  
  return moves.get(0).charAt(0) != 'w' && moves.get(0).charAt(0) != 's';
}
public boolean horizontal() {  
  if (moves.size() > 1) {    
    return moves.get(1).charAt(0) != 'd' && moves.get(1).charAt(0) != 'a';
  }  
  return moves.get(0).charAt(0) != 'd' && moves.get(0).charAt(0) != 'a';
}
public void keyPressed() {  
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
public void keyReleased() {  
  switch(key) {  
  case ' ':    
    fpaf = 10;    
    break;
  }
}
public int randomInt(int max) {  
  return PApplet.parseInt(random(max));
}
public void reset() {  
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
public void draw() {  
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
class Apple {  
  PVector pos;  
  int size;
  int worth;
  public void constructor(PVector pos, int size, int worth) {    
    this.pos = pos;    
    this.size = size;
    this.worth = worth;
  }  
  public void newPos() {
    this.pos.x = (round(random((width / this.size) - 2)) + 1) * this.size;    
    this.pos.y = (round(random((height / this.size) - 2)) + 1) * this.size;
    while (snake.appleInside()) {
      this.pos.x = (round(random((width / this.size) - 2)) + 1) * this.size;    
      this.pos.y = (round(random((height / this.size) - 2)) + 1) * this.size;
    }
  }
  public void display() {    
    noStroke();    
    fill(255, 0, 0);    
    square(this.pos.x, this.pos.y, this.size);
  }
}
class Pause {    
  PVector pos;  
  PVector size;  
  String options = "";  
  String keyBinds = "";    
  public void constructor(PVector pos, PVector size, ArrayList<String> opts, ArrayList<String> controls) {    
    this.pos = pos;    
    this.size = size;    
    for (int i = 0; i < opts.size(); i++) {      
      this.options = this.options + opts.get(i) + "\n";
    }        
    for (int i = 0; i < controls.size(); i++) {      
      this.keyBinds = this.keyBinds + controls.get(i) + "\n";
    }
  }       
  public void show() {    
    textAlign(CENTER, CENTER);    
    text(this.options + "\n" + noSave, width / 2, height / 2);
  }    
  public void showKeys() {    
    textAlign(CENTER, CENTER);    
    text(this.keyBinds, width / 2, height / 2);
  }
}
class Snake {  
  PVector pos;
  boolean hasMoved;
  ArrayList<PVector> bp;  
  int segSize;  
  public void constructor(PVector headPos, ArrayList bodyParts, int segSize) {    
    this.pos = headPos;    
    this.bp = bodyParts;    
    this.segSize = segSize;
    this.hasMoved = false;
  }
  public boolean appleInside() {
    if (this.pos.x == apple.pos.x && this.pos.y == apple.pos.y) {
      return true;
    }
    for (int i = 0; i < this.bp.size(); i++) {
      if (this.bp.get(i).x == apple.pos.x && this.bp.get(i).y == apple.pos.y) {
        return true;
      }
    }
    return false;
  }
  public boolean checkIfBoutaDie() {    
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
  public ArrayList<String> newUpdate(ArrayList<String> moves, int numFrame) {    
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
  public boolean checkDead() {    
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
  public void moveBody() {
    if (!this.hasMoved) {this.hasMoved = true;}
    for (int i = this.bp.size() - 1; i > 0; i--) {      
      this.bp.get(i).x = this.bp.get(i-1).x;      
      this.bp.get(i).y = this.bp.get(i-1).y;
    }    
    this.bp.get(0).y = this.pos.y;    
    this.bp.get(0).x = this.pos.x;
  }  
  public boolean ateApple(Apple apple) {    
    return (this.pos.x == apple.pos.x && this.pos.y == apple.pos.y);
  }  
  public void grow() {    
    this.bp.add(new PVector(700, 700));
  }  
  public void display() {    
    fill(0, 230, 0);    
    stroke(0);    
    for (int i = 0; i < this.bp.size(); i++) {      
      square(this.bp.get(i).x, this.bp.get(i).y, this.segSize);
    }   
    fill(0, 230, 0);    
    square(this.pos.x, this.pos.y, this.segSize);
  }
}
class SaveGame {  
  public void create() {    
    return;
  }  
  public void openGame() {    
    JSONObject game = loadJSONObject("data\\game.json");    
    apple.pos.x = game.getJSONObject("apple").getFloat("x");    
    apple.pos.y = game.getJSONObject("apple").getFloat("y");    
    moves = new ArrayList<String>();    
    snake.bp = new ArrayList<PVector>();       
    for (int i = 0; i < game.getJSONArray("moves").size(); i++) {      
      moves.add(game.getJSONArray("moves").getJSONObject(i).getString(str(i)));
    }    
    for (int i = 0; i < game.getJSONArray("snake").size(); i++) {      
      if (i == 0) {        
        snake.pos.x = game.getJSONArray("snake").getJSONObject(i).getFloat("x");        
        snake.pos.y = game.getJSONArray("snake").getJSONObject(i).getFloat("y");
      }      
      try {        
        snake.bp.set(i, new PVector(          game.getJSONArray("snake").getJSONObject(i + 1).getFloat("x"), game.getJSONArray("snake").getJSONObject(i + 1).getFloat("y")          )          );
      }      
      catch(Exception e) {        
        try {          
          snake.bp.add(new PVector(            game.getJSONArray("snake").getJSONObject(i + 1).getFloat("x"), game.getJSONArray("snake").getJSONObject(i + 1).getFloat("y")            )            );
        }        
        catch(Exception ea) {
        }
      }
    }
  }  
  public void saveGame(Snake snek, Apple apple) {    
    JSONArray snake = new JSONArray();    
    JSONArray moveJSON = new JSONArray();    
    JSONObject move = new JSONObject();    
    JSONObject game = new JSONObject();    
    JSONObject app = new JSONObject();    
    JSONObject seg = new JSONObject();    
    seg.setFloat("x", snek.pos.x);    
    seg.setFloat("y", snek.pos.y);    
    snake.setJSONObject(0, seg);    
    for (int i = 0; i < snek.bp.size(); i++) {      
      seg = new JSONObject();      
      seg.setFloat("x", snek.bp.get(i).x);      
      seg.setFloat("y", snek.bp.get(i).y);      
      snake.setJSONObject(i + 1, seg);
    }    
    game.setJSONArray("snake", snake);    
    app.setFloat("x", apple.pos.x);    
    app.setFloat("y", apple.pos.y);    
    game.setJSONObject("apple", app);    
    for (int i = 0; i < moves.size(); i++) {      
      move = new JSONObject();      
      move.setString(str(i), moves.get(i));      
      moveJSON.setJSONObject(i, move);
    }    
    game.setJSONArray("moves", moveJSON);    
    saveJSONObject(game, "data/game.json");
  }
}
  public void settings() {  size(600, 600); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "snakeProcessing" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
