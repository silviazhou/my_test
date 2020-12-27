
import os
import json


def main():

    update_dict = {
        "summary_train": False,
        "summary_train_dir": "./new_summaries"
    }

    update_dict_json_file = os.path.realpath("./my_test.json")
    with open(update_dict_json_file, "w") as update_json:
        json.dump(update_dict, update_json)

    my_cmd = "python ./train.py --config_update_json_file {}".format(
        update_dict_json_file)
    os.system(my_cmd)

    # parser.add_argument('--config_update_json_file', type=str, default="",
    #                     help='update config dict to config.py')
    #
    # if args_opt.config_update_json_file:
    #     print(111, "summary_train", cfg.summary_train)
    #     with open(args_opt.config_update_json_file, 'r') as update_file:
    #         config_update_dict = json.load(update_file)
    #         cfg.update(config_update_dict)
    #     print(222, "summary_train", cfg.summary_train)


if __name__ == "__main__":
    main()
