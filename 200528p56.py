import re
def maketext(script):
    written_pattern = r':'
    match = re.findall(written_pattern, script)

    for writtenString in match:
        script = script.replace(writtenString, 'said,')

    return script




s = """mother : My kids are waiting for me. What time is it? What time is it? What time is it, trees!

trees : Eight O'clock, Eight O'clock, It's eight O'clock, Tic Tock

mother : What time is it? What time is it? What time is it, birds!

birds : Twelve O'clock, Twelve O'clock, It's Twelve O'clock, Tic Tock

mother : It's so late!"""

print(maketext(s))
