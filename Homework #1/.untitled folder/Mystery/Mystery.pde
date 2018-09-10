class gravitystar  //class for the gravity stars
{
  float x, y; //declares two variables for position
  void update() //update function, used for animation
  { 
    float r1 = random(0, 2*PI); //creates a random angle betewwn 0 & 360°
    float r2 = random(10, 15); //creates a random length between 10 and 15
    stroke(98, 233, 255); //sets the line color to "Spacewar!" blue
    line(x + r2*cos(r1), y + r2*sin(r1), x - r2*cos(r1), y - r2*sin(r1)); //draws a line with the random length and angle and length that passes through the center of the star
    stroke(0); //sets the line color to black
    fill(0,30); //sets the fill color to black with 30% opacity
    ellipse(x, y, 40, 40); //draws a circle over the star, this achieves the crt "ghosting" effect present on the original program for the gravity star
  }
}
class spaceship //class for the spaceships
{
  float xspeed, yspeed, x, y, angleofRotation, angleofAcceleration, forceofGravity, angleofAttraction, reloadTime; //declares variables used for the spaceship class
  boolean dead, exploded, turningLeft, turningRight, thrusterOn = false; //more booleans used for the spaceship class
  void drawErase(boolean draw)//the drawErase function, can be used for both drawing and erasing
  {
    if(draw) //if the function was called drawing, do the following:
    {
    stroke(98, 233, 255); //sets the line color to "Spacewar!" blue
    triangle((x + 10*cos(angleofRotation + (3*PI/4))), (y + 10*sin(angleofRotation + (3*PI/4))), (x + 10*cos(angleofRotation)), (y + 10*sin(angleofRotation)), (x + 10*cos(angleofRotation - (3*PI/4))), (y + 10*sin(angleofRotation - (3*PI/4)))); //draws a triangle which represents the spaceship, based upon the anle of rotation
    }
    else //if the function was called for erasing, do the following:
    {
    fill(0); //sets the fll color to black
    stroke(0); //sets the line color to black
    triangle((x + 25*cos(angleofRotation + (3*PI/4))), (y + 25*sin(angleofRotation + (3*PI/4))), (x + 25*cos(angleofRotation)), (y + 25*sin(angleofRotation)), (x + 25*cos(angleofRotation - (3*PI/4))), (y + 25*sin(angleofRotation - (3*PI/4)))); //does the same to erase, except draws a larger triangle to compensate for movement
    }
  }
  void update(ArrayList<gravitystar> stars, ArrayList<spaceship> ships, ArrayList<torpedo> torpedoes) //update function for the spaceship
  {
    if(dead == false) //if the spaceship has not exploded, do the following
    { 
      drawErase(false); //erases the ship
      x += xspeed; //applies the ship's speed in the x direction to its x position 
      y += yspeed; //applies the ship's speed in the y direction to its y position 
      drawErase(true); //re draw the ship
      for(int i = 0; i < stars.size(); i++) //repeats this process for each star
      {
      gravitystar star = stars.get(i); //select a star
      forceofGravity = 100/pow(dist(star.x, star.y, x, y), 1.7); //calculates the force of attraction, or gravity, between the ship and the selected star based upon the distance between them and raising it to the power 0f 1.7
      angleofAttraction = atan2((star.y - y), (star.x - x)); //calculates the angle between the ship and the selected star
      xspeed += forceofGravity*cos(angleofAttraction); //applies gravitational acceleration to the speed of the ship in the x direction by taking the cosine of the angle between the two bodies and multiplying it by the force of attraction
      yspeed += forceofGravity*sin(angleofAttraction); //applies gravitational acceleration to the speed of the ship in the y direction by taking the sine of the angle between the two bodies and multiplying it by the force of attraction
      if(dist(x,y, star.x, star.y) < 20) //if the distance between the ship and the selected star is less than 20, do the following:
      {
        dead = true; //assumes the two have collided, and marks the ship as destroyed
      }
      }
      for(int i = 0; i<ships.size(); i++) //repeats this for each ship
      {
        spaceship ship = ships.get(i); //selects a ship
        if(dist(x,y, ship.x, ship.y) < 20 && (x != ship.x && y !=ship.y)) //if the distance between the ship and the selected ship is less than 20, do the following:
        {
          dead = true; //assumes the two have collided, and marks the ship as destroyed
        }
      }
      for(int i = 0; i<torpedoes.size(); i++) //repeats this for each torpedo
      {
        torpedo torp = torpedoes.get(i); //select a torpedo
        if(dist(x,y, torp.x, torp.y) < 20 && (x != torp.x && y != torp.y)) //if the distance between the ship and the selected torpedo is less than 20, do the following:
        {
          dead = true; //assumes the ship has been shot, and marks the ship as destroyed
        }
      }
      if(turningLeft) //if the ship is turning left, do the following
      {
        angleofRotation -= 0.07; //rotates the ship -0.07 radians clockwise
      }
      if(turningRight)
      {
        angleofRotation += 0.07; //rotates the ship -0.07 radians counter-clockwise
      }
      if(thrusterOn) //if the ship has its thruster ignited, do the following
      {
        angleofAcceleration = angleofRotation; //sets the angle of acceleration to the angle of rotation
        xspeed += 0.03*cos(angleofAcceleration); //applies acceleration from the thruster to the speed of the ship in the x direction using similar trigonometry as before
        yspeed += 0.03*sin(angleofAcceleration); //applies acceleration from the thruster to the speed of the ship in the y direction using similar trigonometry as before
        stroke(255, 188, 77); //sets the line color to orange
        float r = random(7, 15); //creates a random flame particle size between 7 & 15
        triangle((x + 7*cos(angleofRotation + (3*PI/4))), (y + 7*sin(angleofRotation + (3*PI/4))), (x + r*cos(angleofRotation + PI)), (y + r*sin(angleofRotation + PI)), (x + 7*cos(angleofRotation - (3*PI/4))), (y + 7*sin(angleofRotation - (3*PI/4)))); //creates thruster particles in the shape of triangles in a similar fasion to before
      }
      if(reloadTime > 0) //if the reload time is greater than zero, do the following:
      {
        reloadTime--; //decreases the reload time by 1
      }
    }
    if(dead == true) //if the ship is dead, do the following:
    {
      if(exploded == false) //if the ship has not already exploded, do the following:
      {
        drawErase(false); //erases the ship
        for(int i = 0; i < 300; i++) //repeats this 300 times
        { 
          stroke(255, 188, 77); //sets the line color to orange
          float r1 = random(0,(i/5)); //creates a randomd distance from the center
          float r2 = random(0, 2*PI); //creates a random angle
          point((x + r1*cos(r2)), (y + r1*(sin(r2)))); //plots an explosion particle with the pre-determined distance and angle
        }
        exploded = true; //tells the computer that the ship has already exploded
      }
    }
    if(x > 1280) //if the ship has moved past the right side of the screen, do the following:
    {
      xspeed *= -0.5; //bounces the ship in the opposite direction
      x = 1270; //sets the x position of the ship to slightly to the left of the right edge of the screen
    }
    if(x < 0) //if the ship has moved past the left side of the screen, do the following:
    {
      xspeed *= -0.5; //bounces the ship in the opposite direction
      x = 10; //sets the x position of the ship to slightly to the right of the left edge of the screen
    }
    if(y > 740) //if the ship has moved past the bottom of the screen, do the following:
    {
      yspeed *= -0.5; //bounces the ship in the opposite direction
      y = 730; //sets the y position of the ship to slightly above the bottom of the screen
    }
    if(y < 0) //if the ship has moved past the top of the screen, do the following:
    {
      yspeed *= -0.5; //bounces the ship in the opposite direction
      y = 10; //sets the y position of the ship to slightly below the top of the screen
    }
  }
}
class torpedo //class for the torpedoes
{
  float x, y, xspeed, yspeed, angleofAcceleration, forceofGravity, angleofAttraction; //variables used for the torpedo class
  boolean detonated; //another boolean used by the torpedo class
  void update(ArrayList<gravitystar> stars, ArrayList<spaceship> ships) //update function for the torpedo class
  {
    if(detonated != true) //if the torpedo has not detonated, do the following: 
    {
      for(int i = 0; i<ships.size(); i++) //repeats this for every ship
      {
        spaceship ship = ships.get(i); //selects a ship
        if(dist(x,y, ship.x, ship.y) < 20 && (x != ship.x && y !=ship.y)) //if the distance between the torpedo and the selected ship is less than 20, do the following:
        {
          detonated = true; //assumes the two have collided and marks the torpedo as detonated
        }
      }
      for(int i = 0; i < stars.size(); i++) //repeats this for every star
      {
        gravitystar star = stars.get(i); //selects a star
        forceofGravity = 550/pow(dist(star.x, star.y, x, y), 1.7); //calculates the force of attraction, or gravity, between the torpedo and the selected star based upon the distance between them and raising it to the power 0f 1.7 
        angleofAttraction = atan2((star.y - y), (star.x - x)); //calculates the angle between the torpedo and the selected star
        xspeed += forceofGravity*cos(angleofAttraction); //applies gravitational acceleration to the speed of the torpedo in the x direction by taking the cosine of the angle between the two bodies and multiplying it by the force of attraction
        yspeed += forceofGravity*sin(angleofAttraction); //applies gravitational acceleration to the speed of the torpedo in the x direction by taking the cosine of the angle between the two bodies and multiplying it by the force of attraction
        if(dist(x,y, star.x, star.y) < 20 && (x != star.x && y !=star.y)) //if the distance between the torpedo and the selected star is less than 20, do the following:
        {
          detonated = true;//assumes the two have collided and marks the torpedo as detonated
        }
      }
      x += xspeed; //applies the torpedoes's speed in the x direction to its x position
      y += yspeed; //applies the torpedoes's speed in the x direction to its y position
      stroke(0, 205, 88); //sets the fill color to green
      ellipse(x, y, 1, 1); //draws tracer particles
    }
    if(detonated == true) //if the torpedo has detonated, do the following:
    {
      x = 100000; //teleport the torpedo far off screen
      y = 100000;
    }
    if(x > 1280) //if the torpedo has gone off the right edge of the screen do the following:
    {
      x = 100000; //teleport the torpedo far off screen
      y = 100000;
    }
    if(x < 0) //if the torpedo has gone off the left edge of the screen do the following:
    {
      x = 100000; //teleport the torpedo far off screen
      y = 100000;
    }
    if(y > 800) //if the torpedo has gone off the bottom edge of the screen do the following:
    {
      x = 100000; //teleport the torpedo far off screen
      y = 100000;
    }
    if(y < 0) //if the torpedo has gone off the top edge of the screen do the following:
    {
      x = 100000; //teleport the torpedo far off screen
      y = 100000;
    }
  }
}
ArrayList<gravitystar> stars = new ArrayList<gravitystar>(); //creates a list of stars
ArrayList<spaceship> ships = new ArrayList<spaceship>(); //creates a list of ships
ArrayList<torpedo> torpedoes = new ArrayList<torpedo>(); //creates a list of torpedoes
void keyPressed()
{
  spaceship ship1 = ships.get(0); //selects ship 1 as the first ship in the list of ships
  spaceship ship2 = ships.get(1); //selects ship 2 as the second ship in the list of ships
  if(key == 'w') //if the key w is pressed, do the following:
  { 
    if(ship1.reloadTime == 0) //if the ship has finished reloading do the following:
    {
      torpedo torp = new torpedo(); //creates a new torpedo
      torpedoes.add(torp); //adds it to the list of torpedoes
      torp.x = ship1.x + 35*cos(ship1.angleofRotation); //sets the torpedo's x position based upon the ship's angle, the torpedo is placed 35 pixels from the center of the ship in the front
      torp.y = ship1.y + 35*sin(ship1.angleofRotation); //sets the torpedo's y position based upon the ship's angle, the torpedo is placed 35 pixels from the center of the ship in the front
      torp.angleofAcceleration = ship1.angleofRotation; //sets the angle of the torpedo based upon the ship's angle
      torp.xspeed = 10*cos(torp.angleofAcceleration); //sets the torpedoe's speed in the x direction, the speed of the torpedo is 10
      torp.yspeed = 10*sin(torp.angleofAcceleration); //sets the torpedoe's speed in the y direction, the speed of the torpedo is 10
      ship1.reloadTime = 30; //sets the reload time of the ship to 30 frames, which is 1 second
    }
  }
  if(key == 'a')//if the key "a" is pressed, do the following:
  {
    ship1.turningLeft = true; //tells the computer that ship1 is turning left
  }
  if(key == 's')//if the key "s" is pressed, do the following:
  {
    ship1.thrusterOn = true; //tells the computer that ship1's thruster is on
  }
  if(key == 'd')//if the key "d" is pressed, do the following:
  {
    ship1.turningRight = true; //tells the computer that ship1 is turning right
  }
  if(key == 'i')//the code below is the same as ship1, but repurposed for ship2
  { 
    if(ship2.reloadTime == 0)
    {
      torpedo torp = new torpedo();
      torpedoes.add(torp);
      torp.x = ship2.x + 35*cos(ship2.angleofRotation);
      torp.y = ship2.y + 35*sin(ship2.angleofRotation);
      torp.angleofAcceleration = ship2.angleofRotation;
      torp.xspeed = 10*cos(torp.angleofAcceleration);
      torp.yspeed = 10*sin(torp.angleofAcceleration);
      ship2.reloadTime = 30;
    }
  }
  if(key == 'j')
  {
    ship2.turningLeft = true;
  }
  if(key == 'k')
  {
    ship2.thrusterOn = true;
  }
  if(key == 'l')
  {
    ship2.turningRight = true;
  }
}
void keyReleased() //if any key has been released, cancel the effects of any pressed key
{
  spaceship ship1 = ships.get(0);
  spaceship ship2 = ships.get(1);
  if(key == 'w')
  {
  }
  if(key == 'a')
  {
    ship1.turningLeft = false;
  }
  if(key == 's')
  {
    ship1.thrusterOn = false;
  }
  if(key == 'd')
  {
    ship1.turningRight = false;
  }
  if(key == 'j')
  {
    ship2.turningLeft = false;
  }
  if(key == 'k')
  {
    ship2.thrusterOn = false;
  }
  if(key == 'l')
  {
    ship2.turningRight = false;
  }
}
void setup() //Initializing content
{
 size(1280, 800); //sets the screen size to 180x800 pixels, the resolution of my MacBook Pro
 background(0); //sets the background color to black
 for(int i = 0; i < 4; i++)//repeats this 4 times
 {
   stars.add(new gravitystar()); //creates a new star and adds it to the list of stars
 }
 stars.get(0).x = 490; //sets the initial position of each star
 stars.get(0).y = 250;
 stars.get(1).x = 690;
 stars.get(1).y = 550;
 stars.get(2).x = 940;
 stars.get(2).y = 400;
 stars.get(3).x = 140;
 stars.get(3).y = 700;
 for(int i = 0; i < 2; i++) //repeats this twice
 {
   ships.add(new spaceship()); //creates a new ship and adds it to the list of ships
 }
 ships.get(0).x = 100; //sets the initial position and rotation of the ships
 ships.get(0).y = 100;
 ships.get(1).x = 1180;
 ships.get(1).y = 700;
 ships.get(1).angleofRotation = PI;
}
void draw()
{
  stroke(0); //sets the line color to black
  fill(0, 10); //sets the fill color to black, with 10% opacity
  rect(0, 0, 1280, 800); //creates the "ghosting effect for the torpedo tracer particles
  for(int i = 0; i < stars.size(); i++) //updates the stars
  {
    stars.get(i).update();
  }
  for(int i = 0; i < ships.size(); i++) //updates the ships
  {
    ships.get(i).update(stars, ships, torpedoes);
    if(ships.get(i).exploded == true)//if a ship explodes, reset the game
    {
      ships.get(0).x = 100;
      ships.get(0).y = 100;
      ships.get(1).x = 1180;
      ships.get(1).y = 700;
      ships.get(0).xspeed = 0;
      ships.get(0).yspeed = 0;
      ships.get(1).xspeed = 0;
      ships.get(1).yspeed = 0;
      ships.get(0).dead = false;
      ships.get(1).dead = false;
      ships.get(0).exploded = false;
      ships.get(1).exploded = false;
      ships.get(0).angleofRotation = 0;
      ships.get(1).angleofRotation = PI;
      for(int j = 0; j < torpedoes.size(); j++)
      {
        torpedoes.get(j).detonated = true; 
      }
    }
  }
  for(int i = 0; i < torpedoes.size(); i++) //updates the torpedoes
  {
    torpedoes.get(i).update(stars, ships);
  }
}
