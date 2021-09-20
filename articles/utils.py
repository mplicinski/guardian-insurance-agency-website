from random import randint
from django.utils.text import slugify

def slugify_instance_title(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__ # this makes it general purpose
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        # auto genereate new slug
        # slug = f"{slug}-{qs.count() +1}" #if slug exists take the current count of slugs with the same name and add that count to the slug #nevermind this suck 
        rand_int = randint(100_000, 25_000_000) # maybe add random chars too
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance, save=save, new_slug=slug) # recursion to keep checking through all slugs
    instance.slug = slug
    if save:
        instance.save()
    return instance