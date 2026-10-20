export function showScreen(id){ document.querySelectorAll('[data-screen]').forEach(x=>x.hidden=x.dataset.screen!==id); }
