export async function getMedia(){ return navigator.mediaDevices.getUserMedia({audio:true,video:true}); }
export async function listDevices(){ return navigator.mediaDevices.enumerateDevices(); }
