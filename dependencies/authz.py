from typing import Annotated, Any
from fastapi import Depends, HTTPException, status
from dependencies.authn import authenticated_user



# Permission = [
#    {"role":"admin",
#     "Permission": ['post_event','get_event', 'delete_event', 'update_event', 'view_event']
#     },
#    {"role":"host",
#     "Permission": ['post_event','get_event', 'update_event', 'put_event']
#     },
#    {"role":"guest",
#     "Permission": ['get_event', 'put_event']
#     }
# ]


# def has_permissions(permissions):

# getting the user role from the authenticated user
def has_roles(roles):
    def check_roles(user: Annotated[Any, Depends(authenticated_user)]):
        if user["role"] not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied"
            )
    return check_roles

