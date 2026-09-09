
import time
import pyfiglet
from random import randint, choice

def print_ascii_banner():
    """طباعة عنوان Happy Birthday بخط عشوائي."""
    fonts = ["slant", "doom", "alligator", "starwars", "banner3-D"]
    try:
        font = choice(fonts)
        art = pyfiglet.figlet_format("Happy Birthday", font=font)
        print("\n" + "=" * 80)
        print(art)
        print("=" * 80 + "\n")
    except:
        print("\n🎉🎂 HAPPY BIRTHDAY 🎂🎉\n")
        print("=" * 80 + "\n")


def print_name_frame(name):
    """طباعة إطار جميل حول اسم الشخص."""
    line = f"🎉  عيد ميلاد سعيد يا {name}!  🎉"
    border = "─" * len(line)
    print(border)
    print(line)
    print(border + "\n")


def celebration_effects(name):
    """تأثيرات حركية ورموز ورسائل تهنئة."""
    emojis = ["🎂", "🎈", "🎁", "✨", "🥳", "🌟", "🎉"]
    messages = [
        f"🎉 كل سنة وانت طيب يا {name}!",
        "✨ نتمنى لك يوماً رائعاً مليئاً بالسعادة!",
        f"🎁 ألف مبروك عيد ميلادك يا {name}!",
        "🌟 أتمنى لك سنة جديدة كلها نجاح!",
        "🥳 يوم سعيد عليك دايماً!"
    ]

    for i in range(20):
        spaces = " " * randint(1, 40)

        if i % 4 == 0 and messages:
            msg = messages.pop(0)
            print(spaces + msg)
        else:
            print(spaces + choice(emojis))

        time.sleep(0.12)


def birthday_celebration():
    """الدالة الرئيسية لبرنامج تهنئة عيد ميلاد."""
    name = input("🎉 من هو صاحب عيد الميلاد؟ ")

    print_ascii_banner()
    print_name_frame(name)
    celebration_effects(name)

    print("\n" + "~" * 80)
    print(f"🥳 {name}, أتمنى لك أجمل عيد ميلاد على الإطلاق! 🎁")
    print("~" * 80 + "\n")


# تشغيل البرنامج
if __name__ == "_main_":
    birthday_celebration()