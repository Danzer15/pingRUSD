import platform
import subprocess
import os
##
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
##
def get_target():
    while True:
        target = input("Target (example = google.com) : ").strip()
        
        if target and not target.isdigit():
            return target
        print("Pleasee, Fill with Target Name")
##
def packet_get_count():
    while True:
         packet_count = input("How Many Packet: ").strip()
         if packet_count.isdigit() and int(packet_count) > 0:
             return int(packet_count)
         print("Pleaseee, Fill With the Number of Packets")
##
def main():
    clear_screen()
    print("----------------")
    print("----pingRUSD----")
    print("----------------")

    target = get_target()
    count = packet_get_count()

    print("On Process Ladsss")

    # mententukan perintah berdasarkan OS user
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, str(count), target] 

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout
        error = result.stderr

        print(output)

        if result.returncode == 0:
            print("\nStatus : SUCCESS")
        else:
            print("\nStatus : FAILED")
            if error:
                print("Error:\n", error)

    except Exception as e:
        print("\nTerjadi Kesalahan: ", str(e))
        print("\nStatus: FAILED")

if __name__ == "__main__":
    main()
