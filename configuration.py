import toml
import socket
with open('configuration.toml') as f:
    config = toml.load(f)

discovery_hostname = socket.gethostname()
discovery_tag = f"Autodiscovered-{discovery_hostname}"
