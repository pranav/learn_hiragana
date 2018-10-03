# coding=utf-8

import argparse
import random
import logging
import sys
logging.basicConfig(format='%(message)s', level=logging.INFO)


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


KANA = {
    'katakana': [
        ('ア', 'a'),
        ('イ', 'i'),
        ('ウ', 'u'),
        ('エ', 'e'),
        ('オ', 'o'),

        ('カ', 'ka'),
        ('キ', 'ki'),
        ('ク', 'ku'),
        ('ケ', 'ke'),
        ('コ', 'ko'),

        ('サ', 'sa'),
        ('シ', 'shi'),
        ('ス', 'su'),
        ('セ', 'se'),
        ('ソ', 'so'),

        ('タ', 'ta'),
        ('チ', 'chi'),
        ('ツ', 'tsu'),
        ('テ', 'te'),
        ('ト', 'to'),

        ('ナ', 'na'),
        ('ニ', 'ni'),
        ('ヌ', 'nu'),
        ('ネ', 'ne'),
        ('ノ', 'no'),

        ('ハ', 'ha'),
        ('ヒ', 'hi'),
        ('フ', 'fu'),
        ('ヘ', 'he'),
        ('ホ', 'ho'),

        ('マ', 'ma'),
        ('ミ', 'mi'),
        ('ム', 'mu'),
        ('メ', 'me'),
        ('モ', 'mo'),

        ('ヤ', 'ya'),
        ('ユ', 'yu'),
        ('ヨ', 'yo'),

        ('ラ', 'ra'),
        ('リ', 'ri'),
        ('ル', 'ru'),
        ('レ', 're'),
        ('ロ', 'ro'),

        ('ワ', 'wa'),
        ('ヲ', 'wo'),

        ('ン', 'n')
    ],
    'hiragana': [
        ('あ', 'a'),
        ('い', 'i'),
        ('う', 'u'),
        ('え', 'e'),
        ('お', 'o'),

        ('か', 'ka'),
        ('き', 'ki'),
        ('く', 'ku'),
        ('け', 'ke'),
        ('こ', 'ko'),

        ('さ', 'sa'),
        ('し', 'shi'),
        ('す', 'su'),
        ('せ', 'se'),
        ('そ', 'so'),

        ('た', 'ta'),
        ('ち', 'chi'),
        ('つ', 'tsu'),
        ('て', 'te'),
        ('と', 'to'),

        ('な', 'na'),
        ('に', 'ni'),
        ('ぬ', 'nu'),
        ('ね', 'ne'),
        ('の', 'no'),

        ('は', 'ha'),
        ('ひ', 'hi'),
        ('ふ', 'fu'),
        ('へ', 'he'),
        ('ほ', 'ho'),

        ('ま', 'ma'),
        ('み', 'mi'),
        ('む', 'mu'),
        ('め', 'me'),
        ('も', 'mo'),

        ('や', 'ya'),
        ('ゆ', 'yu'),
        ('よ', 'yo'),

        ('ら', 'ra'),
        ('り', 'ri'),
        ('る', 'ru'),
        ('れ', 're'),
        ('ろ', 'ro'),

        ('わ', 'wa'),
        ('を', 'wo'),

        ('ん', 'n'),

        ('が', 'ga'),
        ('ぎ', 'gi'),
        ('ぐ', 'gu'),
        ('げ', 'ge'),
        ('ご', 'go'),

        ('ざ', 'za'),
        ('じ', 'ji'),
        ('ず', 'zu'),
        ('ぜ', 'ze'),
        ('ぞ', 'zo'),

        ('だ', 'da'),
        ('づ', 'zu'),
        ('で', 'de'),
        ('ど', 'do'),

        ('ば', 'ba'),
        ('び', 'bi'),
        ('ぶ', 'bu'),
        ('べ', 'be'),
        ('ぼ', 'bo'),


        ('ぱ', 'pa'),
        ('ぴ', 'pi'),
        ('ぷ', 'pu'),
        ('ぺ', 'pe'),
        ('ぽ', 'po')
    ]
}


def get_kana(kana, starting, ending):
    filtered_list = []
    found_starting = False
    found_ending = False
    global KANA
    for kana_item in KANA[kana]:
        if found_starting and found_ending:
            break
        if kana_item[1] == starting:
            found_starting = True
        if kana_item[1] == ending:
            found_ending = True
        if found_starting or found_ending:
            filtered_list.append(kana_item)
    return filtered_list


def ok(str):
    logging.info(Colors.OKGREEN + str + Colors.ENDC)


def fail(str):
    logging.fatal(Colors.FAIL + str + Colors.ENDC)


def warn(str):
    logging.warn(Colors.WARNING + str + Colors.ENDC)


def trial(choice):
    """
    Query the user for the hiragana tuple correctness.
    :type choice: tuple
    :return bool
    """
    hiragana = raw_input("Please enter " + choice[0] + ": ")
    return hiragana == choice[0]


def log_current_trial_info(successful_trials, failed_trials):
    """
    :type successful_trials: list
    :type failed_trials: list
    """
    total_trials = len(successful_trials) + len(failed_trials)
    logging.info("%s/%s correct. %d%%" % (len(successful_trials), total_trials, int(len(successful_trials)*100/total_trials)))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("kana")
    parser.add_argument("--starting", default="a", required=False, dest="starting", help="Hiragana to start with")
    parser.add_argument("--ending", default="po", required=False, dest="ending", help="Hiragana to end with")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.kana not in ['hiragana', 'katakana']:
        logging.error("Must choose one of hiragana or katakana!")

    logging.info("LEARN KANA!")
    successful_trials = []
    failed_trials = []
    kana_list = get_kana(args.kana, args.starting, args.ending)
    try:
        logging.info("Please enter in the matching hiragana.")
        while True:
            logging.info(" ")
            choice = random.choice(kana_list)
            if trial(choice):
                successful_trials.append(choice)
                ok("໒( ͡ᵔ ▾ ͡ᵔ )७ Correct!")
            else:
                failed_trials.append(choice)
                fail("(ಥ﹏ಥ) Wrong! It was %s." % choice[1])

            log_current_trial_info(successful_trials, failed_trials)
    except KeyboardInterrupt:
        warn("Goodbye!")
        logging.info("You should learn these hiragana more!")
        [warn("%s - %s" % choice) for choice in set(failed_trials)]
        sys.exit(0)


if __name__ == '__main__':
    main()
