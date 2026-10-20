async def handle(message, context):
    await context['relay'](message)
