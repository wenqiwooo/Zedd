int const rOutPin = 9;
int const gOutPin = 10;
int const bOutPin = 11;

// Constants to identify the LED colour
int const RED = 9;
int const GREEN = 10;
int const BLUE = 11;

// Array of values of the RGB for the light settings
int white[] = {255, 255, 255};
int candle[] = {255, 147, 41};
int cool[] = {212, 235, 255};
int black[] = {167, 0, 255};
int party[] = {255, 255, 255};
int brightnessArray[] = {1, 2, 3, 4};

// Switch it on
int const ON = 1;
int const FADE = 2;
int const OFF = 0;

// Moods 
int const WHITE_LIGHT = 0;
int const CANDLE_LIGHT = 1;
int const COOL_LIGHT = 2;
int const BLACK_LIGHT = 3;
int const PARTY_LIGHT = 4;

int cmd = 1;
int R = 255;
int G = 255;
int B = 255;
int ambience = 1; 
int brightness = 1;

char control;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(rOutPin, OUTPUT);
  pinMode(gOutPin, OUTPUT);
  pinMode(bOutPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if(Serial.available()) {
    control = Serial.read();
  }
  setVariables(convert(control));
  
  if(cmd == ON) {
    setMood(ambience);      //Sets the R, G, B values to the values of the mood
    if(ambience == 4) {
      partySequence();
    } else {
      onAll(); 
    }
  } else if(cmd == FADE) {
    setBrightness(brightness, ambience);    //Sets the R, G, B values
    if(ambience == 4) {
      partySequence();
    } else {
      onAll(); 
    }
  } else {
    offAll();
  } 

  delay(4000);

  /*if(ambience== 5) {
    ambience = 0;
  } else {
    ambience = ambience + 1;
  }*/
  
  /*brightness = brightness + 1;
  if(brightness == 5) {
    brightness = 1;
  }*/
  offAll();
  delay(100);

}

int convert(char ans) {
  int cmd;
  if(ans == 'a') {
    cmd = 100;
  } else if(ans == 'b') {
    cmd = 101;
  } else if(ans == 'c') {
    cmd = 102;
  } else if(ans == 'd') {
    cmd = 103;
  } else if(ans == 'e') {
    cmd = 104;
  } else if(ans == 'f') {
    cmd = 201;
  } else if(ans == 'g') {
    cmd = 202;
  } else if(ans == 'h') {
    cmd = 203;
  } else if(ans == 'i') {
    cmd = 204;
  }  else if(ans == 'j') {
    cmd = 300;
  }
  return cmd;
}

void setVariables(int ans) {
  if(ans >= 100 && ans < 200) {
    cmd = ON;
    ambience = ans % 100;
  } else if(ans >= 200 && ans < 300) {
    cmd = FADE;
    brightness = ans % 200;
  } else {
    cmd = OFF;
  }
}

void setBrightness(int level, int mood) {
  setMood(mood);
  R = R / 4 * brightness;
  G = G / 4 * brightness;
  B = B / 4 * brightness;
}

void onAll() {
  analogWrite(RED, R);
  analogWrite(BLUE, B);
  analogWrite(GREEN, G); 
}

void offAll() {
  digitalWrite(RED, LOW);
  digitalWrite(GREEN, LOW);
  digitalWrite(BLUE, LOW);
}

void partySequence() {
  for(int i = 0; i < 10; i++) {
    flash(1);
    flash(1);
    flash(1);
    flash(2);
    flash(2);
    flash(2);
    flash(3);
    flash(3);
    flash(3);
    running();
  }
}

void set(int light, int value) {
  if(light == RED) {
    analogWrite(rOutPin, value);
  } else if(light == BLUE) {
    analogWrite(bOutPin, value);
  } else {
    analogWrite(gOutPin, value);
  }
}

void setMood(int mood) {
  if(mood == WHITE_LIGHT) {
    R = white[0];
    G = white[1];
    B = white[2];
  } else if(mood == CANDLE_LIGHT) {
    R = candle[0];
    G = candle[1];
    B = candle[2];
  } else if(mood == COOL_LIGHT) {
    R = cool[0];
    G = cool[1];
    B = cool[2];
  } else if(mood == BLACK_LIGHT) {
    R = black[0];
    G = black[1];
    B = black[2];
  } else {    //if(mood == PARTY)
    R = party[0];
    G = party[1];
    B = party[2];
  }
}

void running() {
  set(RED, R);
  delay(20);
  set(RED, OFF);
  delay(20);
  set(BLUE, B);
  delay(20);
  set(BLUE, OFF);
  delay(20);
  set(GREEN, G);
  delay(20);
  set(GREEN, OFF);
  delay(20);
}

void flash(int command) {
  if(command == 1) {    //flash red
    set(RED, R);
    delay(50);
    set(RED, OFF);
    delay(50);
  } else if(command == 2) {   //flash blue
    set(BLUE, B);
    delay(50);
    set(BLUE, OFF);
    delay(50);
  } else {              //flash green
    set(GREEN, G);
    delay(50);
    set(GREEN, OFF);
    delay(50);
  }
}
