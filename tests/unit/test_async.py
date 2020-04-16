import aiohttp
import pytest


@pytest.mark.asyncio
async def test_get(url, event_loop):
    """Simple async http get request to httpbin
    :param url : fixture which return url
    :param event_loop : default loop from pytest-asycio, design as fixture
    """
    async with aiohttp.ClientSession(loop=event_loop) as session:
        async with session.get(url) as response:
            try:
                res = await response.json()
                status = response.status
            except Exception as e:
                pytest.raises(e)
            finally:
                assert res["url"] == url
                assert status == 200
