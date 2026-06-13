import pywhatkit
import time

numbers = [
    "+919408015289",
    "+919104473913",
    "+919574380349"
]

for num in numbers:
    pywhatkit.sendwhatmsg_instantly(
        num,
        "Hii",
        wait_time=15,
        tab_close=True
    )
    
    