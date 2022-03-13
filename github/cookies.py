def get_cookie(cookie: str, name: str) -> str:
    cookies = cookie.split(";")

    cookie_dict = {}
    for cookie in cookies:
        cookie = cookie.strip()
        equals_idx = cookie.find("=")
        k, v = cookie[:equals_idx], cookie[equals_idx+1:]
        cookie_dict[k] = v

    return cookie_dict[name]


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert get_cookie('theme=light; sessionToken=abc123', 'theme') == 'light', 'theme=light'
    assert get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo') == 'true', 'ffo=true'
    print("Looks like you know everything. It is time for 'Check'!")
