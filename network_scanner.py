import subprocess
import os
from system_util import SystemUtil
from thread_job import ThreadJob

class NetworkScanner:
    # Instance constants
    ROUTER_IP = "192.168.1.1"
    NETWORKING_DEVICE = "?"
    ARP_COMMAND = ["arp", "-a"]
    PING_COMMAND = "ping -n 1 "
    ENCODING = "utf-8"
    BASE_IP = "192.168.1."

    device_activity = {
        "total": "Total devices found: ",
        "connected": "New devices connected, from previous scan: ",
        "same": "No network device activity observed",
        "disconnected": "Devices disconnected, from previous scan: "
    }

    # Instance data Prop
    prev_found_devices_len = None

    # Methods

    def __refresh_arp_list(self):
        print("Pinging network...\n")
        for i in range(2, 255):
            ip = self.BASE_IP + str(i)
            response = os.system(self.PING_COMMAND + ip)

            if response == 0:
                print("\n", ip, 'is up!')
            else:
                print("\n", ip, 'is down!')

        SystemUtil.clear_terminal()

    def __get_network_devices(self):
        print("Getting network devices...\n")
        stdout_result = subprocess.run(self.ARP_COMMAND, capture_output=True)
        bytes_list = stdout_result.stdout.splitlines()
        str_converted = [str(x, self.ENCODING) for x in bytes_list]
        filtered_result = [x.split(sep=" ")[0] for x in str_converted if self.ROUTER_IP not in x and x[0] != self.NETWORKING_DEVICE]
        return filtered_result



    def get_network_devices_output(self):
        self.__refresh_arp_list()
        filtered_result = self.__get_network_devices()
        total_devices_found = len(filtered_result)
        changed_devices = None if self.prev_found_devices_len is None else total_devices_found - self.prev_found_devices_len
        self.prev_found_devices_len = total_devices_found

        output = f"{self.device_activity['total']} {total_devices_found} \n"

        if changed_devices != None and changed_devices > 0:
            output += f"{self.device_activity['connected']} {changed_devices}\n"
        elif changed_devices != None and changed_devices == 0:
            output += f"{self.device_activity['same']}\n"
        elif changed_devices != None:
            output += f"{self.device_activity['disconnected']} {changed_devices}\n"

        for idx, device_name in enumerate(filtered_result):
            output += f"Device {idx}: {device_name}\n"

        output += "\n"    
        return output
