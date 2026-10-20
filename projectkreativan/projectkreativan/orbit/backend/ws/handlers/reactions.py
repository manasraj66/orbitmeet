async def handle(message, context):
    await context['broadcast'](message)
