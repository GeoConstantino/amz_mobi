import os
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep


BOOK_LINKS = []
FIRST_PAGE_NUM = 1
LAST_PAGE_NUM = 400

def buy_book(book_link):

    print('...comprando...livro...')
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get(book_link)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])


def get_books_links(browser_page):

    try:
        elements = browser_page.find_elements_by_class_name("a-color-tertiary")

        for element in elements:

            book_item = element.find_element_by_class_name("a-button-text")

            if book_item is not None:
                                
                try:
                    
                    book_link = book_item.get_attribute('href')
                    sleep(0.1)
                    BOOK_LINKS.append(book_link)
                    buy_book(book_link)

                except:
                    print('Ocorreu um erro... Tente resolver você mesmo usando o IPDB, ou finalize o programa.')
                    import ipdb; ipdb.set_trace()
            else:
                print('Ocorreu um erro... Tente resolver você mesmo usando o IPDB, ou finalize o programa.')
                import ipdb; ipdb.set_trace()

    except AttributeError:
        print('Ocorreu um erro... Tente resolver você mesmo usando o IPDB, ou finalize o programa.')
        import ipdb; ipdb.set_trace()



if __name__ == "__main__":
    
    #start()

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)
    
    link_amazon = 'https://www.amazon.com.br/s?i=digital-text&bbn=5308307011&rh=n%3A5308307011%2Cp_36%3A5560478011%2Cp_n_feature_browse-bin%3A6406077011%7C6406078011&s=popularity-rank&dc&page={}&language=en_US&_encoding=UTF8&fst=as%3Aoff&linkCode=sl2&linkId=02321018ed113bd4621621a252c9f986&qid=1586219653&rnid=19553430011&ref=sr_pg_2'

    print('currently seeing itens starting on: \n', link_amazon.format(FIRST_PAGE_NUM), '\n')
    
    browser.get(link_amazon.format(FIRST_PAGE_NUM))



    #TUTORIAL

    if os.path.isfile("cookies.pkl"):
        
            cookies = pickle.load(open('cookies.pkl', 'rb'))

            for cookie in cookies:

                browser.add_cookie(cookie)

            browser.refresh()
            get_books_links(browser)

    else:

        print("\n\n NA PRIMEIRA EXECUCAO, LOGUE NA SUA CONTA DA AMAZON, MANDE ARMAZENAR A SENHA NO NAVEGADOR, E RETORNE AO PROGRAMA PARA FECHA-LO. \n\n\n\n")
        
        input("ATENCAO: APOS LOGAR NO SITE, DIGITE QUALQUER TECLA PARA FINALIZAR O PROGRAMA. RODE O PROGRAMA NOVAMENTE:")

        pickle.dump(browser.get_cookies(), open('cookies.pkl', 'wb'))
            
        browser.close()

        exit()


    for page_number in range(FIRST_PAGE_NUM + 1, LAST_PAGE_NUM + 1):

        print('currently seeing itens starting on: \n', link_amazon.format(page_number), '\n' )

        print('--  PAGE {}  --\n\n'.format(page_number))

        link = link_amazon.format(page_number)
         
        browser.get(link)

        get_books_links(browser)