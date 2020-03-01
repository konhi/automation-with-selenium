urls = {
    'login': 'https://sejfik.com/pages/enter.php',
    'ptc': 'https://sejfik.com/pages/ptcontest.php?startpos=',
    'ptc_paid': 'https://sejfik.com/pages/ptc.php?startpos=',
    'inbox': 'https://sejfik.com/pages/inbox.php',
    'starting_page': 'https://sejfik.com/pages/startowa.php'
}

xpaths = {
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

anticheat_word = "Reklama sprawdzająca - uwaga!"
