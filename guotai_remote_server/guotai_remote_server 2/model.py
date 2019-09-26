# coding=utf8

import csv
import os
import pyodbc

import jieba
import numpy as np
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# constants

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(ROOT_DIR, 'static')
INPUT_DIR = os.path.join(STATIC_DIR, 'input')

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

# TODO
CASE_MODEL_PATH = './tmp/m_risk_model_case.joblib'
CASE_MODEL_NAME = 'M_RISK_CASE_MODEL'
CASE_MODEL_PATH_1 = './tmp/m_risk_model_case_1.joblib'
CASE_MODEL_NAME_1 = 'M_RISK_CASE_MODEL_1'

train_start = 0
train_end = 100
test_start = 200
test_end = 210


def conn_db2():
    # database_info_dict = read_config()

    try:
        dbstring = u'driver={IBM DB2 ODBC DRIVER};' \
                   u'database=%s;' \
                   u'hostname=%s;' \
                   u'port=%s;' \
                   u'protocol=tcpip;' \
                   u'uid=%s;' \
                   u'pwd=%s;' \
                   u'LONGDATACOMPAT=1;' \
                   u'LOBMAXCOLUMNSIZE=10485875;' % ("AUTOTEST",
                                                    "10.189.111.9",
                                                    "50000",
                                                    "Administrator",
                                                    "gtja.8888")

        conn = pyodbc.connect(dbstring)
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print(e)
        # GlobalLogging.getLog().info(e[0].decode('gbk'))


def read_data_from_db2():
    print('read_data_from_db2...')
    conn, cursor = conn_db2()

    train_data = []
    if conn:
        last_id = 0
        sql = """
            SELECT  {}, ID
              FROM TIMESVC.SX_AI_RISK_TRAIN_DATA 
              WHERE ID > {}
              ORDER BY ID
              fetch first 10000 rows only
        """.format(','.join(test_case_all_input_fields), last_id)
        cursor.execute(sql)
        rows = cursor.fetchall()
        while rows:
            print('read {}...'.format(last_id))
            for row in rows:
                dict_row = {field: row[i] for i, field in enumerate(test_case_all_input_fields)}
                train_data.append(dict_row)
                last_id = row[-1]

            sql = """
                SELECT  {}, ID
                  FROM TIMESVC.SX_AI_RISK_TRAIN_DATA 
                  WHERE ID > {}
                  ORDER BY ID
                  fetch first 10000 rows only
            """.format(','.join(test_case_all_input_fields), last_id)
            cursor.execute(sql)
            rows = cursor.fetchall()

        print('train_data[: 10]')
        print(train_data[: 10])

    cursor.close()
    conn.close()

    return train_data[0: 100]


def read_csv_in_dict(filename):
    csv_dict_list = []
    with open(filename, 'r', encoding='utf-8-sig') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            row = dict(row)
            csv_dict_list.append(row)
    return csv_dict_list


# read data
def get_text_data_set(fields, dict_list):
    column_dict = {field: [] for field in fields}
    for row in dict_list:
        for field in fields:
            column_dict[field].append(row[field])

    return column_dict


# todo
# 获取枚举字段值的maple，不同值对应不同的数字
def get_enum_value_2_num_maple(enum_field_list):
    value_2_num_maple = {}
    num = 0
    for value in enum_field_list:
        if value not in value_2_num_maple.keys():
            value_2_num_maple[value] = num
            num += 1
    return value_2_num_maple


# todo
def enum_value_2_num(enum_field_list, maple):
    new_enum_field_list = [maple[value] for value in enum_field_list]
    return new_enum_field_list


# todo
def get_enum_field_list(field_dict_all, enum_field_name):
    enum_field_list = [row[enum_field_name] for row in field_dict_all]
    return enum_field_list


# todo
def get_maples(cases_train_data):
    maples = {}
    train_num = len(cases_train_data)
    case_enum_field_array = np.empty(shape=[train_num, 0])
    project_enum_field_array = np.empty(shape=[train_num, 0])

    for cases_enum_field_name in cases_enum_field_name_list:
        current_list = get_enum_field_list(cases_train_data, cases_enum_field_name)
        maples[cases_enum_field_name] = get_enum_value_2_num_maple(current_list)
        case_enum_field_array = np.c_[
            case_enum_field_array, np.array(enum_value_2_num(current_list, maples[cases_enum_field_name]))]

    for case_project_enum_field_name in case_project_enum_fields_list:
        current_list = get_enum_field_list(cases_train_data, case_project_enum_field_name)
        maples[case_project_enum_field_name] = get_enum_value_2_num_maple(current_list)
        project_enum_field_array = np.c_[
            project_enum_field_array, np.array(enum_value_2_num(current_list, maples[case_project_enum_field_name]))]

    return maples, case_enum_field_array, project_enum_field_array


def get_data_fields(field_name_list, data_dict):
    fields_dict_all = []
    dict_all = data_dict

    for row in dict_all:
        fields_dict = {}
        for field_name in field_name_list:
            fields_dict[field_name] = row[field_name]
        fields_dict_all.append(fields_dict)
    return fields_dict_all


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


def shuffle_data(data):
    index_list = np.arange(len(data))
    shuffle_new_data = []
    for i in index_list:
        shuffle_new_data.append(data[i])
    return shuffle_new_data


def create_tf_idf_model(text_list):
    corpus = cut_word(text_list)
    vectorizer = TfidfVectorizer()
    tf_idf = vectorizer.fit_transform(corpus)
    return vectorizer, tf_idf


def case_tf_idf_model_create(train_text_name2text_dict):
    tf_idf_list = []
    vectorizer_list = []
    for field_name in text_field_name:
        text_list = train_text_name2text_dict[field_name]
        vectorizer, tf_idf_model = create_tf_idf_model(text_list)

        tf_idf_list.append(tf_idf_model)
        vectorizer_list.append(vectorizer)

    model_info_dict = {
        'tf_idf': tf_idf_list,
        'vectorizer': vectorizer_list
    }
    return model_info_dict


# todo
def case_tf_idf_model_save(train_num, model_info_dict, case_enum_field_array, project_enum_field_array, case_id_list,
                           maples, cases_train_data_use_field_set, cases_test_data_use_field_set):
    case_save_data = {
        'model_info_dict': model_info_dict,
        'train_num': train_num,
        "case_enum_field_array": case_enum_field_array,
        "project_enum_field_array": project_enum_field_array,
        'case_id_list': case_id_list,
        "maples": maples,
        "cases_train_data_use_field_set": cases_train_data_use_field_set,
        "cases_test_data_use_field_set": cases_test_data_use_field_set
    }
    # TODO
    joblib.dump(case_save_data, CASE_MODEL_PATH_1)


# todo
def case_tf_idf_model():
    cases_data = read_data_from_db2()
    # cases_data = read_csv_in_dict(os.path.join(INPUT_DIR, 'sx_final_project_shuffle1-split.csv'))
    cases_data = shuffle_data(cases_data)
    cases_train_data = cases_data[train_start:train_end]
    cases_test_data = cases_data[test_start:test_end]
    train_num = len(cases_train_data)

    print('Start train case model')
    case_data_text_set = get_text_data_set(case_field_name, cases_train_data)
    maples, case_enum_field_array, project_enum_field_array = get_maples(cases_train_data)
    model_info_dict = case_tf_idf_model_create(case_data_text_set)

    case_id_list = get_data_fields(['CASES_ID'], cases_train_data)
    # 暂时存储训练和测试数据的文本字段，一条是一个dict,存成一个list
    cases_train_data_use_field_set = get_data_fields(case_field_name, cases_train_data)
    cases_test_data_use_field_set = get_data_fields(case_field_name, cases_test_data)

    print('Start saving case model')
    case_tf_idf_model_save(train_num, model_info_dict, case_enum_field_array, project_enum_field_array, case_id_list,
                           maples, cases_train_data_use_field_set, cases_test_data_use_field_set)


class TrainModel(object):
    def POST(self):
        case_tf_idf_model()

