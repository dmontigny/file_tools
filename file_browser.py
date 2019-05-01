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
    # browser.get_dirs("\\\\steds\DDP")
    # browser.get_dirs("p:\\Test")
    # browser.get_dirs("\\\\fl51s02\\Advanced Systems\\Program Folders\DDP")
    # browser.get_dirs("\\\\fl51s02\\GPS_III\\OBC\\11.0_Technical\\Test\\TestResults\\OBC\\KARI")
    if target:
        browser.search(target)
    end = time.time()
    print('elapsed time = ', end - start)
    browser.show_dirs()





