def designerPdfViewer(h, w):
    letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    num = 0
    leg = 0
    for i in w:
        ind = letter.index(i)
        ano = h[ind]
        if ano > num:
            num = ano
        leg += 1
    return num*leg


designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7
                   ], "zaba")
