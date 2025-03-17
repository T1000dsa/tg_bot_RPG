LEXICON = {'start':'Приветствую! Добро пожаловать в текстовую РПГ!\n'
           'Обдумывай свой каждый шаг, ведь он можеть стать последним!\n',
           'start_processing':'Для начала тебе следует выбрать\n'
           'расу и класс\n',
           'help':'/start - запуск бота\n'
                '/help - получить список комманд\n',
           'class_processing':'Выберете класс',
           'game_over':'Игра окончена!\n Ваше приключение кончается здесь...',
           'enemy_down':'Враг был повержен!',
           'retr_succ':'Вам удалось сбежать!',
           'retr_unsucc':'Вам неудалось сбежать!',
           'butt_1':'Human',
           'butt_2':'Elf',
           'butt_3':'Ork',
           'butt_4':'Beastmen',
           'butt_5':'Demon',
           'butt_6':'Undead',
           'arg_0':'Yes',
           'arg_1':'No',
           'class_1':'Warrior',
           'class_2':'Mage',
           'class_3':'Rogue',
           'in_data':'Уже находится в датабазе',
           'race_data':'Характеристики расы {key_1}:\n'
                              'Очки Здоровья: {key_2}\n'
                              'Физический урон: {key_3}\n'
                              'Магический урон: {key_4}\n'
                              'Физическая защита: {key_5}\n'
                              'Магическая защита: {key_6}\n'
                              'Скорость: {key_7}\n'
                              'Удача: {key_8}\n',
            'class_data':
                'Характеристики персонажа,\n'
                'учитывая класс {key_0} и расу {key_1}:\n'
                'Очки Здоровья: {key_2}\n'
                'Физический урон: {key_3}\n'
                'Магический урон: {key_4}\n'
                'Физическая защита: {key_5}\n'
                'Магическая защита: {key_6}\n'
                'Скорость: {key_7}\n'
                'Удача: {key_8}\n',
            'act1':{
                # Warrior
                'warrior':
                ['Своим мечом вы настигаете плоть врага', 
                 'Вы делаете удар', 
                 'Вы делаете выпад',
                 'Вы наносите удар по противнику',
                 'Ваша атака находит противника',
                 'Вы успешно поражаете противника'], 
                # Mage
                'mage':
                ['Вы взмахиваете посохом и магический снаряд достигает противника', 
                 'Своей магией вы атакуете врага',
                 'Магические снаряды вырываются из вашего посоха в сторону противника',
                 'Ваша магия наносит удар по противнику',
                 'Ваша магия причиняет вред вашему врагу',
                 'Вы наносите урон своей магией'], 
                # Rogue
                'rogue':
                ['Вы со своей скоростью и ловкостью вы умудряетесь вонзить свой кинжал в противника',
                 'Вы своим кинжалом наносите урон',
                 'Со своим кинжалом вы жалите своего врага',
                 'Ваш кинжал наносит урон противнику',
                 'Вы наносите урон вашему врагу',
                 'Вы жалите своего врага в шею'],

                 'enemy':
                 ['Враг наносит удар',
                  'Вражеский клинок наносит вам урон',
                  'Вы почти уворачиваетесь от врага, но тот был проворнее',
                  'Ваша броня рассекается вражеским оружием',
                ]
            },

            'act2':{
                # Warrior
                'warrior':
                ['Вы встаёте в защиту',
                 'Вы выставляете перед собой щит',
                 'Вы готовитесь паррировать вражеский атаки'], 
                # Mage
                'mage':
                ['Вы создаёте зищитный купол вокруг вас',
                 'Вы выставляете перед собой свой посох',
                 'Вы готовитесь к уклонению от вражеской атаки'], 
                # Rogue
                'rogue':
                ['Вы готовитесь к защите',
                 'Вы готовитесь паррировать вражеские атаки',
                 'Вы выставляете перед собой свои кинжалы']
                 },

            'act3':'Вы смотрите в свой рюкзак, в поисках чего-нибудь полезного',
            'act4':'Вы пытаетесь убежать',


    
    

           
           }

LEXICON_COMMANDS = {'/start':'Старт бота',
           '/help':'Список команд',
           '/stats':'Характеристеки персонажа'}