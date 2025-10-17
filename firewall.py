import random

def genarate_random_ip():
    return f"192.168.1.{random.randint(1, 20)}"

def check_rules(rules, ip):
    for ips, condition in rules.items():
        if ips == ip:
            return condition
        return "allow"
firewall_rules = {
    "192.168.1.1": "block",
    "192.168.1.4": "block",
    "192.168.1.9": "block",
    "192.168.1.13": "block",
    "192.168.1.16": "block",
    "192.168.1.19": "block"
}
    
for x in range(10):
    ip = genarate_random_ip()
    print(f"ip adress:{ip}, condition:{check_rules(firewall_rules, ip)}, token:{random.randint(1000, 9999)}")

    
