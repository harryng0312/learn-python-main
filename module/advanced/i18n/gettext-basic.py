import gettext


def print_some_strings() -> None:
    _ = gettext.gettext
    print(_("hello_world"))
    print(_("test_msg"))
    trans = gettext.translation(domain="gettext_basic", localedir="locale", languages=["en"])
    trans.install()
    print(trans.gettext("hello_world"))
    print(trans.gettext("test_msg"))
    return
    
# xgettext xgettext -d gettext_basic -o gettext_basic.pot module/advanced/i18n/gettext-basic.py

if __name__ == "__main__":
    print_some_strings()
    pass