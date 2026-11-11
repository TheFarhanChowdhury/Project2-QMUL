import pytest
from datetime import datetime, timedelta
from MarketTracker import MarketTracker

def generate_prices(start, count, base_price):
    return [(start + timedelta(days=i), base_price + i) for i in range(count)]

def test_empty_markettracker():
    mt = MarketTracker()
    start = datetime(2025, 4, 1)
    end = datetime(2025, 4, 10)
    with pytest.raises(KeyError):
        mt.get_price_data("TSLA", start, end)

def test_single_asset_add_and_get():
    mt = MarketTracker()
    asset = "AAPL"
    start = datetime(2025, 4, 1)
    times = [start + timedelta(days=i) for i in range(5)]
    prices = [100 + i for i in range(5)]

    for t, p in zip(times, prices):
        mt.add_price(asset, t, p)

    data = mt.get_price_data(asset, start, start + timedelta(days=4))
    assert len(data) == 5
    for (time, (price, minp, maxp, avgp)), expected_price in zip(data, prices):
        assert price == expected_price
        assert minp <= price <= maxp
        assert minp == min(prices[:prices.index(price)+1])
        assert maxp == max(prices[:prices.index(price)+1])
        assert round(avgp, 5) == round(sum(prices[:prices.index(price)+1])/len(prices[:prices.index(price)+1]), 5)

def test_multiple_assets():
    mt = MarketTracker()
    start = datetime(2025, 4, 1)

    assets = {
        "GOOG": generate_prices(start, 3, 200),
        "NVDA": generate_prices(start, 4, 300),
        "TSLA": generate_prices(start, 5, 400),
    }

    for name, price_data in assets.items():
        for time, price in price_data:
            mt.add_price(name, time, price)

    for name, price_data in assets.items():
        result = mt.get_price_data(name, price_data[0][0], price_data[-1][0])
        assert len(result) == len(price_data)
        for (time, (price, _, _, _)), (expected_time, expected_price) in zip(result, price_data):
            assert time == expected_time
            assert price == expected_price

def test_missing_asset_raises_keyerror():
    mt = MarketTracker()
    with pytest.raises(KeyError):
        mt.get_price_data("NONEXISTENT", datetime(2025, 1, 1), datetime(2025, 2, 1))


def test_get_price_data_stats():
    mt = MarketTracker()
    asset = "META"
    base_date = datetime(2025, 3, 20)

    # Add prices every day for 15 days with controlled prices
    prices = [
        (base_date + timedelta(days=i), float(i)) for i in range(15)
    ]  # Prices from 0.0 to 14.0

    for t, p in prices:
        mt.add_price(asset, t, p)

    # Query a date range that only includes the last 5 days
    start = base_date + timedelta(days=10)
    end = base_date + timedelta(days=14)

    data = mt.get_price_data(asset, start, end)

    assert len(data) == 5

    for i, (time, (price, minp, maxp, avgp)) in enumerate(data):
        index = i + 10  # Corresponds to price[i+10]
        window_start_index = max(0, index - 10)
        window_prices = [p for (_, p) in prices[window_start_index:index + 1]]
        assert price == prices[index][1]
        assert minp == min(window_prices)
        assert maxp == max(window_prices)
        assert round(avgp, 5) == round(sum(window_prices) / len(window_prices), 5)
