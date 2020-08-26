# this replaces the old hog_eval.py, which is kept around in case you want a local solution
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import hog

ENDPOINT = "https://hog-calc.apps.cs61a.org/api/compare_strategies"

STRATEGY_0 = hog.final_strategy
STRATEGY_1 = hog.always_roll(4)


def export(strategy):
    out = []
    for i in range(hog.GOAL_SCORE):
        out.append([])
        for j in range(hog.GOAL_SCORE):
            out[-1].append(strategy(i, j))
    return out


def main():
    token = OAuthSession().auth()
    data = {
        "strat0": json.dumps(export(STRATEGY_0)),
        "strat1": json.dumps(export(STRATEGY_1)),
        "token": token,
    }
    request = Request(ENDPOINT, bytes(urlencode(data), "utf-8"))
    body = json.loads(urlopen(request).read().decode())
    if body["success"]:
        print("Win rate: {}".format(body["win_rate"]))
    else:
        raise Exception(body["message"])

##################
# AUTHENTICATION #
################ #

"""
Bacon OK integration: mostly ported from OK Client
https://github.com/okpy/ok-client/blob/master/client/utils/auth.py
"""
import http.server
import json
import logging
import time
import webbrowser
from urllib.parse import parse_qsl, urlencode, urlparse
from urllib.request import Request, urlopen

log = logging.getLogger(__name__)

CLIENT_ID = "hog-calc"

# Don't worry, it is ok to share this
CLIENT_SECRET = "P0MeHIEDgrnTDIJ4sfOsH3rpIUQMoL0"

OAUTH_SCOPE = "email"

# Localhost
REDIRECT_HOST = "127.0.0.1"
REDIRECT_PORT = 6265

# OAuth post timeout
TIMEOUT = 10

# Server/API config
OK_SERVER_URL = "https://okpy.org"
INFO_ENDPOINT = "/api/v3/user/"
ASSIGNMENT_ENDPOINT = "/api/v3/assignment/"
AUTH_ENDPOINT = "/oauth/authorize"
TOKEN_ENDPOINT = "/oauth/token"
ERROR_ENDPOINT = "/oauth/errors"

# URL to redirect user to upon OAuth success
SUCCESS_ENDPOINT_URL = "https://okpy.org"  # temporary


class BaconOkException(Exception):
    """Base exception class for Bacon/OK integration."""


class OAuthException(BaconOkException):
    """ OAuth related exception """

    def __init__(self, error="", error_description=""):
        super().__init__()
        self.error = error
        self.error_description = error_description


def _pick_free_port(hostname=REDIRECT_HOST, port=0):
    """ Try to bind a port. Default=0 selects a free port. """
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((hostname, port))  # port=0 finds an open port
    except OSError as e:
        if port == 0:
            print("Unable to find an open port for authentication.")
            raise BaconOkException(e)
        else:
            return _pick_free_port(hostname, 0)
    addr, port = s.getsockname()
    s.close()
    return port


def _make_token_post(server, data):
    """Try getting an access token from the server. If successful, returns the
    JSON response. If unsuccessful, raises an OAuthException.
    """
    try:
        request = Request(server + TOKEN_ENDPOINT, bytes(urlencode(data), "utf-8"))
        body = json.loads(urlopen(request, timeout=TIMEOUT).read().decode())
    except Exception as e:
        log.warning("Other error when exchanging code", exc_info=True)
        raise OAuthException(error="Authentication Failed", error_description=str(e))
    if "error" in body:
        log.error(body)
        raise OAuthException(
            error=body.get("error", "Unknown Error"),
            error_description=body.get("error_description", ""),
        )
    return body


def _make_code_post(server, code, redirect_uri):
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_uri,
    }
    info = _make_token_post(server, data)
    return info["access_token"], int(info["expires_in"]), info["refresh_token"]


def _get_code():
    """ Make the requests to get OK access code """
    # email = input("Please enter your bCourses email: ")

    host_name = REDIRECT_HOST
    try:
        port_number = _pick_free_port(port=REDIRECT_PORT)
    except BaconOkException:
        # Could not bind to REDIRECT_HOST:0, try localhost instead
        host_name = "localhost"
        port_number = _pick_free_port(host_name, 0)

    redirect_uri = "http://{0}:{1}/".format(host_name, port_number)

    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": OAUTH_SCOPE,
    }
    url = "{}{}?{}".format(OK_SERVER_URL, AUTH_ENDPOINT, urlencode(params))
    assert webbrowser.open_new(url)
    return _get_code_via_browser(redirect_uri, host_name, port_number)


def _get_code_via_browser(redirect_uri, host_name, port_number):
    """ Get OK access code by opening User's browser """
    server = OK_SERVER_URL
    code_response = None
    oauth_exception = None

    class CodeHandler(http.server.BaseHTTPRequestHandler):
        def send_redirect(self, location):
            self.send_response(302)
            self.send_header("Location", location)
            self.end_headers()

        def send_failure(self, oauth_exception):
            params = {
                "error": oauth_exception.error,
                "error_description": oauth_exception.error_description,
            }
            url = "{}{}?{}".format(server, ERROR_ENDPOINT, urlencode(params))
            self.send_redirect(url)

        def do_GET(self):
            """Respond to the GET request made by the OAuth"""
            nonlocal code_response, oauth_exception
            log.debug("Received GET request for %s", self.path)
            path = urlparse(self.path)
            qs = {k: v for k, v in parse_qsl(path.query)}
            code = qs.get("code")
            if code:
                try:
                    code_response = _make_code_post(server, code, redirect_uri)
                except OAuthException as e:
                    oauth_exception = e
            else:
                oauth_exception = OAuthException(
                    error=qs.get("error", "Unknown Error"),
                    error_description=qs.get("error_description", ""),
                )

            if oauth_exception:
                self.send_failure(oauth_exception)
            else:
                self.send_redirect(SUCCESS_ENDPOINT_URL)

        def log_message(self, format, *args):
            return

    server_address = (host_name, port_number)
    print("Authentication server running on {}:{}".format(host_name, port_number))

    try:
        httpd = http.server.HTTPServer(server_address, CodeHandler)
        httpd.handle_request()
    except OSError as e:
        log.warning("HTTP Server Err {}".format(server_address), exc_info=True)
        raise

    if oauth_exception:
        raise oauth_exception
    return code_response


class OAuthSession:
    """ Represents OK OAuth state """

    def __init__(self, access_token="", refresh_token="", expires_at=-1, session=None):
        """ Create OK OAuth state with given tokens, and expiration """
        self.session = self.refresh_token = self.access_token = None
        self.expires_at = -1
        self.assignment = None
        if session is not None:
            config = session.config()
            self.session = session
            if "ok_access_token" in config:
                self.access_token = config["ok_access_token"]
            if "ok_refresh_token" in config:
                self.refresh_token = config["ok_refresh_token"]
            if "ok_expires_at" in config:
                self.expires_at = int(config["ok_expires_at"])
            if "ok_last_download_assignment" in config:
                self.assignment = config["ok_last_download_assignment"]
        elif access_token and refresh_token and expires_at >= 0:
            self.access_token = str(access_token)
            self.refresh_token = str(refresh_token)
            self.expires_at = expires_at

    def auth(self):
        """
        Returns OAuth access token which can be passed to the server
        for identification. If force_reauth is specified then will
        force re-authenticate the user; else tries to reuse or
        refresh previous token
        """

        # Perform OAuth
        try:
            self.access_token, expires_in, self.refresh_token = _get_code()
        except UnicodeDecodeError as e:
            with format.block("-"):
                print("Authentication error")
        except OAuthException as e:
            with format.block("-"):
                print("Authentication error: {}".format(e.error.replace("_", " ")))
                if e.error_description:
                    print(e.error_description)
        else:
            cur_time = int(time.time())
            self.expires_at = cur_time + expires_in
        return self.access_token

if __name__ == '__main__':
    main()