export function formatDuration(seconds){ const m=Math.floor(seconds/60),s=seconds%60; return `${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`; }
