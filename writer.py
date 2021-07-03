import random
import os

char_color = "blue"
char_set = "set0"
fontcolor = False
totalset = len(os.listdir("images/letters")) + 1

htmlc = [
    "<html><head><style>.lines{width:100%;height:auto;float:left;}#paper{background:white;height:auto;float:left;padding:50px 50px;width:90%;}img,span{height:25px;width:15px;float:left;margin-top:5px;margin-bottom:10px;}.clblack{filter:brightness(30%);}.clblue{filter:brightness(100%);}</style></head><body><div id='paper'>"
]

# select Random set
random_char = random.randrange(1, totalset)
char_set = "set{}".format(random_char)

with open("content.txt", "r") as textfile:
     for line in textfile:
        # Strips the newline character
        curst = line.strip()
        htmlc.append('<div class="lines">')
        for ch in curst:
            # get char ASCII Code of char
            charcode = ord(ch)

            if charcode == 126:
                if fontcolor:
                    char_color = "blue"
                    fontcolor = False
                else:
                    char_color = "black"
                    fontcolor = True
            elif charcode == 32 or charcode == 124:
                htmlc.append("<span></span>")

            if charcode != 126 and charcode != 32 and charcode != 124:
                htmlc.append(
                    "<img src='images/letters/{}/{}/{}.png'/>".format(
                        char_set, char_color, charcode
                    )
                )
        htmlc.append("</div>")

htmlc.append("</div></body></html>")

with open("page.html", "w") as page_html:
    page_html.writelines(htmlc)