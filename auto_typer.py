import argparse
import pyautogui as auto
import time

parser = argparse.ArgumentParser(description='This script reads from a text file and types its contents on the focused window')
parser.add_argument('path')
parser.add_argument('-dt', '--delayTime', type=float, default=2.5)
parser.add_argument('-i', '--interval', type=float, default=0.0125)
args = parser.parse_args()

if args.delayTime < 0:
    print('Error: Delay time cannot be a negative number!')
    exit()

if args.interval < 0:
    print('Error: Interval cannot be a negative number!')
    exit()

try:
    with open(args.path, 'r') as file:
        text = file.read()
        print('File successfully read!')

        if args.delayTime > 0:
            print(f'Waiting for {args.delayTime} seconds...')
            time.sleep(args.delayTime)

        print('Started typing...')
        start_time = time.time()
        
        auto.typewrite(text, interval=args.interval)
        elapsed_time = time.time() - start_time

except FileNotFoundError:
    print('Error: Input file not found!')
    exit()
except UnicodeDecodeError:
    print('Error: File must be text file!')
    exit()
    
print(f'Successfully finished in: {elapsed_time * 1000:.2f} ms')
