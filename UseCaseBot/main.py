import subprocess
from fastapi import FastAPI, HTTPException
from typing import Dict, Any

app = FastAPI()

# Docker container names and their IPs

# Need to encorporate somehow the "docker inspect containerX" command so
# I can give more information to the end user about the device they are 
# pinging such as "container 1: status: running, running: true, gateway, ip,
# mac address" 
ips = {
    'container1': '172.17.0.2',
    'container2': '172.17.0.3',
    'container3': '172.17.0.4',
}

def ping(src_container: str, dest_ip: str) -> Dict[str, Any]:
    """
    Returns {"result": True} if host (str) responds to a ping request from the given Docker container.
    Otherwise, return the error.
    """
    command = ['docker', 'exec', '-it', src_container, 'ping', '-c', '1', dest_ip]

    try:
        return {"result": subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0}
    except Exception as e:
        return {"error": str(e)}

@app.get("/ping", response_model=Dict[str, Any])
async def perform_ping():
    results = {}
    for container in ips.keys():
        for ip in ips.values():
            if ips[container] != ip:  # Do not ping the container itself
                result = ping(container, ip)
                if 'error' in result:
                    raise HTTPException(status_code=500, detail=result)
                results[f"From {container} to {ip}"] = 'succeeded' if result['result'] else 'failed'
    return results
