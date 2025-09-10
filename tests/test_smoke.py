def test_imports():
    import simple_factory.main as s
    import factory_method.main as fm
    import abstract_factory.main as af
    assert callable(s.main) and callable(fm.main) and callable(af.main)
