export function addMessage(list,message){list.push({...message,receivedAt:Date.now()});return list}
