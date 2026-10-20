// Multiple STUN endpoints improve connectivity discovery; TURN is still needed on restrictive networks.
export const ICE_SERVERS = [
 { urls: 'stun:stun.l.google.com:19302' },
 { urls: 'stun:stun.cloudflare.com:3478' },
 { urls: 'stun:stun1.l.google.com:19302' }
];
export const AVATARS = ['#7c8cff','#42d6b3','#ffb86b','#ff7a90'];
