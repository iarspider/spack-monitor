__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "Apache-2.0 OR MIT"

from django.contrib.sites.shortcuts import get_current_site
from spackmon import settings


def globals(request):
    """Returns a dict of defaults to be used by templates, if configured
    correcty in the settings.py file."""
    return {
        "DOMAIN": settings.DOMAIN_NAME,
        "TWITTER_USERNAME": settings.cfg.TWITTER_USERNAME,
        "GITHUB_REPOSITORY": settings.cfg.GITHUB_REPOSITORY,
        "GITHUB_DOCUMENTATION": settings.cfg.GITHUB_DOCUMENTATION,
        "SITE_NAME": get_current_site(request).name,
        "GOOGLE_ANALYTICS_ID": settings.cfg.GOOGLE_ANALYTICS_ID,
        "GOOGLE_ANALYTICS_SITE": settings.cfg.GOOGLE_ANALYTICS_SITE,
    }
