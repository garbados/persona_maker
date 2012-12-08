import json
import operator

with open('data/user_data', 'r') as f:
    user_data = eval(f.read())

topics = {}
for user in user_data:
    try:
        user_topics = user['digitalFootprint']['topics']
    except KeyError:
        continue
    for topic in user_topics:
        topic = topic['value']
        try:
            topics[topic] += 1
        except KeyError:
            topics[topic] = 1

sorted_topics = sorted(topics.iteritems(), key=operator.itemgetter(1))
sorted_topics.reverse()

with open('data/parsed_data', 'w') as f:
    f.write(str(sorted_topics) + '\n')

print sorted_topics