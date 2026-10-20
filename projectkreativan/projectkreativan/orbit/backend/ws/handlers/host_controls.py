async def handle(message, context):
    if not context.get('is_host'):
        raise PermissionError('Host privileges required')
    await context['broadcast'](message)
