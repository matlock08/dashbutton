import RPi.GPIO as GPIO
import time
import smtplib

gpio_pin_number=18
pulse_last=0
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("XXXXXXXX@gmail.com", "XXXXXXX")
 
msg = "YOUR MESSAGE!"
server.sendmail("XXXXXXX@gmail.com", "XXXXXXXXXX", msg)
server.quit()

GPIO.setmode(GPIO.BCM)

GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        pulse_start = time.time()
        GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)        
        pulse_end = time.time()
        print('Button Pressed')

        if pulse_end - pulse_last > 50:
            print('-> Single Click')
        else
            print('-> Doble Click')
            

        pulse_last = pulse_end
        time.sleep(0.2)
        
except:
    GPIO.cleanup()
