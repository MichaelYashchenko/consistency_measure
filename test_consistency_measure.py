from consistency_measure import DistanceBetweenSupremumAndInfimum as dbsi

class TestTwoBars:
    def test_1(self):
        sup = [1., 1.]
        inf = [1., 0.5]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 1

    def test_2(self):
        sup = [1., 1.]
        inf = [1., 0.]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 2

    def test_3(self):
        sup = [1., 1.]
        inf = [0., 0.0]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 3

    def test_4(self):
        sup = [1., 0.5]
        inf = [1., 0.]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 1

    def test_5(self):
        sup = [1., 0.5]
        inf = [0., 0.]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 2

    def test_6(self):
        sup = [1., 0.]
        inf = [0., 0.]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 1

class TestThreeBars:
    def test_1(self):
        sup = [1., 1., 1.]
        inf = [1., 0., 0.5]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 3

    def test_2(self):
        sup = [0.5, 1., 0.5]
        inf = [0., 1., 0]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 3

    def test_3(self):
        sup = [1., 1., 1.]
        inf = [0., 0., 1]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 4

    def test_4(self):
        sup = [1., 0.5, 1.]
        inf = [1., 0., 0]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 3

    def test_5(self):
        sup = [0.5, 1., 1.]
        inf = [0., 0.5, 1]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 2

    def test_6(self):
        sup = [0.5, 0, 1.]
        inf = [0, 0, 1]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 1

    def test_7(self):
        sup = [1., 1., 1.]
        inf = [1., 1., 0]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 2

    def test_8(self):
        sup = [1., 1., 0.5]
        inf = [0.5, 1., 0]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 2

    def test_9(self):
        sup = [1., 0.5, 1.]
        inf = [1., 0., 0.5]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 2

    def test_10(self):
        sup = [0.5, 1., 0.5]
        inf = [0., 1., 0.5]
        cs = dbsi(sup, inf)
        assert cs.get_counter() == 2

