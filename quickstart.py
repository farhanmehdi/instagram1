# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'vegan_expo'
insta_password = '0628862362expo'

comments = ['Nice shot!  ',
        'I love your profile!  ',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use  ?',
        'Love your posts  ',
        'Looks awesome  ',
        'Getting inspired by you  ',
        ':raised_hands: Yes!',
        'I can feel your passion   :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username, password=insta_password, headless_browser=False)

with smart_run(session):
  """ Activity flow """	
  #commenti in inglese	
  #session.set_comments(['Awesome', 'Really Cool', 'I like your stuff','Nice shot!  ','I love your profile!  ','Your feed is an inspiration :thumbsup:','Just incredible :open_mouth:','What camera did you use  ?','Love your posts  ', 'Looks awesome  ','Getting inspired by you  ',':raised_hands: Yes!','I can feel your passion   :muscle:'])


  session.set_do_comment(enabled=True, percentage=50)
  session.set_comments(['Awesome', 'Really Cool', 'I like your stuff' ])
  # general settings		
  #session.set_dont_include(["deniseluzii", "friend2", "friend3"])		
  
  # activity		
  session.like_by_tags(["vegan","diet" ], amount=50)
  session.like_by_tags(['vegan','diet'], amount=50, interact=True)
  #session.follow_by_tags(['vegan'], amount=100)
  
  #session.set_comments(comments)
  #session.join_pods(topic='sports', engagement_mode='no_comments')

  #following
  #session.set_do_follow(enabled=True, percentage=50)
  session.set_smart_hashtags(['vegan', 'diet'], limit=3, sort='top', log_tags=True)
  #session.like_by_tags(amount=50, use_smart_hashtags=True)
  
