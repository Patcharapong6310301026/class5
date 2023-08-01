# 1-2-simple-sync-wrong.py
#เรียกใช้ asyncio และ Time
import asyncio
import time
# การทำงานdefโดยกำหนดเป็นsleepทำการโชว์ time ต่อวินาที
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await sleep(1)
# บวกเลข : เพิ่มเลขไปเรื่อยๆจนกว่าจะถึงค่าที่กำหนดไว้.
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        #call asyncronous await function for do another work while waiting sleep working
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')
# set time Start.    
start = time.time()
# build loop for get value.
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
# loop run until complete.
loop.run_until_complete(asyncio.wait(tasks))
# close the loop.
loop.close()
# set time End.
end = time.time()
print(f'Time: {end-start:.2f} sec')