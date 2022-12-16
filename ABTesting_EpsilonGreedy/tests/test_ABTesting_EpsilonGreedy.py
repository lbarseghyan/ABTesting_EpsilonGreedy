#!/usr/bin/env python

"""Tests for `ABTesting_EpsilonGreedy` package."""

import pandas as pd
from ABTesting_EpsilonGreedy import ABTesting_EpsilonGreedy



def test_experiment():
    assert ABTesting_EpsilonGreedy.Bandit.experiment([1, 2, 3, 4], 2000, pd.read_csv('tests/Test_Data.csv'))
    assert ABTesting_EpsilonGreedy.Bandit.experiment([1, 2, 3], 500)


def test_experiment_results():
    experiment_output1 = ABTesting_EpsilonGreedy.Bandit.experiment([1, 2, 3, 4], 2000, pd.read_csv('tests/Test_Data.csv'))
    experiment_output2 = ABTesting_EpsilonGreedy.Bandit.experiment([1, 2, 3], 500)
    assert ABTesting_EpsilonGreedy.Bandit.experiment_results(experiment_output1) is None
    assert ABTesting_EpsilonGreedy.Bandit.experiment_results(experiment_output2) is None


def test_plot_average_reward():
    experiment_output1 = ABTesting_EpsilonGreedy.Bandit.experiment([1, 2, 3, 4], 2000, pd.read_csv('tests/Test_Data.csv'))
    experiment_output2 = ABTesting_EpsilonGreedy.Bandit.experiment([1, 2, 3], 500)
    assert ABTesting_EpsilonGreedy.Bandit.plot_average_reward(experiment_output1) is None
    assert ABTesting_EpsilonGreedy.Bandit.plot_average_reward(experiment_output2) is None

