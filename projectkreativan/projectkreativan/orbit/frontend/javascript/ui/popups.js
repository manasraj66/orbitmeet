export function confirmJoin(name,onAccept,onDeny){const ok=window.confirm(`Admit ${name}?`);(ok?onAccept:onDeny)?.()}
