import hashlib
import sys

def main():
    try:
        argm = sys.argv[1]
    except:
        print("Error argument!")
        exit(0)
    
    print("\t██╗  ██╗ █████╗ ███████╗██╗  ██╗████████╗ ██████╗  ██████╗ ██╗     ")
    print("\t██║  ██║██╔══██╗██╔════╝██║  ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     ")
    print("\t███████║███████║███████╗███████║   ██║   ██║   ██║██║   ██║██║     ")
    print("\t██╔══██║██╔══██║╚════██║██╔══██║   ██║   ██║   ██║██║   ██║██║     ")
    print("\t██║  ██║██║  ██║███████║██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗")
    print("\t╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝\n")
    choice = input("* 1)MD5\n* 2)SHA1\n* 3)SHA256\n* 4)SHA512\n:")

    if choice == "1":
        res = hashlib.md5(str(argm).encode("ascii")).hexdigest()
        print("Hash -> {}".format(res))
    elif choice == "2":
        res = hashlib.sha1(str(argm).encode("ascii")).hexdigest()
        print("Hash -> {}".format(res))
    elif choice == "3":
        res = hashlib.sha256(str(argm).encode("ascii")).hexdigest()
        print("Hash -> {}".format(res))
    elif choice == "4":  
        res = hashlib.sha512(str(argm).encode("ascii")).hexdigest()
        print("Hash -> {}".format(res))
    else:
        print("Error choice!")
        exit(0)

    
if __name__ == "__main__":
    main()