#!/usr/bin/env python3

def filter_strings(input_list):
    """Returns a collection of unique strings starting with `TRG_`."""
    pass


if __name__ == '__main__':

    strings_to_filter = [
        "TRG_2482154ff",
        "GRT-ndfs8fng",
        "nnjdkfdnrnggfgnrunfg93",
        "TRG_",
        "",
        "TRG_2482154ff",
        "TRG_2482154ff",
        "TRG_3482154fbnfur",
        "fdnjrnfg_TRG_fbnjn5455",
    ]

    print(filter_strings(strings_to_filter))
