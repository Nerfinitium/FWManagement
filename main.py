import subprocess
import platform

class FirewallManager:
    def __init__(self):
        self.os_type = platform.system().lower()

    def list_rules(self):
        if self.os_type == "linux":
            subprocess.run(["iptables", "-L", "-n", "-v"])
        elif self.os_type == "windows":
            subprocess.run(["netsh", "advfirewall", "firewall", "show", "rule"])
        else:
            print("Unsupported operating system.")

    def allow_traffic(self, protocol, source_ip, destination_port):
        """Allow traffic based on specified parameters."""
        if self.os_type == "windows":
            subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule",
                            "name=AllowTraffic", "dir=in", "action=allow",
                            f"protocol={protocol}", f"localip={source_ip}", f"localport={destination_port}"])
        else:
            print("Unsupported operating system.")

    def block_traffic(self, protocol, source_ip, destination_port):
        if self.os_type == "windows":
            subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule",
                            "name=BlockTraffic", "dir=in", "action=block",
                            f"protocol={protocol}", f"localip={source_ip}", f"localport={destination_port}"])
        else:
            print("Unsupported operating system.")

    def clear_rules(self):
        if self.os_type == "windows":
            subprocess.run(["netsh", "advfirewall", "reset"])
        else:
            print("Unsupported operating system.")

if __name__ == "__main__":
    firewall_manager = FirewallManager()

    print("Current Firewall Rules:")
    firewall_manager.list_rules()

    firewall_manager.allow_traffic("tcp", "192.168.1.2", "22")

    print("\nUpdated Firewall Rules:")
    firewall_manager.list_rules()
