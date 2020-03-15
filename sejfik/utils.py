driver_settings: tuple = (
    '--profile-directory=Default',
    '--disable-plugins-discovery',
    '--start-maximized',
    #  '--log-level=3',
    '--start-incognito',
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.137 Safari/537.36'
)

driver_settings_headless: tuple = (
    '--headless',
    '--disable-gpu'
)

prefs: dict = {
    'profile.default_content_setting_values': {
        'images': 2
    }
}

urls: dict = {
    'login': 'https://sejfik.com/pages/enter.php',
    'ptc': 'https://sejfik.com/pages/ptcontest.php?startpos=',
    'ptc_paid': 'https://sejfik.com/pages/ptc.php?startpos=',
    'inbox': 'https://sejfik.com/pages/inbox.php',
    'starting_page': 'https://sejfik.com/pages/startowa.php'
}

xpaths: dict = {
    'login': {
        'username_input': 'html/body/div[@class="container"]/div[@class="content"]/form[@class="form-login"]/table/tbody/tr/td/input[@name="username"]',
        'password_input': 'html/body/div[@class="container"]/div[@class="content"]/form[@class="form-login"]/table/tbody/tr/td/input[@name="password"]',
        'login_button': 'html/body/div[@class="container"]/div[@class="content"]/form[@class="form-login"]/table/tbody/tr/td/input[@name="submit"]'
    },
    
    'enter': {
        'username': 'html/body/div[@class="green-box"]/div[@class="container-top"]/div[@class="user"]/a[@href="https://sejfik.com/pages/profil.php"]/span'
    },

    'ptc': {
        'anchor_normal': 'html/body/div[@class="container"]/div[@class="content"]/div[@class="box"]/div[@class="box-content-row"]/div[@class="title"]/a[@target="_ptc" and not(img)]',
        'anchor_alternative': 'html/body/div[@class="container"]/div[@class="content"]/div[@class="box"]/div[@class="box-content-row"]/div[@class="title"]/a[@target="_ptc" and img]',
    },

    'inbox': {
        'anchor': 'html/body/div[@class="container"]/div[@class="content"]/div[@class="content-width"]/div[@class="inbox_table"]/form[@id="inbox"]/table/tbody/tr/td[@class="subject_mail"]/a[@target="inbox"]'
    },

    'starting_page': {
        'user_starting_page': 'html/body/div[@class="container"]/div[@class="content"]/p/b'
    }
}

anticheat_word: str = "Reklama sprawdzająca - uwaga!"
