boolean w, a, s, d, game_over;
int counter, reload;
void keyPressed()
{
  if(key == 'w')
  {
    w = true;
  }
  if(key == 'a')
  {
    a = true;
  }
  if(key == 's')
  {
    s = true;
  }
  if(key == 'd')
  {
    d = true;
  }
  if(key == ' ')
  {
    if(reload <= 0)
    {
      projectile projectile1 = new projectile();
      projectile1.init(player1.x + 40*cos(player1.r), player1.y, player1.z + 40*sin(player1.r), player1.r);
      projectiles.add(projectile1);
      reload = 15;
    }
  }
}

void keyReleased()
{
  if(key == 'w')
  {
    w = false;
  }
   if(key == 'a')
  {
    a = false;
  }
   if(key == 's')
  {
    s = false;
  }
   if(key == 'd')
  {
    d = false;
  }
}
class projectile
{
  float x, y, z, xspeed, yspeed, zspeed, r;
  void init(float xpos, float ypos, float zpos, float angle)
  {
    r = angle;
    x = xpos;
    y = ypos + 10;
    z = zpos;
    xspeed = 7*cos(r);
    zspeed = 7*sin(r);
  }
  void update()
  {
   x += xspeed;
   z += zspeed;
   strokeWeight(8);
   line(x, y, z, x + 100*cos(r), y, z + 100*sin(r));
   strokeWeight(1);
  }
  void collision(ArrayList<enemy> enemies)
  {
    for(int i  = 0; i < enemies.size(); i++)
    {
      if(dist(x, y, z, enemies.get(i).x, enemies.get(i).y, enemies.get(i).z) < 40)
      {
        enemies.remove(i);
      }
    }
  }
}
class enemy
{
 float x, y, z, xspeed, zspeed, r, a;
 int counter;
 boolean dead;
 void init(float xpos, float ypos, float zpos)
 {
   x = xpos;
   y = ypos;
   z = zpos;
 }
 void update(player player1)
 {
   a = atan2((player1.z - z), (player1.x - x));
   if(counter == 0)
   {
     xspeed = cos(a) + random(-1, 1);
     zspeed = sin(a) + random(-1, 1);
     counter = 120;
   }
   counter--;
   x += xspeed;
   z += zspeed;
   translate(x, y, z);
   sphere(40);
   translate(-x, -y, -z);
 }
}

class pyramid
{
  float x, y, z, size = 0;
  void init(float xpos, float ypos, float zpos, float scale)
  {
    x = xpos;
    y = ypos;
    z = zpos;
    size = scale;
  }
  void update()
  {
    translate(x, y, z);
    stroke(0,255,0);
    noFill();
    
    beginShape(TRIANGLES);
    vertex(-size, size, -size);
    vertex( size, size, -size);
    vertex(   0,    -size,  0);
    
    vertex( size, size, -size);
    vertex( size,  size, size);
    vertex(   0,    -size,  0);
    
    vertex( size, size, size);
    vertex(-size, size, size);
    vertex(   0,   -size,  0);
    
    vertex(-size,  size, size);
    vertex(-size, size, -size);
    vertex(   0,  -size,  0);
    endShape();
    
    translate(-x, -y, -z);
  }
  void collision(ArrayList<projectile> projectiles)
  {
    for(int i  = 0; i < projectiles.size(); i++)
    {
      if(dist(x, z, projectiles.get(i).x, projectiles.get(i).z) < 40)
      {
        projectiles.remove(i);
      }
    }
  }
}
class box
{
  float x, y, z, size = 0;
  void init(float xpos, float ypos, float zpos, float scale)
  {
    x = xpos;
    y = ypos;
    z = zpos;
    size = scale;
  }
  void update()
  {
    translate(x, y, z);
    stroke(0,255,0);
    noFill();
    box(size);
    translate(-x, -y, -z);
  }
  void collision(ArrayList<projectile> projectiles)
  {
    for(int i  = 0; i < projectiles.size(); i++)
    {
      if(dist(x, z, projectiles.get(i).x, projectiles.get(i).z) < 40)
      {
        projectiles.remove(i);
      }
    }
  }
}
class player
{
  float x, y, z, r, c = 0;
  void init(float xpos, float ypos, float zpos, float angle)
  {
    x = xpos;
    y = ypos;
    z = zpos;
    r = angle;
  }
  void update()
  {
    if(w == true && c != 1)
    {
      x += 3*cos(r);
      z += 3*sin(r);
    }
    if(s == true && c != 2)
    {
      x -= 3*cos(r);
      z -= 3*sin(r);
    }
    if(a == true)
    {
      r -= 0.01;
    }
    if(d == true)
    {
      r += 0.01;
    }
    camera(x, y, z, x + 40*cos(r), y, z + 40*sin(r), 0, 1, 0);
    c = 0;
  }
  void collision(ArrayList<box> boxes, ArrayList<pyramid> pyramids)
  {
    for(int i = 0; i < boxes.size(); i++)
    {
      if(x + 40*cos(r) < boxes.get(i).x + 40 && z + 40*sin(r) < boxes.get(i).z + 40)
      {
        if(x + 40*cos(r) > boxes.get(i).x - 40 && z + 40*sin(r) > boxes.get(i).z - 40)
        {
          c = 1;
        }
      }
      if(x - 40*cos(r) < boxes.get(i).x + 40 && z - 40*sin(r) < boxes.get(i).z + 40)
      {
        if(x - 40*cos(r) > boxes.get(i).x - 40 && z - 40*sin(r) > boxes.get(i).z - 40)
        {
          c = 2;
        }
      }
    }
    
    for(int i = 0; i < pyramids.size(); i++)
    {
      if(x + 40*cos(r) < pyramids.get(i).x + 40 && z + 40*sin(r) < pyramids.get(i).z + 40)
      {
        if(x + 40*cos(r) > pyramids.get(i).x - 40 && z + 40*sin(r) > pyramids.get(i).z - 40)
        {
          c = 1;
        }
      }
      if(x - 40*cos(r) < pyramids.get(i).x + 40 && z - 40*sin(r) < pyramids.get(i).z + 40)
      {
        if(x - 40*cos(r) > pyramids.get(i).x - 40 && z - 40*sin(r) > pyramids.get(i).z - 40)
        {
          c = 2;
        }
      }
    }
  }
}
ArrayList<projectile> projectiles = new ArrayList<projectile>();
ArrayList<enemy> enemies = new ArrayList<enemy>();
ArrayList<box> boxes = new ArrayList<box>();
ArrayList<pyramid> pyramids = new ArrayList<pyramid>();
player player1 = new player();
void setup()
{
  for(int i = 0; i < 10; i++)
  {
    enemies.add(new enemy());
  }
  for(int i = 0; i < 50; i++)
  {
    boxes.add(new box());
  }
  for(int i = 0; i < enemies.size(); i+=2)
  {
    enemies.get(i).init(random(-2048,-512), 384, random(-2048, -512));
    enemies.get(i+1).init(random(512,2048), 384, random(512, 2048));
  }
  for(int i = 0; i < 50; i++)
  {
    pyramids.add(new pyramid());
  }
  for(int i = 0; i < boxes.size(); i++)
  {
    boxes.get(i).init(20*random(-128, 128), 384, 20*random(-128, 128), 80);
  }
  for(int i = 0; i < pyramids.size(); i++)
  {
    pyramids.get(i).init(20*random(-128, 128), 384, 20*random(-128, 128), 40);
  }
  size(1024, 768, P3D);
  background(0);
  player1.init(512, 384, 0, PI/2);
}
void draw()
{
  if(counter == 0)
  {
    enemies.add(new enemy());
    enemies.get(enemies.size() - 1).init(random(-2048,2048), 384, random(-2048, 2048));
    if(dist(enemies.get(enemies.size() - 1).x, enemies.get(enemies.size() - 1).z, player1.x, player1.z) < 40)
    {
      enemies.remove(enemies.size() - 1);
    }
    counter = enemies.size()*30;
  }
  counter--;
  background(0);
  for(int i = 0; i < projectiles.size(); i++)
  {
    projectiles.get(i).update();
  }
  for(int i = 0; i < boxes.size(); i++)
  {
    boxes.get(i).update();
    boxes.get(i).collision(projectiles);
  }
  for(int i = 0; i < pyramids.size(); i++)
  {
    pyramids.get(i).update();
    pyramids.get(i).collision(projectiles);
  }
  for(int i = 0; i < projectiles.size(); i++)
  {
    projectiles.get(i).collision(enemies);
    if(dist(projectiles.get(i).x, projectiles.get(i).z, player1.x, player1.z) > 500)
    {
      projectiles.remove(i);
    }
  }
  for(int i = 0; i < enemies.size(); i++)
  {
    enemies.get(i).update(player1);
    if(dist(enemies.get(i).x, enemies.get(i).z, player1.x, player1.z) < 40)
    {
      game_over = true;
    }
  }
  player1.collision(boxes, pyramids);
  player1.update();
  if(game_over == true)
  {
    player1.init(512, 384, 100, 3*PI/2);
    textSize(12);
    fill(0, 255, 0);
    text("YOU DIED", 480, 384, 0);
  }
  reload--;
}
