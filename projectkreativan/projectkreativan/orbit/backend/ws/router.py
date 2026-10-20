async def dispatch(message, context):
    kind = message.get('type')
    handler = context.get('handlers', {}).get(kind)
    if handler: await handler(message, context)
