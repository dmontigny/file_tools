from clsfiles import ClassBrowser
import time

browser = ClassBrowser()
browser.configure_logger()

while True:
    path = input("\n\nEnter path to search (NULL to quit): ")
    if not path:
        break
    target = input('Enter search target (NULL to quit): ')
    if not target:
        break

    start = time.time()
    browser.get_dirs(path)

    if target:
        browser.search_4_files(target)
    end = time.time()
    print('elapsed time = ', end - start)
    browser.show_dirs()





