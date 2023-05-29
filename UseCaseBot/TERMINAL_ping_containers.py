import subprocess
import platform

# Docker container names and their IPs
ips = {
    'container1': '172.17.0.2',
    'container2': '172.17.0.3',
    'container3': '172.17.0.4',
}

def ping(src_container: str, dest_ip: str) -> bool:
    """
    Returns True if host (str) responds to a ping request from the given Docker container.
    """
    command = ['docker', 'exec', '-it', src_container, 'ping', '-c', '1', dest_ip]

    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

for container in ips.keys():
    for ip in ips.values():
        if ips[container] != ip:  # Do not ping the container itself
            result = ping(container, ip)
            print(f"Ping from {container} to IP {ip} {'succeeded' if result else 'failed'}")

