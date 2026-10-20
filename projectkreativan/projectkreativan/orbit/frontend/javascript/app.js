import { createMeeting, joinMeeting } from './core/socket.js';
const status = document.querySelector('#status');
const createButton = document.querySelector('#create');
const joinButton = document.querySelector('#join');
function openRoom(roomId, hostToken='') { window.location.href = `/static/html/meeting.html?room=${encodeURIComponent(roomId)}${hostToken ? `&host=${encodeURIComponent(hostToken)}` : ''}`; }
createButton.addEventListener('click', async () => {
  createButton.disabled = true; status.textContent = 'Creating your meeting...';
  try { const result = await createMeeting(); if (!result.room_id) throw new Error('The server did not return a meeting code.'); openRoom(result.room_id, result.host_token); }
  catch (e) { status.textContent = `Could not create meeting: ${e.message}`; }
  finally { createButton.disabled = false; }
});
joinButton.addEventListener('click', async () => {
  const code = document.querySelector('#code').value.trim();
  if (!code) { status.textContent = 'Please enter a meeting code.'; return; }
  joinButton.disabled = true; status.textContent = 'Joining your meeting...';
  try { const result = await joinMeeting(code); if (!result.room_id || !result.request_id) throw new Error('The server did not return a join request.'); status.textContent = 'Request sent. Waiting for host approval…'; let state='pending'; while(state==='pending'){ await new Promise(r=>setTimeout(r,350)); const check=await fetch(`/api/join-status/${encodeURIComponent(result.room_id)}/${encodeURIComponent(result.request_id)}`); if(!check.ok) throw new Error((await check.json()).detail || 'Could not check approval status'); state=(await check.json()).status; } if(state==='denied') throw new Error('Host denied your request.'); openRoom(result.room_id); }
  catch (e) { status.textContent = `Could not join meeting: ${e.message}`; }
  finally { joinButton.disabled = false; }
});

const historyBox = document.querySelector('#meeting-history');
if (historyBox) { fetch('/api/history').then(r=>r.json()).then(data=>{ const items=data.meetings||[]; historyBox.innerHTML = items.length ? items.map(m=>`<article class="history-item"><strong>${m.room_id}</strong><span>${new Date(m.created_at).toLocaleString()}</span><small>${m.status}</small></article>`).join('') : '<p>No meetings yet. Your created meetings will appear here.</p>'; }).catch(()=>historyBox.textContent='Meeting history is currently unavailable.'); }
