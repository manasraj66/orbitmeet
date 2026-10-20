import { ICE_SERVERS } from '../config.js';
export function createPeerConnection(){ return new RTCPeerConnection({iceServers:ICE_SERVERS}); }
