import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <start> <end>")
    sys.exit(1)

start = int(sys.argv[1])
end = int(sys.argv[2])

for i in range(start, end + 1):
    if i % 2 != 0:
        print(i)
