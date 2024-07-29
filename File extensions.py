file = input("what's the file? ")

if file.endswith(".gif"):
    print("image.gif")
elif file.endswith(".jpg"):
    print("image.jepg")
elif file.endswith(".jepg"):
    print("image.jepg")
elif file.endswith("png"):
    print("image.jepg")
elif file.endswith(".pdf"):
    print("application.pdf")
elif file.endswith(".txt"):
    print("document.txt")
elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
