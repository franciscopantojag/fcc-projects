from copy import deepcopy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs: 'int') -> None:
        items = kwargs.items()
        self.contents = [key for (key, value) in items for _ in range(value)]

    def draw(self, n_items: 'int'):
        n_items = min(n_items, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n_items)]


def experiment(hat: 'Hat', expected_balls: 'dict[str, int]', num_balls_drawn: 'int', num_experiments: 'int'):
    acc = 0

    for _ in range(num_experiments):
        different_hat = deepcopy(hat)
        balls_drawn = different_hat.draw(num_balls_drawn)
        balls_request = sum([1 for (key, value) in expected_balls.items()
                             if balls_drawn.count(key) >= value])
        acc += 1 if balls_request == len(expected_balls) else 0

    return acc / num_experiments


test = Hat(red=3, blue=2)
print(test)
