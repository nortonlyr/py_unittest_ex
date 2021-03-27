from pytest import fixture, mark


@fixture(scope="module")
def meta_fixture():
    print("\n*** begin meta_fixture***")
    yield
    print("\n*** end meta_fixture ***")


