import sys


class User:
    def __init__(self):
        self._name = None

    @property
    def name(self):
        return unmask(self._name)

    @name.setter
    def name(self, value):
        self._name = mask(value)


def shift(string, reverse=False):
    """Shift ord value of character within range."""

    new_string = []

    for char in string:
        try:
            value = ord(char)

            if value in range(ord('A'), ord('Z') + 1):
                min = ord('A')
                max = ord('Z')
            elif value in range(ord('a'), ord('z') + 1):
                min = ord('a')
                max = ord('z')

            values = range(min, max + 1)

            if reverse:
                index = values.index(value) - 1
            else:
                index = values.index(value) + 1

            new_string.append(chr(values[index % len(values)]))

        except:
            new_string.append(char)

    return ''.join(new_string)


def mask(value):
    return shift(value)

def unmask(value):
    return shift(value, True)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        value = ' '.join(sys.argv[1:])
        print(f'MASKING "{value}"')

        masked_value = shift(value)
        print(f'MASKED "{masked_value}"')

        unmasked_value = shift(masked_value, True)
        print(f'UNMASKED "{unmasked_value}"')

    else:
        value = input('enter a name: ')
        user = User()
        user.name = value

        print(f'user.name => {user.name}')
        print(f'user._name => {user._name}')