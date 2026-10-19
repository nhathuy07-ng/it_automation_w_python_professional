import psutil

def main():
    print(psutil.virtual_memory().free / 1024**3)

main()