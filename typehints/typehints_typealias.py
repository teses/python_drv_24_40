

# Server
## Address
## ConnectionOptions
# Angaben von eigenen Typen mit Aliase
type Address = tuple[str,int]
type ConnectionOptions = dict[str, str]
type Server = tuple[Address, ConnectionOptions]

# Type Hints ohne Alias -> kompliziert, komplex
def broadcast_message(message: str, server: tuple[tuple[str,int],dict[str, str]]):
    pass

# mit Alias
def broadcast_message2(message: str, server: Server) -> None:
    print(f"Broadcasting {message} to {server}")

def broadcast_message_to_all_servers(message: str, servers: list[Server]) -> None:
    for s in servers:
        broadcast_message2(message, s)

############################################################################################
# Beispielvariable für einen Server:
serverData: Server = (
    ("127.0.0.1", 8080),               # Address
    {"protocol": "http", "timeout": "5"}  # ConnectionOptions
)
broadcast_message2("Hallo wie gehts", serverData)

############################################################################################
# Serverliste
serversData: list[Server] = [
    (("127.0.0.1", 8080), {"protocol": "http", "timeout": "5"}),
    (("192.168.1.10", 22), {"protocol": "ssh", "user": "admin"}),
    (("example.com", 443), {"protocol": "https", "retries": "3"}),
    (("10.0.0.5", 3306), {"protocol": "mysql", "user": "root", "password": "secret"}),
]
broadcast_message_to_all_servers("Hallo wie gehts", serversData)


