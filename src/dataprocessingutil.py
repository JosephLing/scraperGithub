def isCommentInString(message):
    search = "#"
    if message.startswith(search):
        return 1
    if search in message:
        inString = False
        specailCharacter = False
        for c in message:

            if c == search and not inString and not specailCharacter:
                return 2

            specailCharacter = False

            if c == "'":
                inString = True
            elif inString and c == "'":
                inString = False

            elif not inString and c == '\\':
                specailCharacter = True
    return 0
