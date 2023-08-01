# 1-3-simple-sync-right.py
#เรียกใช้ asyncio และ Time
import asyncio
import time

async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    # delay 1 seconds
    await asyncio.sleep(1)
    
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print (f'Task {name}: Computing {total}+{number}')
        # call asyncronous await function for do another work while waiting sleep working
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')
# set time Start.
start = time.time()
# build loop for get value.
loop = asyncio.get_event_loop()
tasks = [
    # build loop for get value.
    loop.create_task(sum("A", [1,2])),
    loop.create_task(sum("B", [1,2,3])),
]
# build loop for get value.
loop.run_until_complete(asyncio.wait(tasks))
#close the loop.
loop.close()
# set time End.
end = time.time()
print(f'Time: {end-start:.2f} sec')   
 