def get_user_slug(instance):
    """
    Returns the slug for a user instance.
    """
    return f"{instance.email}"


def get_user_media_path_prefix(instance, filename):
    """
    Returns the path prefix for user media files.
    """
    return f"users/{instance.slug}/media/{filename}"
