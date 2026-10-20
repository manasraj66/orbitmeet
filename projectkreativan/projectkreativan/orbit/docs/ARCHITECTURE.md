# Architecture

FastAPI serves the static frontend and REST endpoints. WebSockets carry room events and WebRTC signaling; media flows peer-to-peer where possible, with STUN/TURN configured for connectivity.
