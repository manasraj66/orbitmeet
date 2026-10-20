export function createMicMeter(stream){ const ctx=new AudioContext(); const analyser=ctx.createAnalyser(); ctx.createMediaStreamSource(stream).connect(analyser); return {ctx,analyser}; }
