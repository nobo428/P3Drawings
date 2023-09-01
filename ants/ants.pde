int cols, rows;
int scl = 20;
float[][] flowfield;
int particleCount = 10000;
Particle[] particles;

void setup() {
  size(800, 800);
  cols = floor(width/scl);
  rows = floor(height/scl);
  flowfield = new float[cols][rows];
  for (int x = 0; x < cols; x++) {
    for (int y = 0; y < rows; y++) {
      flowfield[x][y] = random(TWO_PI);
    }
  }
  particles = new Particle[particleCount];
  for (int i = 0; i < particles.length; i++) {
    particles[i] = new Particle();
  }
}

void draw() {
  background(255);
  for (int x = 0; x < cols; x++) {
    for (int y = 0; y < rows; y++) {
      int index = x + y * cols;
      float angle = flowfield[x][y];
      stroke(0);
      strokeWeight(0);
      pushMatrix();
      translate(x*scl, y*scl);
      rotate(angle);
      line(0, 0, scl, 0);
      popMatrix();
    }
  }
  for (Particle p : particles) {
    p.follow(flowfield);
    p.update();
    p.edges();
    p.show();
  }
}

class Particle {
  PVector pos, vel, acc;

  Particle() {
    pos = new PVector(random(width), random(height));
    vel = new PVector();
    acc = new PVector();
  }

  void follow(float[][] flowfield) {
    int x = floor(pos.x / scl);
    int y = floor(pos.y / scl);
    float xOff = pos.x / scl - x;
    float yOff = pos.y / scl - y;
    if (x >= 0 && x < cols-1 && y >= 0 && y < rows-1) {
      int index = x + y * cols;
      float angle1 = flowfield[x][y];
      float angle2 = flowfield[x+1][y];
      float angle3 = flowfield[x][y+1];
      float angle4 = flowfield[x+1][y+1];
      float angle = lerp(lerp(angle1, angle2, xOff), lerp(angle3, angle4, xOff), yOff);
      angle += random(-1, 1);
      vel.x = cos(angle);
      vel.y = sin(angle);
      vel.normalize();
      vel.mult(2);
    }
  }

  void update() {
    pos.add(vel);
  }

  void show() {
    stroke(0);
    strokeWeight(3);
    point(pos.x, pos.y);
  }

  void edges() {
    if (pos.x > width) pos.x = 0;
    if (pos.x < 0) pos.x = width;
    if (pos.y > height) pos.y = 0;
    if (pos.y < 0) pos.y = height;
  }
}
