export function toast(message){ const el=document.createElement('div'); el.className='toast'; el.textContent=message; document.body.append(el); setTimeout(()=>el.remove(),3000); }
export function floatReaction(emoji){ const el=document.createElement('span'); el.className='float-emoji'; el.textContent=emoji; document.body.append(el); setTimeout(()=>el.remove(),1400); }
