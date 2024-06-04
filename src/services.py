from typing import Any, Dict, List

import tweepy

from src.connection import trends_collection
from src.constants import BRAZIL_WOE_ID
from src.secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET


def _get_trends(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]:
    """Get treending topics from Twitter API.

    Args:
        woe_id (int): Identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    trends = api.trends_place(woe_id)

    return trends[0]["trends"]


def get_trends() -> List[Dict[str, Any]]:
    """Get treending topics persisted in MongoDB.

    Args:
        woe_id (int): Identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    trends = trends_collection.find({})
    return list(trends)


def save_trends() -> None:
    """Get trends topics and save on MongoDB."""
    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = _get_trends(woe_id=BRAZIL_WOE_ID, api=api)
    trends_collection.insert_many(trends)


def display_trends(trends: List[Dict[str, Any]]) -> None:
    """Display trends in a user-friendly manner.

    Args:
        trends (List[Dict[str, Any]]): List of trends to display.
    """
    for trend in trends:
        name = trend.get("name")
        tweet_volume = trend.get("tweet_volume")
        print(f"Trend: {name}")
        if tweet_volume:
            print(f"Tweet Volume: {tweet_volume}")
        else:
            print("Tweet Volume: Not available")
        print("-" * 40)