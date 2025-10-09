from collections import deque

suggested_links = deque(int(x) for x in input().split())
featured_articles = [int(x) for x in input().split()]

target_engagement_value =  int(input())
final_feed = []

while suggested_links and featured_articles:
    curr_suggestion = suggested_links.popleft()
    curr_article = featured_articles.pop()

    if curr_suggestion == curr_article:
        final_feed.append(0)
        continue


    divident = max(curr_suggestion,curr_article)
    devisor = min(curr_suggestion,curr_article)

    result = divident % devisor
    

    if divident == curr_article:
        final_feed.append(result)

        if result == 0:
            continue

        featured_articles.append(result*2)

    elif divident == curr_suggestion:
        final_feed.append(-result)

        if result == 0:
            continue

        suggested_links.append(result * 2)


eng_val = sum(final_feed)

print(f'Final Feed: {", ".join(str(x) for x in final_feed)}')
if eng_val - target_engagement_value >= 0:
    print(f'Goal achieved! Engagement Value: {eng_val}')
else:
     print(f'Goal not achieved! Short by: {target_engagement_value - eng_val}')