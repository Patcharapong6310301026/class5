#2-2-basic-gather
# import asyncio and time
import asyncio
import time
# build hello function : sent output as started and done time.
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    # delay 4 seconds
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")
# build main and build 2 tasks    
async def main():
    # wrap the coro into a task and schedule its execution. Return the Task object.
    task1 = asyncio.create_task(hello(1)) #returns immediately, the task is created
    #await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    # task2 doesn't do anything until the event is set from task1.
    await asyncio.gather(task1, task2)
    
if __name__ == '__main__':
    # set time Start.
    start = time.time()
    # run main function.
    asyncio.run(main())
    # set time End.
    end = time.time()
    print(f'Time: {end-start:.2f} sec')