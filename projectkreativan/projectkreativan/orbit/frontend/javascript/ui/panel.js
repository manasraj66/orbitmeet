export function openPanel(name){document.dispatchEvent(new CustomEvent('orbit:panel',{detail:{name}}))}
