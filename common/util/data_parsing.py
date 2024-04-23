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


def parse_xml(xml_file, start_tag):
    """
    file 형식의 xml 파싱 함수
    :param xml_file: 파싱할 xml file
    :param start_tag: 시작 태그
    :return: [{Tag: Value}, {Tag: Value}, ... ]
    """
    tree = ET.parse(xml_file)
    root = tree.find(start_tag)

    val_list = list()
    val = dict()
    for i in root.iter():
        if not has_children(i):
            if val.__contains__(i.tag):
                val_list.append(val)
                val = {}
            val.update({i.tag: i.text})

    return val_list
