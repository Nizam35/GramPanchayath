from django.core.exceptions import ValidationError
from django.utils import six
from django.utils.translation import ugettext_lazy as _

# from confusable_homoglyphs import confusables

CONFUSABLE_EMAIL = _(u"This email address cannot be registered. "
                     "Please supply a different email address.")
DUPLICATE_EMAIL = _(u"This email address is already in use. "
                    u"Please supply a different email address.")



def validate_confusables_email(value):
    """
    Validator which disallows 'dangerous' email addresses likely to
    represent homograph attacks.
    An email address is 'dangerous' if either the local-part or the
    domain, considered on their own, are mixed-script and contain one
    or more characters appearing in the Unicode Visually Confusable
    Characters file.
    """
    if '@' not in value:
        return
    local_part, domain = value.split('@')
    if confusables.is_dangerous(local_part) or \
       confusables.is_dangerous(domain):
        raise ValidationError(CONFUSABLE_EMAIL, code='invalid')
