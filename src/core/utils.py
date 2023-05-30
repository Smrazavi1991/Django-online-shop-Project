from product.models import Category
from django.contrib.auth.models import Group
import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed, ParseError
from user.models import User


def categories_cascade_deactivation_check():
    all_categories = Category.objects.all()
    for category1 in all_categories:
        if category1.sub:
            category2_id = category1.sub.id
            category2 = Category.objects.get(id=category2_id)
            if category2.sub:
                category3_id = category2.sub.id
                category3 = Category.objects.get(id=category3_id)
                if category3.is_deleted is True or category3.is_active is False:
                    category2.is_active = False
                    category2.save()
            if category2.is_deleted is True or category2.is_active is False:
                category1.is_active = False
                category1.save()


def identify_user_role(user_id: int):
    list_of_roles = []
    user_roles = Group.objects.filter(user__id=user_id)
    if not user_roles:
        list_of_roles = None
    else:
        for user_role in user_roles:
            list_of_roles.append(user_role.name)
    return list_of_roles


def auth(self, request):
    # Extract the JWT from the Authorization header
    # jwt_token = request.META.get('HTTP_AUTHORIZATION')
    jwt_token = request.COOKIES.get("token", None)
    if jwt_token is None:
        return None

    # Decode the JWT and verify its signature
    try:
        payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.exceptions.InvalidSignatureError:
        raise AuthenticationFailed('Invalid signature')
    except:
        raise ParseError()

    # Get the user from the database
    username_ = payload.get('user_identifier')
    if username_ is None:
        raise AuthenticationFailed('User identifier not found in JWT')

    user = User.objects.filter(username=username_).first()
    if user is None:
        raise AuthenticationFailed('User not found')

    # Return the user and token payload
    return user, payload

