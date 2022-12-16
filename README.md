
# ABTesting_EpsilonGreedy



### A/b Testing: Multi-Armed Bandit Problem.
In marketing terms, a multi-armed bandit solution is a 'smarter' or more complex version of A/B testing that uses various algorithms to dynamically allocate traffic to variations that are performing well while allocating less traffic to underperforming variations.
The term "multi-armed bandit" comes from a hypothetical experiment where a person must choose between multiple actions, each with an unknown payout. The goal is to determine the best or most profitable outcome through a series of choices. At the beginning of the experiment, when odds and payouts are unknown, the gambler must determine which machine to pull, in which order and how many times. This is the "multi-armed bandit problem."

### Multi-Armed Bandit Example
One real-world example of a multi-armed bandit problem is when a news website has to make a decision about which ads to display to its visitors. In this case, they want to maximize advertising revenue, but they may be lacking enough information about the visitor to pursue a specific advertising strategy. They typically have a large number of ads from which to choose, and they want to know which ads will drive maximum revenue for their news site. The website needs to make a series of decisions, each with unknown outcome and 'payout.'

### Epsilon-Greedy Algorithm
There are many different solutions developed to tackle the multi-armed bandit problem. One of the most commonly used solutions is the Epsilon-greedy algorithm. This is an algorithm for continuously balancing exploration with exploitation. (In 'greedy' experiments, the lever with the highest known payout is always pulled except when a random action is taken). A randomly chosen arm is pulled a fraction ε of the time. The other 1-ε of the time, the arm with the highest known payout is pulled. In some versions of the algorithm, ε decreases over time, making it less probable to choose an arm at random. 



## ABTesting_EpsilonGreedy Package
ABTesting_EpsilonGreedy is a Python package for multi-armed bandit testing that uses the Epsilon Greedy algorithm. The package contains a function that performs the experiment and returns a dataframe that stores the reward and the cumulative average reward for each trial. The package also includes functions that display and visualize the results. 


### Installation
This package can be installed from https://test.pypi.org/project/ABTesting-EpsilonGreedy/0.1.0/. 



### Credits
This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
