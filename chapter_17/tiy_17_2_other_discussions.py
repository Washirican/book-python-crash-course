# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-11-26, File created.
# --------------------------------------------------------------------------- #
from operator import itemgetter

import requests
from plotly import offline


# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'author': response_dict['by'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        }
    # Handle news articles with no user comments (i.e. no descendants key)
    try:
        submission_dict['comments'] = response_dict['descendants']
    except KeyError:
        submission_dict['comments'] = 0

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

# for submission_dict in submission_dicts:
#     print(f"\nTitle: {submission_dict['title']}")
#     print(f"Discussion link: {submission_dict['hn_link']}")
#     print(f"Comments: {submission_dict['comments']}")

repo_links, comments, labels = [], [], []
for submission in submission_dicts:
    repo_link = f"<a href='{submission['hn_link']}'>{submission['title']}</a>"
    repo_links.append(repo_link)
    comments.append(submission['comments'])
    label = f"{submission['author']}<br />{submission['title']}"
    labels.append(label)

# Make visualization.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': comments,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Hacker News: Top 10 Stories',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'News Article',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Number of Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hacker_news_top_stories.html')
