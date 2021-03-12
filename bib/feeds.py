from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from blog.models import Post


class LatestPostFeed(Feed):
    title = "Latest Posts"
    link = ""
    description = "Updates on changes."

    def items(self):
        return Post.objects.order_by('created')[:10]


class AtomLatestPostFeed(LatestPostFeed):
    feed_type = Atom1Feed
    subtitle = LatestPostFeed.description
