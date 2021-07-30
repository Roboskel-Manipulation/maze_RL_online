import random

import numpy as np
from plot_utils.plot_utils import get_config, plot_learning_curve, plot_test_score, plot, plot_mean_sem
from maze3D_new.server import Server


def reward_function_timeout_penalty(goal_reached, timedout):
    # for every timestep -1
    # timed out -50
    # reach goal +100
    if goal_reached:
        return 100
    if timedout:
        return -50
    return -1


class ActionSpace:
    def __init__(self):
        self.actions = list(range(3))
        self.shape = 2
        self.actions_number = len(self.actions)
        self.high = self.actions[-1]
        self.low = self.actions[0]

    def sample(self):
        return np.random.randint(self.low, self.high + 1, 2)


class Maze3D:
    def __init__(self, config=None, config_file=None):
        self.config = get_config(config_file) if config_file is not None else config

        self.action_space = ActionSpace()
        self.fps = 60
        self.done = False

        self.server = Server()
        self.server.start()
        print("START!!!!")
        self.observation, _ = self.reset()
        self.observation_shape = (len(self.observation),)

    def reset(self):
        res = self.server.request('reset')
        return res['observation'], res['setting_up_duration']

    def step(self, action_agent, timed_out, goal, action_duration):
        """
        Performs the action of the agent to the environment for action_duration time.
        Simultaneously, receives input from the user via the keyboard arrows.

        :param action_agent: the action of the agent. gives -1 for down, 0 for nothing and 1 for up
        :param timed_out: Not used
        :param goal: Not used
        :param action_duration: the duration of the agent's action on the game
        :return: a transition [observation, reward, done, timeout, train_fps, duration_pause, action_list]
        """
        payload = {
            'action_agent': action_agent,
            'action_duration': action_duration,
            'timed_out': timed_out
        }
        try:
            res = self.server.request('step', payload)
        except Exception:
            # set connection status and recreate socket
            print("connection lost... reconnecting")
            self.server.close()
            self.server = Server()
            self.server.start()
            print("connection re-established")
            res = self.server.request('step', payload)

        self.observation = np.array(res['observation'])

        self.done = res['done']
        fps = res['fps']
        duration_pause = res['duration_pause']

        reward = reward_function_timeout_penalty(self.done, timed_out)

        return self.observation, reward, self.done, fps, duration_pause, []


if __name__ == '__main__':
    """Dummy execution"""
    while True:
        try:
            maze = Maze3D()
            while True:
                maze.step(random.randint(-1, 1), None, None, 200)
        except:
            maze.server.close()
            pass


def save_logs_and_plot(experiment, chkpt_dir, plot_dir, max_games):
    # score_history a list with the reward for each episode
    x = [i + 1 for i in range(len(experiment.score_history))]
    np.savetxt(chkpt_dir + '/scores.csv', np.asarray(experiment.score_history), delimiter=',')

    # action_history as returned by get_action_pair: a dyad agent and human {-1,0,1}
    actions = np.asarray(experiment.action_history)

    x_actions = [i + 1 for i in range(len(actions))]
    # Save logs in files
    np.savetxt(chkpt_dir + '/actions.csv', actions, delimiter=',')
    # np.savetxt('tmp/sac_' + timestamp + '/action_side.csv', action_side, delimiter=',')
    np.savetxt(chkpt_dir + '/epidode_durations.csv', np.asarray(experiment.game_duration_list), delimiter=',')

    np.savetxt(chkpt_dir + '/game_step_durations.csv', np.asarray(experiment.train_step_duration_list), delimiter=',')
    np.savetxt(chkpt_dir + '/online_update_durations.csv', np.asarray(experiment.online_update_durations),
               delimiter=',')
    np.savetxt(chkpt_dir + '/total_fps.csv', np.asarray(experiment.total_fps_list), delimiter=',')
    np.savetxt(chkpt_dir + '/train_fps.csv', np.asarray(experiment.train_fps_list), delimiter=',')
    np.savetxt(chkpt_dir + '/test_fps.csv', np.asarray(experiment.test_fps_list), delimiter=',')

    np.savetxt(chkpt_dir + '/distance_travel.csv', np.asarray(experiment.distance_travel_list), delimiter=',')
    np.savetxt(chkpt_dir + '/distance_travel_test.csv', np.asarray(experiment.test_distance_travel_list), delimiter=',')
    np.savetxt(chkpt_dir + '/pure_rewards.csv', experiment.reward_list, delimiter=',')
    np.savetxt(chkpt_dir + '/pure_rewards_test.csv', experiment.test_reward_list, delimiter=',')

    np.savetxt(chkpt_dir + '/grad_updates_durations.csv', experiment.grad_updates_durations, delimiter=',')

    # test_game_number logs
    np.savetxt(chkpt_dir + '/test_episode_duration_list.csv', experiment.test_game_duration_list, delimiter=',')
    np.savetxt(chkpt_dir + '/test_score_history.csv', experiment.test_score_history, delimiter=',')
    np.savetxt(chkpt_dir + '/test_length_list.csv', experiment.test_length_list, delimiter=',')

    # plot_learning_curve(x, experiment.score_history, plot_dir + "/train_scores.png")
    plot(experiment.length_list, plot_dir + "/train_length.png", x=[i + 1 for i in range(max_games)])
    plot(experiment.game_duration_list, plot_dir + "/train_game_durations.png", x=[i + 1 for i in range(max_games)])

    plot(experiment.train_step_duration_list, plot_dir + "/train_game_step_durations.png",
         x=[i + 1 for i in range(len(experiment.train_step_duration_list))])
    plot(experiment.test_step_duration_list, plot_dir + "/test_game_step_durations.png",
         x=[i + 1 for i in range(len(experiment.test_step_duration_list))])

    plot(experiment.online_update_durations, plot_dir + "/online_updates_durations.png",
         x=[i + 1 for i in range(len(experiment.online_update_durations))])
    plot(experiment.total_fps_list, plot_dir + "/total_fps.png",
         x=[i + 1 for i in range(len(experiment.total_fps_list))])
    plot(experiment.train_fps_list, plot_dir + "/train_fps.png",
         x=[i + 1 for i in range(len(experiment.train_fps_list))])
    plot(experiment.test_fps_list, plot_dir + "/test_fps.png",
         x=[i + 1 for i in range(len(experiment.test_fps_list))])

    plot(experiment.grad_updates_durations, plot_dir + "/grad_updates_durations.png",
         x=[i + 1 for i in range(len(experiment.grad_updates_durations))])

    # plot game logs
    # todo: not working properly
    plot_test_score(experiment.test_score_history, plot_dir + "/test_scores.png")
    plot(experiment.test_length_list, plot_dir + "/test_length.png",
         x=[i + 1 for i in range(len(experiment.test_length_list))])
    plot(experiment.test_game_duration_list, plot_dir + "/test_game_duration.png",
         x=[i + 1 for i in range(len(experiment.test_game_duration_list))])

    # todo: not working properly
    x = [i + 1 for i in range(experiment.max_games)]
    plot_learning_curve(x, experiment.reward_list, plot_dir + "/rewards_train.png")
    x = [i + 1 for i in range(int(experiment.test_max_games * experiment.max_games / experiment.test_interval))]
    plot_learning_curve(x, experiment.test_reward_list, plot_dir + "/rewards_test.png")

    plot_mean_sem(experiment.test_max_games, experiment.test_score_history, plot_dir + "/score_mean_sem.png",
                  "Testing Scores")
    try:
        # todo: not working properly
        plot_test_score(experiment.test_score_history, plot_dir + "/test_scores_mean_std.png")
    except:
        print("An exception occurred while plotting")
