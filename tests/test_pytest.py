def test_hello(testdir):
    """Make sure that our plugin works."""

    # create a temporary pytest test file
    testdir.makepyfile(
        """
        import aiohttp
        import asyncio
        
        def test_aioresponses_works(aioresponse):
            loop = asyncio.get_event_loop()
            mocked.get('http://example.com', status=200, body='test')
            session = aiohttp.ClientSession()
            resp = loop.run_until_complete(session.get('http://example.com'))
        
            assert resp.status == 200
    """
    )

    # run all tests with pytest
    result = testdir.runpytest()

    # check that all 4 tests passed
    result.assert_outcomes(passed=1)
