class SaveGame {  
  void create() {    
    return;
  }  
  void openGame() {    
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
  void saveGame(Snake snek, Apple apple) {    
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
