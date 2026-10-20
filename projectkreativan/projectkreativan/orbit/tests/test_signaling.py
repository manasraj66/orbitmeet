def test_signaling_handler_is_async_callable():
    import inspect
    from backend.ws.handlers.signaling import handle
    assert inspect.iscoroutinefunction(handle)
