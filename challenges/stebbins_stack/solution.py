import itertools


def isSiStebbinsStack(deck):
    position = 1
    suite_order = {
        '1': 'C',
        '2': 'H',
        '3': 'S',
        '4': 'D'
    }
    face_card_value = {
        'A': 1,
        'J': 11,
        'Q': 12,
        'K': 13
    }

    def get_next_card(card):
        print('Given Card: {}'.format(card))
        first_card_value = card[:-1]
        first_card_suite = card[-1]

        if first_card_value in face_card_value:
            first_card_value = face_card_value[first_card_value]

        next_card_value = int(first_card_value) % 13 + 3
        if next_card_value > 13:
            next_card_value %= 13

        if next_card_value in face_card_value.values():
            for key, value in face_card_value.items():
                if next_card_value == value:
                    next_card_value = key
                    break

        for key, value in suite_order.items():
            if first_card_suite == value:
                next_card_suite = suite_order[str(int(key) % 4 + 1)]
                break

        next_card = '{}{}'.format(next_card_value, next_card_suite)
        print('Next Card: {}'.format(next_card))
        return next_card

    first_card = deck.pop(0)
    next_card = get_next_card(first_card)
    position = 1
    for count, card in enumerate(deck):
        print('Count: ', count)
        position += 1
        if card == next_card:
            next_card = get_next_card(card)
        else:
            return position
    return 1


if __name__ == "__main__":
    deck = input().split()
    print(isSiStebbinsStack(deck))
