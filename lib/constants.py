DAYS_OF_WEEK=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

'''
A row-column lookup table for channel mappings
{
    row: {
        column: channel,
        ...
    }
}
'''
DEFAULT_CHANNEL_MAPPINGS = {
    'B': {
        '2': 0,
        '4': 1,
        '6': 2,
        '8': 3,
        '10': 4,
        '12': 5,
        '14': 6,
    },
    'C': {
        '3': 7,
        '5': 8,
        '7': 9,
        '9': 10,
        '11': 11,
        '13': 12,
    },
    'D': {
        '2': 13,
        '4': 14,
        '6': 15,
        '8': 16,
        '10': 17,
        '12': 18,
        '14': 19,
    },
    'E': {
        '3': 20,
        '5': 21,
        '7': 22,
        '9': 23,
        '11': 24,
        '13': 25,
    }
}
