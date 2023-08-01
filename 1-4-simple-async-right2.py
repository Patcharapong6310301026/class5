#1-4-simple-async-right2
# import asyncio and time
import asyncio
import time

async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    # delay 1 seconds
    await asyncio.sleep(1)
# plus number : add loop numbers to make value until complete.    
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        # call asyncronous await function for do another work while waiting sleep working
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

async def main():
    await asyncio.gather(sum("A", [1, 2]), sum("B", [1, 2, 3]))
    
if __name__ == '__main__':
     # set time Start.
    start = time.time()
    asyncio.run(main())
    # set time End.
    end = time.time()
    print(f'Time: {end-start:.2f} sec')        