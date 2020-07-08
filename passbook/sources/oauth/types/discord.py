"""Discord OAuth Views"""
from typing import Any, Dict

from passbook.sources.oauth.models import OAuthSource, UserOAuthSourceConnection
from passbook.sources.oauth.types.manager import MANAGER, RequestKind
from passbook.sources.oauth.views.core import OAuthCallback, OAuthRedirect


@MANAGER.source(kind=RequestKind.redirect, name="Discord")
class DiscordOAuthRedirect(OAuthRedirect):
    """Discord OAuth2 Redirect"""

    def get_additional_parameters(self, source):
        return {
            "scope": "email identify",
        }


@MANAGER.source(kind=RequestKind.callback, name="Discord")
class DiscordOAuth2Callback(OAuthCallback):
    """Discord OAuth2 Callback"""

    def get_user_enroll_context(
        self,
        source: OAuthSource,
        access: UserOAuthSourceConnection,
        info: Dict[str, Any],
    ) -> Dict[str, Any]:
        return {
            "username": info.get("username"),
            "email": info.get("email", None),
            "name": info.get("username"),
        }
