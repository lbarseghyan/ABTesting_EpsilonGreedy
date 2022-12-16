import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Bandit:
    """ 
    This class creates a Bandit object, which has its mean, mean estimate, and the number of trials.
    The class has methods to perform A/B testing with the Epsilon Greedy algorithm and display the results 
    with the help of a table and visualization.
    """

    def __init__(self, m, name):
        self.m = m
        self.name = name
        self.m_estimate = 0
        self.N = 0

    def __repr__(self):
        return self.name

    def pull(self, data=None, trial=None, bandits_index=None):
        """ Pull a reward from the data if given, otherwise simulate a new one.

        If the data is given returns the reward for the given trial and the bandit.
        If the data is not given returns a reward from the distribution with mean equal to the given bandit's mean

        Parameters
        ----------
        data : dataframe
             (Default value = None)
        trial : int
             (Default value = None)
        bandits_index : int
             (Default value = None)
             The index of the column in data for given bandit

        Returns
        -------
        float
             The reward for the given bandit
        """

        if data is None:
            return np.random.randn() + self.m
        else:
            return data.iloc[trial, bandits_index]

    def update(self, x):
        """ Update bandit's mean estimate and trial.

        Updates the mean estimate of the bandit based on the new reward and increases
        the number of trials for that bandit.

        Parameters
        ----------
        x : float
        This is a reward we get from a bandit
        """

        self.N += 1
        self.m_estimate = (1 - 1.0 / self.N) * self.m_estimate + 1.0 / self.N * x

    def experiment(bandit_means, num_trials, real_data=None):
        """ Run experiment on the bandit means.

        Uses Epsilon Greedy algorithm to calculate mean estimates of the bandits.

        Parameters
        ----------
        bandit_means : array-like
              List of the bandits' means

        num_trials : int
              Number of trials

        real_data : dataframe
             (Default value = None)
             Dataframe that has the rewards for each bandit and each trial

        Returns
        -------
        dictionary
             The dictionary has two keys and values. First key is the 'Bandits' and the value is a list of bandits.
             Each bandit in a list is an object from Bandit class and has its mean, estimated mean and the number of
             trials, that can be accessed. Second key is the 'Rewards_df' and the value is a dataframe, that stores the
             rewards and the cumulative average reward after each trial.
        """
        bandits = [Bandit(m, 'Bandit ' + str(i + 1)) for i, m in enumerate(bandit_means)]
        rewards = np.empty(num_trials)
        t = 10
        try:
            for i in range(num_trials):

                eps = 1 / t
                t += 0.1
                p = np.random.random()

                if p < eps:
                    j = np.random.randint(len(bandits))
                else:
                    j = np.argmax([b.m_estimate for b in bandits])

                x = bandits[j].pull(real_data, bandits[j].N - 1, j)
                bandits[j].update(x)
                rewards[i] = x

            cumulative_average = np.cumsum(rewards) / (np.arange(num_trials) + 1)
            rewards_df = pd.DataFrame({'Trial': list(range(1, num_trials + 1)),
                                       'Reward': rewards,
                                       'Cumulative Average': cumulative_average}).set_index('Trial')

            return {'Rewards_df': rewards_df, 'Bandits': bandits}

        except:                                                                                                          # noqa: E722
            print('Error: Not enough real data provided. ')
            print('Try again by providing more data or decrease the number of trials. ')

    def experiment_results(experiment_output):
        """ Display the results of experiment.


        Parameters
        ----------
        experiment_output : dictionary
              This is the output of the experiment() method from the Bandit class.
        """

        bandits = experiment_output['Bandits']
        rewards = experiment_output['Rewards_df']['Reward']
        avg_reward = rewards.sum() / len(rewards)
        avg_regret = np.max([b.m for b in bandits]) - avg_reward

        print()
        print('Results of the experiment')
        print()
        print('-------------------------------------------------')
        print("  Bandit  |  Mean  |  Estimated Mean  |  Trials  ")
        print('-------------------------------------------------')
        for b in bandits:
            print(f' {b.name} |   {b.m}    |       {round(b.m_estimate, 3)}      |  {b.N}  ')
        print('-------------------------------------------------')
        print("Average Reward: {}".format(round(avg_reward, 3)))
        print("Average Regret: {}".format(round(avg_regret, 3)))
        print('-------------------------------------------------')
        print('Bandit with highest mean estimate:  ' + str(bandits[np.argmax([b.m_estimate for b in bandits])]))
        print('Highest mean estimate:              ' + str(round(max([b.m_estimate for b in bandits]), 3)))
        print()

    def plot_average_reward(experiment_output):
        """ Visualize the cumulative average reward

        Parameters
        ----------
        experiment_output : dictionary
             This is the output of the experiment() method from the Bandit class.

        """
        plt.figure(figsize=(10, 5))
        cumulative_average = experiment_output['Rewards_df']['Cumulative Average']
        plt.plot(cumulative_average, color='royalblue')
        plt.title("Cumulative Average Reward ")
        plt.xlabel("Trial")
        plt.ylabel("Reward")
        plt.show()
