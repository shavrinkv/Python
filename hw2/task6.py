from typeguard import typechecked
@typechecked
def test(x: int) -> int:
    return x
print(test(10))
print(test("abcd"))