import socket

def dns_lookup(query):
    try:
        # Try to interpret the input as an IP address
        socket.inet_aton(query)
        # Perform a reverse DNS lookup (IP to domain name)
        host_info = socket.gethostbyaddr(query)
        return host_info[0]  # Return the primary domain name
    except socket.error:
        try:
            # If it's not an IP, treat it as a domain name and perform DNS lookup
            return socket.gethostbyname(query)
        except socket.gaierror:
            return "Failed to resolve the domain name."

# Get user input
query = input("Enter a domain name or IP address: ")

# Perform the lookup and print the result
result = dns_lookup(query)

print(f"Result for {query}: {result}")
