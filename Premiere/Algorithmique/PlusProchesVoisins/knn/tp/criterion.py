# [[file:../tp_hp_knn.org::*représentation des arbres][représentation des arbres:1]]
class Criterion:
    """
    criterion abstract class
    """
    def __init__(self, att: str, value: float):
        self._att = att
        self._value = value

    def accept(self, obj: dict) -> bool:
        """
        :return: (bool) True iff obj satisfied the criterion
        """
        pass

class EqualCriterion(Criterion):
    """
    criterion representing an equality
    """
    def accept(self, obj: dict) -> bool:
        """
        :return: (bool) True iff attribute is equal to value
        """
        return obj[self._att] == self._value

    def __str__(self):
        """
        :return: (str) string representation of object
        """
        return f"{self._att} == {self._value}"


class GreaterThanCriterion(Criterion):

    def accept(self, obj: dict) -> bool:
        return obj[self._att] > self._value

    def __str__(self):
        return f"{self._att} > {self._value}"


class LessThanCriterion(Criterion):
    def accept(self, obj: dict) -> bool:
        return obj[self._att] < self._value

    def __str__(self):
        return f"{self._att} < {self._value}"
# représentation des arbres:1 ends here
