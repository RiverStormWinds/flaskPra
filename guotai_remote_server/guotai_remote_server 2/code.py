# coding=utf8

# import
from collections import Counter
from json import JSONDecodeError

import jieba
import json
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
from sklearn.externals import joblib
import web
import json
import datetime
import os

# constants
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(ROOT_DIR, 'static')

jieba.set_dictionary(os.path.join(STATIC_DIR, 'dict.txt'))

# todo
text_field_name = ['CASE_NAME', 'REMARKS', 'EXPECTED_OUTPUT_SET', 'INPUT_STRING_SET']
# text_field_name = ['CASE_NAME', 'REMARKS', 'EXPECTED_OUTPUT', 'INPUT_STRING']

cases_enum_field_name_list = ["CASE_LEVEL"]
case_project_enum_fields_list = ["GH_PROPERTY", "PT_PROPERTY", "ZYX", "GM"]
enum_field_name_list = ["CASE_LEVEL", "GH_PROPERTY", "PT_PROPERTY", "ZYX", "GM"]

# todo
case_field_name = ['CASES_ID', 'CASE_NAME', 'REMARKS', 'EXPECTED_OUTPUT_SET', 'INPUT_STRING_SET']
test_case_all_input_fields = ['CASES_ID', 'CASE_NAME', 'REMARKS', 'EXPECTED_OUTPUT_SET', 'INPUT_STRING_SET',
                              "CASE_LEVEL", "GH_PROPERTY", "PT_PROPERTY", "ZYX", "GM"]
# case_field_name = ['CASES_ID', 'CASE_NAME', 'REMARKS', 'EXPECTED_OUTPUT', 'INPUT_STRING']
# test_case_all_input_fields = ['CASES_ID', 'CASE_NAME', 'REMARKS', 'EXPECTED_OUTPUT', 'INPUT_STRING', "CASE_LEVEL", "GH_PROPERTY", "PT_PROPERTY", "ZYX", "GM"]


# TODO
CASE_MODEL_PATH = './tmp/m_risk_model_case.joblib'
CASE_MODEL_PATH_1 = './tmp/m_risk_model_case_1.joblib'
CASE_MODEL_NAME = 'M_RISK_CASE_MODEL'
stopwords_list = ['XXXX', '$', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '?', '_', '>', '<', ':', '【', '】', '-',
                  '（', ';', ',', '）', '(', ')', '“', '”', '、', '。', '《', '》', '一', '一些', '一何', '一切', '一则', '一方面', '一旦',
                  '一来', '一样', '一般', '一转眼', '万一', '上', '上下', '下', '不', '不仅', '不但', '不光', '不单', '不只', '不外乎', '不如', '不妨',
                  '不尽', '不尽然', '不得', '不怕', '不惟', '不成', '不拘', '不料', '不是', '不比', '不然', '不特', '不独', '不管', '不至于', '不若',
                  '不论', '不过', '不问', '与', '与其', '与其说', '与否', '与此同时', '且', '且不说', '且说', '两者', '个', '个别', '临', '为', '为了',
                  '为什么', '为何', '为止', '为此', '为着', '乃', '乃至', '乃至于', '么', '之', '之一', '之所以', '之类', '乌乎', '乎', '乘', '也',
                  '也好', '也罢', '了', '二来', '于', '于是', '于是乎', '云云', '云尔', '些', '亦', '人', '人们', '人家', '什么', '什么样', '今',
                  '介于', '仍', '仍旧', '从', '从此', '从而', '他', '他人', '他们', '以', '以上', '以为', '以便', '以免', '以及', '以故', '以期',
                  '以来', '以至', '以至于', '以致', '们', '任', '任何', '任凭', '似的', '但', '但凡', '但是', '何', '何以', '何况', '何处', '何时',
                  '余外', '作为', '你', '你们', '使', '使得', '例如', '依', '依据', '依照', '便于', '俺', '俺们', '倘', '倘使', '倘或', '倘然', '倘若',
                  '借', '假使', '假如', '假若', '傥然', '像', '儿', '先不先', '光是', '全体', '全部', '兮', '关于', '其', '其一', '其中', '其二',
                  '其他', '其余', '其它', '其次', '具体地说', '具体说来', '兼之', '内', '再', '再其次', '再则', '再有', '再者', '再者说', '再说', '冒',
                  '冲', '况且', '几', '几时', '凡', '凡是', '凭', '凭借', '出于', '出来', '分别', '则', '则甚', '别', '别人', '别处', '别是', '别的',
                  '别管', '别说', '到', '前后', '前此', '前者', '加之', '加以', '即', '即令', '即使', '即便', '即如', '即或', '即若', '却', '去', '又',
                  '又及', '及', '及其', '及至', '反之', '反而', '反过来', '反过来说', '受到', '另', '另一方面', '另外', '另悉', '只', '只当', '只怕',
                  '只是', '只有', '只消', '只要', '只限', '叫', '叮咚', '可', '可以', '可是', '可见', '各', '各个', '各位', '各种', '各自', '同',
                  '同时', '后', '后者', '向', '向使', '向着', '吓', '吗', '否则', '吧', '吧哒', '吱', '呀', '呃', '呕', '呗', '呜', '呜呼', '呢',
                  '呵', '呵呵', '呸', '呼哧', '咋', '和', '咚', '咦', '咧', '咱', '咱们', '咳', '哇', '哈', '哈哈', '哉', '哎', '哎呀', '哎哟',
                  '哗', '哟', '哦', '哩', '哪', '哪个', '哪些', '哪儿', '哪天', '哪年', '哪怕', '哪样', '哪边', '哪里', '哼', '哼唷', '唉', '唯有',
                  '啊', '啐', '啥', '啦', '啪达', '啷当', '喂', '喏', '喔唷', '喽', '嗡', '嗡嗡', '嗬', '嗯', '嗳', '嘎', '嘎登', '嘘', '嘛',
                  '嘻', '嘿', '嘿嘿', '因', '因为', '因了', '因此', '因着', '因而', '固然', '在', '在下', '在于', '地', '基于', '处在', '多', '多么',
                  '多少', '大', '大家', '她', '她们', '好', '如', '如上', '如上所述', '如下', '如何', '如其', '如同', '如是', '如果', '如此', '如若',
                  '始而', '孰料', '孰知', '宁', '宁可', '宁愿', '宁肯', '它', '它们', '对', '对于', '对待', '对方', '对比', '将', '小', '尔', '尔后',
                  '尔尔', '尚且', '就', '就是', '就是了', '就是说', '就算', '就要', '尽', '尽管', '尽管如此', '岂但', '己', '已', '已矣', '巴', '巴巴',
                  '并', '并且', '并非', '庶乎', '庶几', '开外', '开始', '归', '归齐', '当', '当地', '当然', '当着', '彼', '彼时', '彼此', '往', '待',
                  '很', '得', '得了', '怎', '怎么', '怎么办', '怎么样', '怎奈', '怎样', '总之', '总的来看', '总的来说', '总的说来', '总而言之', '恰恰相反',
                  '您', '惟其', '慢说', '我', '我们', '或', '或则', '或是', '或曰', '或者', '截至', '所', '所以', '所在', '所幸', '所有', '才', '才能',
                  '打', '打从', '把', '抑或', '拿', '按', '按照', '换句话说', '换言之', '据', '据此', '接着', '故', '故此', '故而', '旁人', '无',
                  '无宁', '无论', '既', '既往', '既是', '既然', '时候', '是', '是以', '是的', '曾', '替', '替代', '最', '有', '有些', '有关', '有及',
                  '有时', '有的', '望', '朝', '朝着', '本', '本人', '本地', '本着', '本身', '来', '来着', '来自', '来说', '极了', '果然', '果真', '某',
                  '某个', '某些', '某某', '根据', '欤', '正值', '正如', '正巧', '正是', '此', '此地', '此处', '此外', '此时', '此次', '此间', '毋宁',
                  '每', '每当', '比', '比及', '比如', '比方', '没奈何', '沿', '沿着', '漫说', '焉', '然则', '然后', '然而', '照', '照着', '犹且',
                  '犹自', '甚且', '甚么', '甚或', '甚而', '甚至', '甚至于', '用', '用来', '由', '由于', '由是', '由此', '由此可见', '的', '的确', '的话',
                  '直到', '相对而言', '省得', '看', '眨眼', '着', '着呢', '矣', '矣乎', '矣哉', '离', '竟而', '第', '等', '等到', '等等', '简言之',
                  '管', '类如', '紧接着', '纵', '纵令', '纵使', '纵然', '经', '经过', '结果', '给', '继之', '继后', '继而', '综上所述', '罢了', '者',
                  '而', '而且', '而况', '而后', '而外', '而已', '而是', '而言', '能', '能否', '腾', '自', '自个儿', '自从', '自各儿', '自后', '自家',
                  '自己', '自打', '自身', '至', '至于', '至今', '至若', '致', '般的', '若', '若夫', '若是', '若果 ', '若非', '莫不然', '莫如', '莫若',
                  '虽', '虽则', '虽然', '虽说', '被', '要', '要不', '要不是', '要不然', '要么', '要是', '譬喻', '譬如', '让', '许多', '论', '设使',
                  '设或', '设若', '诚如', '诚然', '该', '说来', '诸', '诸位', '诸如', '谁', '谁人', '谁料', '谁知', '贼死', '赖以', '赶', '起', '起见',
                  '趁', '趁着', '越是', '距', '跟', '较', '较之', '边', '过', '还', '还是', '还有', '还要', '这', '这一来', '这个', '这么', '这么些',
                  '这么样', '这么点儿', '这些', '这会儿', '这儿', '这就是说', '这时', '这样', '这次', '这般', '这边', '这里', '进而', '连', '连同', '逐步',
                  '通过', '遵循', '遵照', '那', '那个', '那么', '那么些', '那么样', '那些', '那会儿', '那儿', '那时', '那样', '那般', '那边', '那里', '都',
                  '鄙人', '鉴于', '针对', '阿', '除', '除了', '除外', '除开', '除此之外', '除非', '随', '随后', '随时', '随着', '难道说', '非但', '非徒',
                  '非特', '非独', '靠', '顺', '顺着', '首先', '！', '，', '：', '；', '？']


def load_model():
    print('Load model')
    case_save_data = joblib.load(CASE_MODEL_PATH_1)
    print("Load finish")
    return case_save_data


# read data
def get_text_data_set(fields, dict_list):
    column_dict = {field: [] for field in fields}
    for row in dict_list:
        for field in fields:
            column_dict[field].append(row[field])

    return column_dict


def get_data_fields(field_name_list, data_dict):
    fields_dict_all = []
    dict_all = data_dict

    for row in dict_all:
        fields_dict = {}
        for field_name in field_name_list:
            fields_dict[field_name] = row[field_name]
        fields_dict_all.append(fields_dict)
    return fields_dict_all


def filter_list_all_to_dict(raw_list_all, index_list_all):
    # print(len(index_list_all))
    # print(len(raw_list_all))
    new_dict_list = []
    for i in range(len(index_list_all)):
        index_list = index_list_all[i]
        raw_list = raw_list_all[i]
        new_dict_list.append({index: raw_list[index] for index in index_list})
    return new_dict_list


def simliarity_dict_merge(current_layer_similarity_dict_list, last_layer_similarity_filter_dict_list):
    merge_similarity_dict_1_list = []
    # print(current_layer_similarity_dict_list)
    for i in range(len(current_layer_similarity_dict_list)):
        merge_similarity_dict_1 = dict(
            Counter(current_layer_similarity_dict_list[i]) + Counter(last_layer_similarity_filter_dict_list[i]))
        merge_similarity_dict_1_list.append(merge_similarity_dict_1)
    return merge_similarity_dict_1_list


def filter_list_with_index_all(old_list, index_list_all):
    new_list_all = []
    for index_list in index_list_all:
        new_list_all.append(old_list[index] for index in index_list)
    return new_list_all


def set_dict_list(old_dict_list, coefficient):
    new_dict_list = []
    for old_dict in old_dict_list:
        new_dict = {}
        for key, value in old_dict.items():
            new_dict[key] = value * coefficient
        new_dict_list.append(new_dict)
    return new_dict_list


def dict_list_value_filter(old_dict_list, min_value):
    new_dict_list = []
    new_dict_list_sorted = []
    new_keys = []
    sorted_new_keys_all = []
    for old_dict in old_dict_list:
        new_dict = {}
        for key, value in old_dict.items():
            if value > min_value:
                new_dict[key] = value
                new_keys.append(key)
        new_dict_list.append(new_dict)
    for new_dict in new_dict_list:
        new_dict_sorted = sorted(new_dict.items(), key=lambda item: item[1], reverse=True)
        new_dict_list_sorted.append(new_dict_sorted)
    for new_dict_sorted in new_dict_list_sorted:
        sorted_new_keys = []
        for sorted_tuple in new_dict_sorted:
            sorted_new_keys.append(sorted_tuple[0])
        sorted_new_keys_all.append(sorted_new_keys)
    return new_dict_list, sorted_new_keys_all


def cut_word(text_list):
    text_cut_list = []
    for text in text_list:
        text_cut = jieba.lcut(text)
        seg_list = ''
        for word in text_cut:
            if word not in stopwords_list:
                seg_list += word
                seg_list += ' '
        text_cut_list.append(seg_list)
    return text_cut_list


def filter_dict(token_list_all):
    frequency = {}
    for token_list in token_list_all:
        for token in token_list:
            if token in frequency.keys():
                frequency[token] += 1
            else:
                frequency[token] = 1
    new_token_list_all = [[token for token in token_list if frequency[token] > 1] for token_list in token_list_all]
    return new_token_list_all


def get_recommend_row_with_similiarity(index_list, row_list, similiarity_dict):
    return [(row_list[index], similiarity_dict[index] / 4) for index in index_list]


class CaseSimilarityModel(object):
    def __init__(self, train_num, test_num, model_info_dict):
        self.train_num = train_num
        self.test_num = test_num
        self.model_info_dict = model_info_dict

    def _info_one_layer_tf_idf(self, layer_num, new_query_cut_list, last_layer_index_list_all,
                               last_layer_similarity_filter_dict_list):
        current_layer_similarity_list = self._get_similarity(new_query_cut_list, layer_num)
        current_layer_similarity_dict_list = filter_list_all_to_dict(current_layer_similarity_list,
                                                                     last_layer_index_list_all)

        merge_similarity_dict_1_list = simliarity_dict_merge(current_layer_similarity_dict_list,
                                                             last_layer_similarity_filter_dict_list)
        merge_similarity_dict_1_1_list = set_dict_list(merge_similarity_dict_1_list, 1 / layer_num)

        merge_similarity_dict_filter_1_list, current_layer_index_list_all = dict_list_value_filter(
            merge_similarity_dict_1_1_list, 0.5)
        merge_similarity_dict_1_filter_list = filter_list_all_to_dict(merge_similarity_dict_1_list,
                                                                      current_layer_index_list_all)
        return current_layer_index_list_all, merge_similarity_dict_1_filter_list

    def _get_similarity(self, new_query_cut_list, layer_num):
        # new_query_cut_list = cut_word(new_query_list)
        vectorizer = self.model_info_dict['vectorizer'][layer_num - 1]
        tf_idf = self.model_info_dict['tf_idf'][layer_num - 1]
        query_matrix = vectorizer.transform(new_query_cut_list)
        cosine_similarities_list = linear_kernel(query_matrix, tf_idf).flatten()
        cosine_similarities_list = np.reshape(cosine_similarities_list, (self.test_num, self.train_num))
        return cosine_similarities_list

    def info(self, test_text_name2text_dict_list):
        assert self.model_info_dict is not None

        # print(one_test_text_name2text_dict)
        index_list_all = []
        similarity_dict_1_filter_list = []
        for i in range(self.test_num):
            index_list_all.append(list(range(self.train_num)))
            similarity_dict_1_filter_list.append({})

        for i, field_name in enumerate(text_field_name):
            text_list = test_text_name2text_dict_list[field_name]
            if len(text_list) > 0:
                index_list_all, similarity_dict_1_filter_list = self._info_one_layer_tf_idf(i + 1,
                                                                                            text_list,
                                                                                            index_list_all,
                                                                                            similarity_dict_1_filter_list)
                # print(index_list)
        return index_list_all, similarity_dict_1_filter_list


def get_enum_field_list(field_dict_all, enum_field_name):
    enum_field_list = [row[enum_field_name] for row in field_dict_all]
    return enum_field_list


def enum_value_2_num(enum_field_list, maple):
    num = len(maple)
    new_enum_field_list = []
    for item in enum_field_list:
        if item in maple.keys():
            new_enum_field_list.append(maple[item])
        else:
            new_enum_field_list.append(num)
            num += 1
    return new_enum_field_list


def get_test_enum_field_array(test_data, maples):
    test_num = len(test_data)
    test_case_enum_field_array = np.empty(shape=[test_num, 0])
    test_project_enum_field_array = np.empty(shape=[test_num, 0])

    for cases_enum_field_name in cases_enum_field_name_list:
        current_list = get_enum_field_list(test_data, cases_enum_field_name)
        test_case_enum_field_array = np.c_[
            test_case_enum_field_array, np.array(enum_value_2_num(current_list, maples[cases_enum_field_name]))]

    for case_project_enum_field_name in case_project_enum_fields_list:
        current_list = get_enum_field_list(test_data, case_project_enum_field_name)
        test_project_enum_field_array = np.c_[test_project_enum_field_array, np.array(
            enum_value_2_num(current_list, maples[case_project_enum_field_name]))]

    # print(test_case_enum_field_array)
    # print(test_project_enum_field_array)
    return test_case_enum_field_array, test_project_enum_field_array


def get_enumeration_field_similarity(enum_array, test_array):
    enum_array = np.array(enum_array)
    test_array = np.array(test_array)
    result = (enum_array == test_array)
    similarity = (result == True).sum(1)
    return similarity


def get_final_similarity(index_list, similarity_dict_filter, case_enum_field_array, project_enum_field_array,
                         test_case_enum_field_array, test_project_enum_field_array):
    final_similarity_dict_all = {}
    case_enum_fields_similarity = get_enumeration_field_similarity(case_enum_field_array, test_case_enum_field_array)
    case_project_enum_fields_similarity = get_enumeration_field_similarity(project_enum_field_array,
                                                                           test_project_enum_field_array)

    for index in index_list:
        final_similarity_dict_all[index] = similarity_dict_filter[index] * 0.8 + case_enum_fields_similarity[
            index] * 0.1 + case_project_enum_fields_similarity[index] * 0.1

    final_similarity_dict_all_1 = sorted(final_similarity_dict_all.items(), key=lambda item: item[1], reverse=True)
    new_index_list = [index_turple[0] for index_turple in final_similarity_dict_all_1]
    return new_index_list, final_similarity_dict_all


def get_similarity_cases_id(index_list, case_data_all):
    case_id_list = []
    case_list = []

    for index in index_list:
        case = case_data_all[index]
        case_id = case["CASES_ID"]
        case_id_list.append(case_id)
        case_list.append(case)
        print(case)

    return case_id_list


def similarity_model(test_data_text_set_cut, test_data, model_info_dict, train_num, case_enum_field_array,
                     project_enum_field_array, case_id_list, maples, train_case_data_use_field_set):
    # test
    test_num = len(test_data)
    # cases_train_data = read_csv_in_dict(os.path.join(INPUT_DIR, 'sx_final_project_shuffle1-split.csv'))[
    #                    train_start: train_end]
    # case_data_text_set = get_data_fields(case_field_name, cases_train_data)
    find_case_num_list = []
    # print(len(case_data_text_set))

    test_data_text_set = get_text_data_set(case_field_name, test_data)
    test_name2text_list = {}
    for field_name in text_field_name:
        test_name2text_list[field_name] = test_data_text_set[field_name]

    model = CaseSimilarityModel(train_num, test_num, model_info_dict)
    index_list_all, similarity_dict_1_filter_list = model.info(test_data_text_set_cut)
    similarity_case_id_all = []

    test_case_enum_field_array, test_project_enum_field_array = get_test_enum_field_array(test_data, maples)

    for i in range(test_num):
        print(i)
        print("input test case")
        current_test_text = {}

        for field_name in case_field_name:
            current_test_text[field_name] = test_data_text_set[field_name][i]

        print(current_test_text)
        print("find cases")

        # 文本相似得到的训练集中相似的case的index,对应case表中case的顺序，这里只有当前一个测试用例的相似用例
        current_index_list = index_list_all[i]
        # 当前一个测试用例和其他用例的相似度字典，key是训练集中用例的index，value是相似度
        current_similarity_dict_filter = similarity_dict_1_filter_list[i]
        # 当前一个测试用例的枚举字段的字典
        current_test_case_enum_field_array = test_case_enum_field_array[i]
        current_test_project_enum_field_array = test_project_enum_field_array[i]

        current_new_index_list, current_final_similarity_dict_all = get_final_similarity(current_index_list,
                                                                                         current_similarity_dict_filter,
                                                                                         case_enum_field_array,
                                                                                         project_enum_field_array,
                                                                                         current_test_case_enum_field_array,
                                                                                         current_test_project_enum_field_array
                                                                                         )
        # 根据index获取case_id
        current_case_id_list = [current_test_text["CASES_ID"]]
        current_case_id_list += get_similarity_cases_id(current_new_index_list, train_case_data_use_field_set)
        # current_case_id_list += get_similarity_cases_id(current_new_index_list, case_data_text_set)
        find_case_num_list.append(len(current_case_id_list) - 1)
        # 添加到测试集所有数据的相似用例的list中
        similarity_case_id_all.append(current_case_id_list)

    # print(find_result(find_case_num_list))
    # print(current_case_id_list)
    return similarity_case_id_all


def find_result(find_case_num_list):
    have_find = [num for num in find_case_num_list if num > 0]
    find_result = {
        "have find": len(have_find),
        "median": np.median(find_case_num_list)
    }
    return find_result


def simialrity_list_2_dict(similarity_case_id_all):
    simialrity_dict = {}
    for simialrity_list in similarity_case_id_all:
        case_id = simialrity_list[0]
        simialrity_case_list = []
        if len(simialrity_list) > 1:
            simialrity_case_list = simialrity_list[1:]
        simialrity_dict[case_id] = simialrity_case_list
    return simialrity_dict


def get_cut(test_data):
    test_data_text_set = get_text_data_set(case_field_name, test_data)
    test_data_text_set_cut = {}
    for i, field_name in enumerate(text_field_name):
        text_list = test_data_text_set[field_name]
        text_list_cut = cut_word(text_list)
        test_data_text_set_cut[field_name] = text_list_cut

    return test_data_text_set_cut


def model_merge(test_data, model_info_dict, train_num, case_enum_field_array, project_enum_field_array, case_id_list,
                maples, train_case_data_use_field_set):
    test_data_text_set_cut = get_cut(test_data)
    # similarity_case_id_all = similarity_model(test_data_text_set_cut,test_data)
    similarity_case_id_all = similarity_model(test_data_text_set_cut, test_data, model_info_dict, train_num,
                                              case_enum_field_array, project_enum_field_array, case_id_list, maples,
                                              train_case_data_use_field_set)
    similarity_case_id_all = simialrity_list_2_dict(similarity_case_id_all)
    return similarity_case_id_all
    # print(similarity_case_id_all)


def valid_item(item):
    if type(item) != dict:
        return 'Should be dict, but {}.'.format(type(item))
    for field in test_case_all_input_fields:
        if field not in item:
            return 'Should contain field <{}>.'.format(field)
        if type(item[field]) != str:
            return 'Field <{}> should be str, but {}.'.format(field, type(item[field]))
    return None


class CalModelMerge(object):
    def POST(self):
        web.header('content-type', 'text/json')
        raw_data = web.data()

        try:
            test_data = json.loads(raw_data)
        except JSONDecodeError:
            web.ctx.status = '400 '
            return json.dumps({
                'error': 'Invalid Json.'
            })

        if type(test_data) != list:
            web.ctx.status = '400 '
            return json.dumps({
                'error': 'Input Case Should be list, but {}.'.format(type(test_data))
            })

        for i, item in enumerate(test_data):
            err = valid_item(item)
            if err:
                web.ctx.status = '400 '
                return json.dumps({
                    'error': '#{}: {}'.format(i, err)
                })

        print(test_data[0])
        case_save_data = load_model()
        model_info_dict = case_save_data["model_info_dict"]
        train_num = case_save_data["train_num"]
        case_enum_field_array = case_save_data["case_enum_field_array"]
        project_enum_field_array = case_save_data["project_enum_field_array"]
        case_id_list = case_save_data['case_id_list']
        maples = case_save_data['maples']
        case_train_data_use_field_set = case_save_data['cases_train_data_use_field_set']
        case_test_data_use_field_set = case_save_data['cases_test_data_use_field_set']

        result = model_merge(test_data, model_info_dict, train_num, case_enum_field_array, project_enum_field_array,
                             case_id_list, maples, case_train_data_use_field_set)
        result_json = json.dumps(result)
        print(result)
        return result_json
