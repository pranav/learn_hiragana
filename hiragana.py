# coding=utf-8

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

HIRAGANA = [
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

    ('が', 'ga'),
    ('ぎ', 'gi'),
    ('ぐ', 'gu'),
    ('げ', 'ge'),
    ('ご', 'go'),

    ('さ', 'sa'),
    ('し', 'shi'),
    ('す', 'su'),
    ('せ', 'se'),
    ('そ', 'so'),


    ('ざ', 'za'),
    ('じ', 'ji'),
    ('ず', 'zu'),
    ('ぜ', 'ze'),
    ('ぞ', 'zo'),

    ('た', 'ta'),
    ('ち', 'chi'),
    ('つ', 'tsu'),
    ('て', 'te'),
    ('と', 'to'),

    ('だ', 'da'),
    ('づ', 'zu'),
    ('で', 'de'),
    ('ど', 'do'),

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

    ('ば', 'ba'),
    ('び', 'bi'),
    ('ぶ', 'bu'),
    ('べ', 'be'),
    ('ぼ', 'bo'),

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

    ('ぱ', 'pa'),
    ('ぴ', 'pi'),
    ('ぷ', 'pu'),
    ('ぺ', 'pe'),
    ('ぽ', 'po')
]


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


def main():
    logging.info("LEARN HIRAGANA!")
    max_hiragana = int(raw_input("How many hiragana would you like to learn?: "))
    successful_trials = []
    failed_trials = []

    try:
        logging.info("Please enter in the matching hiragana.")
        while True:
            logging.info(" ")
            choice = random.choice(HIRAGANA[0:max_hiragana])
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
