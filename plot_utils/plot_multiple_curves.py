from math import sqrt
from statistics import stdev, mean
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

dir = "results/figures/"
file_1c = 'results/tmp/max_games_mode_continuous_O_O_a_60K_every10_Shafti_descending_christina_online_1_test/test_scores.csv'
file_1p = 'results/tmp/max_games_mode_continuous_O_O_a_60K_every10_Shafti_descending_panos_1_test/test_scores.csv'

file_1 = 'results/tmp/max_games_mode_continuous_O_O_a_60K_every10_Shafti_descending_fotis_online_2_test/test_scores.csv'
file_2 = 'results/tmp/max_games_mode_continuous_O_O_a_60K_every10_Shafti_descending_fotis_local_1_test/test_scores.csv'
file_3 = 'results/tmp/max_games_mode_continuous_O_O_a_60K_every10_Shafti_descending_fotis_local_2_test/test_scores.csv'
file_4 = 'results/tmp/max_games_mode_continuous_O_O_a_60K_every10_Shafti_descending_fotis_local_3_test/test_scores.csv'
#
# file_1t = 'results/tmp/loop1_O_O_a_28K_every10_Sparse_2_descending_thanasis_1/test_score_history.csv'
# file_2t = 'results/tmp/loop1_O_O_a_28K_every10_Sparse_2_descending_thanasis_2/test_score_history.csv'
# file_3t = 'results/tmp/loop1_O_O_a_28K_every10_Sparse_2_descending_thanasis_3/test_score_history.csv'
#
# file_1f = 'results/tmp/expert_alg1_online_28K_every10_sparse2_descending_1/test_score_history.csv'
# file_2f = 'results/tmp/expert_alg1_online_28K_every10_sparse2_descending_2/test_score_history.csv'
# file_3f = 'results/tmp/expert_alg1_online_28K_every10_sparse2_descending_3/test_score_history.csv'

# file_name_1 = 'tmp/expert_alg1_online_154K_every10_sparse2_1/test_score_history.csv'
# file_name_2 = 'tmp/expert_alg1_online_154K_every10_sparse2_2/test_score_history.csv'
# file_name_3 = 'tmp/expert_alg1_online_154K_every10_sparse2_3/test_score_history.csv'
#
# file_name_4 = 'tmp/expert_alg1_offline_154K_every10_sparse2_1/test_score_history.csv'
# file_name_5 = 'tmp/expert_alg1_offline_154K_every10_sparse2_2/test_score_history.csv'
# file_name_6 = 'tmp/expert_alg1_offline_154K_every10_sparse2_3/test_score_history.csv'
#
# file_name_7 = 'tmp/expert_alg1_online_28K_every10_sparse2_1/test_score_history.csv'
# file_name_8 = 'tmp/expert_alg1_online_28K_every10_sparse2_2/test_score_history.csv'
# file_name_9 = 'tmp/expert_alg1_online_28K_every10_sparse2_3/test_score_history.csv'
#
# file_name_10 = 'tmp/expert_alg1_offline_28K_every10_sparse2_1/test_score_history.csv'
# file_name_11 = 'tmp/expert_alg1_offline_28K_every10_sparse2_2/test_score_history.csv'
# file_name_12 = 'tmp/expert_alg1_offline_28K_every10_sparse2_3/test_score_history.csv'
#
# file_name_13 = 'tmp/expert_alg1_online_28K_every10_sparse2_descending_1/test_score_history.csv'
# file_name_14 = 'tmp/expert_alg1_online_28K_every10_sparse2_descending_2/test_score_history.csv'
# file_name_15 = 'tmp/expert_alg1_online_28K_every10_sparse2_descending_3/test_score_history.csv'
#
# file_name_16 = 'tmp/expert_alg1_offline_28K_every10_sparse2_descending_1/test_score_history.csv'
# file_name_17 = 'tmp/expert_alg1_offline_28K_every10_sparse2_descending_2/test_score_history.csv'
# file_name_18 = 'tmp/expert_alg1_offline_28K_every10_sparse2_descending_3/test_score_history.csv'
#
# file_name_1t = 'tmp/thanasis/loop1_O_O_a_154K_every10_Sparse_2_normal_thanasis_1/test_score_history.csv'
# file_name_2t = 'tmp/thanasis/loop1_O_O_a_154K_every10_Sparse_2_normal_thanasis_2/test_score_history.csv'
# file_name_3t = 'tmp/thanasis/loop1_O_O_a_154K_every10_Sparse_2_normal_thanasis_3/test_score_history.csv'
#
# file_name_4t = 'tmp/thanasis/loop1_O_a_154K_every10_Sparse_2_normal_thanasis_1/test_score_history.csv'
# file_name_5t = 'tmp/thanasis/loop1_O_a_154K_every10_Sparse_2_normal_thanasis_2/test_score_history.csv'
# file_name_6t = 'tmp/thanasis/loop1_O_a_154K_every10_Sparse_2_normal_thanasis_3/test_score_history.csv'
#
# file_name_7t = 'tmp/thanasis/loop1_O_O_a_28K_every10_Sparse_2_normal_thanasis_1/test_score_history.csv'
# file_name_8t = 'tmp/thanasis/loop1_O_O_a_28K_every10_Sparse_2_normal_thanasis_2/test_score_history.csv'
# file_name_9t = 'tmp/thanasis/loop1_O_O_a_28K_every10_Sparse_2_normal_thanasis_3/test_score_history.csv'
#
# file_name_10t = 'tmp/thanasis/loop1_O_a_28K_every10_Sparse_2_normal_thanasis_1/test_score_history.csv'
# file_name_11t = 'tmp/thanasis/loop1_O_a_28K_every10_Sparse_2_normal_thanasis_2/test_score_history.csv'
# file_name_12t = 'tmp/thanasis/loop1_O_a_28K_every10_Sparse_2_normal_thanasis_3/test_score_history.csv'
#
# file_name_13t = 'tmp/thanasis/loop1_O_O_a_28K_every10_Sparse_2_descending_thanasis_1/test_score_history.csv'
# file_name_14t = 'tmp/thanasis/loop1_O_O_a_28K_every10_Sparse_2_descending_thanasis_2/test_score_history.csv'
# file_name_15t = 'tmp/thanasis/loop1_O_O_a_28K_every10_Sparse_2_descending_thanasis_3/test_score_history.csv'
#
# file_name_16t = 'tmp/thanasis/loop1_O_a_28K_every10_Sparse_2_descending_thanasis_1/test_score_history.csv'
# file_name_17t = 'tmp/thanasis/loop1_O_a_28K_every10_Sparse_2_descending_thanasis_2/test_score_history.csv'
# file_name_18t = 'tmp/thanasis/loop1_O_a_28K_every10_Sparse_2_descending_thanasis_3/test_score_history.csv'

# random_files = [random_file_1]
# legend_names_1 = ["offline_2000_sparse1", "offline_2000_sparse2"]
# legend_names_2 = ["offline_154_every10_sparse1"]
# legend_names = ["offline_28K_every5_sparse2", "online_28K_every5_sparse2", "offline_154K_every10_sparse2", "online_154K_every10_sparse2"]
# legend_names = ["O-O-a 154K", "O-a 154K", "O-O-a 28K Descending", "O-a 28K Descending"]
# legend_names = ["O-O-a 154K", "O-a 154K", "O-O-a 28K", "O-a 28K"]
# legend_names = ["O-O-a 28K Old", "O-O-a 60K New"]
# legend_names = ["O-O-a 28K Maze_v0 40sec", "O-O-a 60K  Maze_v2 40sec", "O-O-a 60K  Maze_v2 30sec"]
legend_names = ["O-O-a 60K Expert", "O-O-a 60K Novel User 1", "O-O-a 60K Novel User 2"]

# filename_list_1 = [file_name_1, file_name_2]
# filename_list_2 = [file_name_3, file_name_4]

colors = ["g", "b", "r", "m", "navy", "darkorange"]
colors_light = ["limegreen", "cornflowerblue", "lightcoral", "violet", "slateblue", "wheat"]

fill = True
start = 0
end = 205


def plot(filename_list, legend_names, figure_file=None):
    fig, ax = plt.subplots()
    axes = plt.gca()
    axes.set_ylim([start, end])
    # colors = sns.color_palette("husl", 5)
    with sns.axes_style("darkgrid"):
        for c, file_name_sublist in enumerate(filename_list):
            merge_lists = []
            for file_name in file_name_sublist:
                my_data = np.genfromtxt(file_name, delimiter=',')
                merge_lists.append(my_data)
            # random = np.genfromtxt(random_file, delimiter=',')
            # means, stds, x_axis = [mean(random)], [stdev(random) / sqrt(len(random))], [0]
            means, stds, x_axis = [], [], []
            for i in range(0, len(merge_lists[0]), 10):
                data = []
                for file_to_merge in merge_lists:
                    data.extend(file_to_merge[i:i + 10])
                means.append(mean(data))
                stds.append(stdev(data) / sqrt(len(data)))
                x_axis.append(i)
            means, stds, x_axis = np.asarray(means), np.asarray(stds), np.asarray(x_axis)
            # meanst = np.array(means.ix[i].values[3:-1], dtype=np.float64)
            # sdt = np.array(stds.ix[i].values[3:-1], dtype=np.float64)
            if fill:
                ax.plot(x_axis, means, c=colors[c], label=legend_names[c], marker='*')
                ax.fill_between(x_axis, means - stds, means + stds, facecolor=colors_light[c], alpha=0.5)
            else:
                plt.errorbar(x_axis, means, stds, label=legend_names[c], marker='*')
        ax.yaxis.set_ticks(np.arange(start, end, 10))
        ax.set_ylabel('Score')
        ax.set_xlabel('Trials')
        plt.grid()
        plt.legend(loc='lower right')
        plt.title("Testing Score Mean and SEM")
        plt.savefig(figure_file)
        # plt.show()

#
# plot([[file_1f, file_2f, file_3f, file_1t, file_2t, file_3t],
#       [file_1, file_2]], legend_names, figure_file=dir + "old_vs_new.png")


# plot([[file_1f, file_2f, file_3f, file_1t, file_2t, file_3t], [file_3], [file_4]], legend_names, figure_file=dir + "v0_v2.png")
plot([[file_4],[file_1c], [file_1p]], legend_names, figure_file=dir + "expert_vs_novel_users_40games.png")

# plot([[file_name_1, file_name_2, file_name_3, file_name_1t, file_name_2t, file_name_3t],
#       [file_name_4, file_name_5, file_name_6, file_name_4t, file_name_5t, file_name_6t],
#       [file_name_7, file_name_8, file_name_9, file_name_7t, file_name_8t, file_name_9t],
#       [file_name_10, file_name_11, file_name_12, file_name_10t, file_name_11t, file_name_12t]],
#     legend_names,
#      figure_file=dir + "154K vs 28K 2 users.png")

# plot([filename_list_sparse1[0]], [legend_names_sparse1[0]], figure_file=dir +"offline_sparse_1")
# plot([filename_list_sparse1[1]], [legend_names_sparse1[1]], figure_file=dir +"online_sparse_1")
# plot([filename_list_sparse2[0]], [legend_names_sparse2[0]], figure_file=dir +"offline_sparse_2")
# plot([filename_list_sparse2[1]], [legend_names_sparse2[1]], figure_file=dir +"online_sparse_2")
#
# plot([filename_list_sparse1[0], filename_list_sparse2[0]], [legend_names_sparse1[0],legend_names_sparse1[0]], figure_file=dir +"offline_all rewards")
# plot([filename_list_sparse1[1], filename_list_sparse2[1]], [legend_names_sparse1[1], legend_names_sparse2[1]], figure_file=dir +"online_all rewards")
#
# plot(filename_list_sparse1, legend_names_sparse1, figure_file=dir +"Learning_Comparison_sparse_1")
# plot(filename_list_sparse2, legend_names_sparse2, figure_file=dir +"Learning_Comparison_sparse_2")
# plot(filename_list_sparse1 + filename_list_sparse2, legend_names_sparse1 + legend_names_sparse2,
#      figure_file=dir +"Learning_Comparison_all rewards")
