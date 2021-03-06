"""
Running regret minimization for configs/example_config.json
"""

import json
import matplotlib.pyplot as plt
import numpy as np
import os

from logbexp.regret_routines import many_bandit_exps


def main():
    # get config
    config_file = 'example_config.json'
    config_path = os.path.join('configs', config_file)
    config = json.load(open(config_path, 'r'))

    # instantiate theta_star and S (S=||theta_star||+1)
    theta_star = (config["norm_theta_star"] / np.sqrt(config["dim"])) * np.ones(config["dim"])
    config["theta_star"] = theta_star
    config["param_norm_ub"] = config["norm_theta_star"] + 1

    # let's go
    mean_cum_regret = many_bandit_exps(config)
    plt.plot(np.arange(1, len(mean_cum_regret)+1), mean_cum_regret)
    plt.show()


if __name__ == '__main__':
    main()