import psutil

def main():
    print(str(round(psutil.virtual_memory().available / 1024**3, 2)) + " GB")

main()