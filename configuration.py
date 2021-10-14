import toml
import socket
with open('configuration.toml') as f:
    config = toml.load(f)

discovery_hostname = socket.gethostname()
discovery_tag = f"Auto Discovered by host {discovery_hostname}"
