async def send_all(peers, message):
    for peer in list(peers):
        await peer.send_json(message)
