def user_listing_path(instance,filename):
    return f'users_{0}/listings/{1}'.format(instance.seller.user.id,filename)