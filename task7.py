def save_xml(data, file_path):
    with open(file_path, 'w') as file:
        xml_content = xmltodict.unparse(data, pretty=True)
        file.write(xml_content)