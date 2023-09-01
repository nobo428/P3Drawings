int count = 230;

void setup(){
 size(1280, 720); 
 frameRate(20);
 smooth();
 background(165, 209, 242);
 fill(241, 242, 165);
 stroke(241, 242, 165);
 ellipse(2*width/3, 100, 100, 100);
}

void draw(){
  float curve = random(10);
  makeLine(int(curve)+20, count);
  count += 10;
  if (count > 720){
     stop(); 
  }
}
void makeLine(int numKinks, int count){
  //float starth = random(height);
  float[][] kinks = new float[numKinks][2];
  //float endh = random(height+1);
  int wiggle = 10 + count/40;
  
  for(int i = 0; i < numKinks; i++){
    for(int j = 0; j<2; j++){
      if(j==0){
       kinks[i][j] = (i+1) * width/(numKinks + 1);
      } else if (i == 0) {
        kinks[i][j] = count;
      } else {
        kinks[i][j] = kinks[0][1] + random(wiggle) * random(-1,1);
      }
    }
  }
   
  colorMode(HSB);
  stroke(random(152,158), 0.3*kinks[0][1] - 10, 330 - .45* kinks[0][1]);
  strokeWeight(10 + kinks[0][1] * .08);
  
  //line(0, starth, kinks[0][0], kinks[0][1]);
  
  for(int q = 0; q < numKinks-1; q++){
    line(kinks[q][0], kinks[q][1], kinks[q+1][0], kinks[q+1][1]);
  }
  
  //line(kinks[numKinks-1][0], kinks[numKinks-1][1], width, endh);
  
}

void mousePressed(){
  noLoop();
  setup();
  loop();
}
