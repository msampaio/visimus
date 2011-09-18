from visimus import settings, utils


def google_cdn(request):
    return {'use_google_cdn': settings.USE_GOOGLE_CDN}


def amazon_cdn(request):
    return {'use_amazon_cdn': settings.USE_AMAZON_CDN}


def git_version(request):
    return {'git_version': utils.git_log()}


def production(request):
    return {'production': settings.PRODUCTION}