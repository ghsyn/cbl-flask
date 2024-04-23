import requests
import xml.etree.ElementTree as ET


def has_children(element) -> bool:
    """
    하위 요소 유무 검사 함수
    :param element: Element T
    :return: 있으면 True, 없으면 False
    """
    for i in element.iter():
        return True if i.findall('*') else False


def find_value(my_tree, start_tag):
    """
    xml 파싱
    :param my_tree: xml구조의 트리
    :param start_tag: 시작 태그
    :return: [{Tag: Value}, {Tag: Value}, ... ]
    """
    root = my_tree.find(start_tag)

    val_list = list()
    val = dict()
    for i in root.iter():
        if not has_children(i):
            if val.__contains__(i.tag):
                val_list.append(val)
                val = {}
            val.update({i.tag: i.text})

    return val_list


if __name__ == '__main__':
    # 문자열 값으로 존재하는 경우
    # tree = ET.fromstring(response.text)

    # 파일로 존재하는 경우
    #  원전 정보 파싱
    khnp_tree = ET.parse(r'D:\cbl_web\cbl_flask\static\data\khnp.xml')
    ret = find_value(khnp_tree, 'body')
    for i in ret:
        print(i)

    # maven pom file 파싱
    pom_tree = ET.parse(r'D:\cbl_web\cbl_flask\static\data\pom.xml')
    ret = find_value(pom_tree, '{http://maven.apache.org/POM/4.0.0}dependencies')
    for i in ret:
        print(i)
