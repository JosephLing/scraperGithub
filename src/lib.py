import yaml
import base64
import binascii

def base64Decode(contents):
    if contents is None:
        return None
    try:
        return base64.b64decode(contents).decode("utf-8")
    except binascii.Error as e:
        return None


def yamlParse(contents):
    try:
        return yaml.safe_load(contents)
    except yaml.scanner.ScannerError as e:
        # print("invalid scan")
        pass
    except yaml.parser.ParserError as e:
        # print("invalid parse")
        pass
    except yaml.constructor.ConstructorError as e:
        # print("invalid constuctor")
        pass
    except yaml.reader.ReaderError as e:
        # print("invalid reader error")
        pass