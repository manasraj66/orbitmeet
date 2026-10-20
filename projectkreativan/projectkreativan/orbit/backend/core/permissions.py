def is_host(peer_id: str, host_id: str) -> bool:
    return bool(peer_id) and peer_id == host_id
