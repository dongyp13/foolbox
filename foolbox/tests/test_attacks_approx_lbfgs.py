import numpy as np

from foolbox.attacks import ApproximateLBFGSAttack as Attack


def test_name():
    attack = Attack()
    assert 'Approx' in attack.name()


def test_attack(bn_adversarial):
    adv = bn_adversarial
    attack = Attack()
    attack(adv, verbose=True, maxiter=1, epsilon=1000)
    assert adv.get() is not None
    assert adv.best_distance().value() < np.inf


# def test_targeted_attack(bn_targeted_adversarial):
#     adv = bn_targeted_adversarial
#     attack = Attack()
#     attack(adv)
#     assert adv.get() is not None
#     assert adv.best_distance().value() < np.inf