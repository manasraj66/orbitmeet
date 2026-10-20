export function initials(name='Guest'){return name.trim().split(/\s+/).map(x=>x[0]).join('').slice(0,2).toUpperCase()}
export function avatarColor(name=''){let h=0;for(const c of name)h=(h*31+c.charCodeAt(0))|0;return `hsl(${Math.abs(h)%360} 65% 55%)`}
