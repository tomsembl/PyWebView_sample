from sqlalchemy import true
import webview
import enchant

while(True):
    class Api:
        def __init__(self, window): 
            self.window = window
        
        def close_window(self): 
            self.window.destroy()
        
        def minimise(self): 
            self.window.minimize()

        def get_AD_list(self, check):
            d = enchant.Dict("en_US")
            print(d.suggest(check))
            return [d.suggest(check),check]
        
        def printt(self, printt):
            print(printt)


    if __name__ == '__main__':
        window = webview.create_window('Hello world', 'home.html', width=400, height=500, frameless=True, easy_drag=False)
        window._js_api = Api(window)
        webview.start()