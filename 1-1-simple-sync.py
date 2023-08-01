# 1-1-simple-sync.py
#เรียกใช้ Time
import time
# การทำงานdefโดยกำหนดเป็นsleepทำการโชว์ time ต่อวินาที
def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1) #ดีเลย์เวลา 1 วิ
    

# def sum สร้างloopเลข จนกว่าค่าจะเต็ม
def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')
#set time start
start = time.time()
#work value
tasks = [
    sum("A", [1,2]),
    sum("B", [1,2,3]),
]
#set time End.
end = time.time()
print(f'Time: {end-start: 2f} sec')