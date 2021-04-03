from django import template

register = template.Library()


@register.simple_tag
def date(tr, td, *args, **kwargs):
    if tr == 0 and td == 0:
        return ''
    elif tr == 0 and td == 1:
        return ''
    elif tr == 0 and td > 1:
        return td - 1
    elif tr == 4 and td > 4:
        return ''
    else:
        return tr*7 + td - 1


@register.simple_tag
def attended(tr, td, *args, **kwargs):
    if tr == 0 and td == 0:
        return ''
    elif tr == 0 and td == 1:
        return ''
    elif tr == 0 and td > 1:
        return 'mark'
    elif tr == 4 and td > 4:
        return ''
    else:
        if tr*7 + td - 1 < 17:
            return 'mark'
        else:
            return 'mark'
