from collections import deque

suggested_links = deque(map(int,input().split()))
featured_articles = list(map(int,input().split()))

target = int(input())

final_feed = []

while suggested_links and featured_articles:
    current_suggested = suggested_links.popleft()
    current_featured = suggested_links.pop()

    if current_suggested == current_featured:
        final_feed.append(0)
    
    elif current_featured > current_suggested:
        remainder = current_featured % current_featured
        final_feed.append(remainder)
        if remainder != 0:
            featured_articles.append(remainder * 2)
    else:
        remainder = current_suggested % current_featured
        final_feed.append(-remainder)
        if remainder != 0:
            suggested_links.append(remainder * 2)

total_engagement_value = sum(final_feed)

print(f'Final Feed: {", ".join(map(str,final_feed))}')

if total_engagement_value >= target:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    print(f"Goal not achieved! Short by: {target - total_engagement_value}")