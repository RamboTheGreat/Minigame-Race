#include <Arduino.h>

#include <Adafruit_GFX.h>
#include <Adafruit_ILI9341.h>
// TFT display and SD card will share the hardware SPI interface.
// For the Adafruit shield, these are the default.
// The display uses hardware SPI, plus #9 & #10
// Mega2560 Wiring: connect TFT_CLK to 52, TFT_MISO to 50, and TFT_MOSI to 51
#define TFT_DC 9
#define TFT_CS 10
#define SD_CS 6

// Use hardware SPI (on Mega2560, #52, #51, and #50) and the above for CS/DC
Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC);
void setup() {
    init();
    Serial3.begin(9600);
    Serial.begin(9600);
    tft.begin();
}
int readSerial() {
    uint8_t byteread=Serial.read();
    if (byteread !=13) {
        Serial.write(byteread);
        Serial3.write(byteread);
    }
    else {
        Serial.write(13);
        Serial.write(10);
    }
    Serial.flush();
    return byteread;
}
int readSerial3() {
    uint8_t byteread=Serial3.read();
    /*if (byteread !=13) {
        Serial3.write(byteread);
    }
    else {
        Serial3.write(13);
        Serial3.write(10);
    }*/
    Serial.flush();
    return byteread;
}
int main() {
    setup();
    tft.fillScreen(ILI9341_BLACK);
    tft.setCursor(20,0);
    tft.setTextColor(ILI9341_WHITE);  tft.setTextSize(7);
    tft.println("Score");
    tft.println("\n");
    tft.setTextSize(6);
    int score=0;
    int otherscore=0;
    tft.setCursor(110,150);
    tft.print('-');
    while (true) {
        if (Serial.available()>0) {
            tft.setCursor(50,150);
            tft.setTextColor(ILI9341_BLACK);
            tft.print(score-48);
            tft.setTextColor(ILI9341_WHITE);
            score=readSerial();
            if (score<54) {
                tft.setCursor(50,150);
                tft.print(score-48);
            }
            else {
                tft.setCursor(70,120);
                tft.setTextColor(ILI9341_WHITE);
                tft.fillScreen(ILI9341_GREEN);
                tft.println("WIN");
                break;
            }

        }
        if (Serial3.available()>0) {
            tft.setCursor(170,150);
            tft.setTextColor(ILI9341_BLACK);
            tft.print(otherscore-48);
            tft.setTextColor(ILI9341_WHITE);
            otherscore=readSerial3();
            if (otherscore<54) {
                tft.setCursor(170,150);
                tft.print(otherscore-48);
            }
            else {
                tft.setCursor(50,120);
                tft.setTextColor(ILI9341_WHITE);
                tft.fillScreen(ILI9341_RED);
                tft.println("LOSE");
                break;
            }
        }
    }
    return 0;
}