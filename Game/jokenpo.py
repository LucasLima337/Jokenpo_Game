# Pedra Papel e Tesoura
import time
import random
import emoji
ki = '\033[1;34mCaixa de Som'
print(f'{ki:^110}')
print('\033[1;36m=' * 103)
from pygame import mixer
mixer.init()
mixer.music.load('eye-of-the-tiger.mp3')
mixer.music.play()
print('\033[1;36m=' * 103)
print('')
e = emoji.emojize(':arrow_forward:', use_aliases=True)
e1 = emoji.emojize(':fast_forward:', use_aliases=True)
epe = emoji.emojize(':punch:', use_aliases=True)
epa = emoji.emojize(':hand:', use_aliases=True)
ete = emoji.emojize(':v:', use_aliases=True)
ex = emoji.emojize(':x:', use_aliases=True)
ev = emoji.emojize(':heavy_check_mark:', use_aliases=True)
ede = emoji.emojize(':-1:', use_aliases=True)
eplayer = emoji.emojize(':bust_in_silhouette:', use_aliases=True)
ecomputer = emoji.emojize(':computer:', use_aliases=True)
ecoli = emoji.emojize(':collision:', use_aliases=True)
verm = '\033[1;31m'
azc = '\033[1;36m'
am = '\033[1;33m'
bra = '\033[1;30m'
ecoli1 = f'{ecoli}' * 5
game = ''
fri = '-¨-' * 15
wi = f'{azc}{fri} {am}G\033[1;34ma{verm}m\033[1;32me{azc}S{am}t\033[1;34ma{verm}t\033[1;32mi{azc}o{am}n {azc}{fri}'
while game != 0:
    print(f'{wi}')
    playername = str(input(f'\033[1;35m{e} Digite o seu nome ou nickname para jogar: ')).strip().title()
    print('')
    print(f'\033[1;30mSeja bem-vindo(a) ao Game Jokenpô, \033[1;32m{playername.split()[0]}\033[1;30m!')
    print('')
    pcname = ''
    x = d = y = resp = jop = joc = ''
    while x != 0:
        es = str(input(f'''{bra}Deseja dar um nome para seu {verm}adversário{bra}, \033[1;32m{playername}{bra}?
\033[1;32m[1] SIM {ev}
\033[1;31m[2] NÃO {ex}
\033[1;35m{e} Sua escolha: '''))
        if es == '1':
            print('')
            pcname = str(input(f'\033[1;35m{e} Escolha um nome para seu {verm}adversário{bra}: ')).strip().title()
            print('')
            print(f'\033[1;32mPronto! {bra}O nome do seu {verm}adversário {bra}foi definido para {verm}{pcname}{bra}!')
            print(f'\033[1;32mBoa sorte e bom jogo! {ev}')
            print('')
            d = 'de'
            x = 0
        elif es == '2':
            print('')
            print(f'\033[1;32mCerto! {bra}O nome do seu {verm}adversário {bra}será definido como {verm}"Computador"')
            print(f'\033[1;32mBoa sorte e bom jogo! {ev}')
            print('')
            pcname = 'Computador'
            d = 'do'
            x = 0
        else:
            print('')
            print(f'\033[1;31mDado inválido, tente novamente! {ex}')
            print('')
            x = 1
    while y != 0:
        pc = random.randint(1, 3)
        player = int(input(f'''\033[1;30mEscolha qual será sua jogada (digite o número correspondente):
\033[1;34m[1] Pedra {epe}
\033[1;33m[2] Papel {epa}
\033[1;32m[3] Tesoura {ete}
\033[1;31m[0] Desistir {ede}
\033[1;35m{e} Sua escolha: '''))
        print('')
        if 1 <= player <= 3:
            if player == 1 and pc == 1:
                resp = f'\033[1;33m{ecoli1} \033[1;30mResultado: \033[1;33mEMPATE {ecoli1}'
                jop = f'\033[1;34mPedra {epe}'
                joc = f'\033[1;34mPedra {epe}'
            elif player == 1 and pc == 2:
                resp = f'\033[1;31m{ecoli1} \033[1;30mResultado: \033[1;31mDERROTA {ecoli1}'
                jop = f'\033[1;34mPedra {epe}'
                joc = f'\033[1;33mPapel {epa}'
            elif player == 1 and pc == 3:
                resp = f'\033[1;32m{ecoli1} \033[1;30mResultado: \033[1;32mVITÓRIA {ecoli1}'
                jop = f'\033[1;34mPedra {epe}'
                joc = f'\033[1;32mTesoura {ete}'
            elif player == 2 and pc == 1:
                resp = f'\033[1;32m{ecoli1} \033[1;30mResultado: \033[1;32mVITÓRIA {ecoli1}'
                jop = f'\033[1;33mPapel {epa}'
                joc = f'\033[1;34mPedra {epe}'
            elif player == 2 and pc == 2:
                resp = f'\033[1;33m{ecoli1} \033[1;30mResultado: \033[1;33mEMPATE {ecoli1}'
                jop = f'\033[1;33mPapel {epa}'
                joc = f'\033[1;33mPapel {epa}'
            elif player == 2 and pc == 3:
                resp = f'\033[1;31m{ecoli1} \033[1;30mResultado: \033[1;31mDERROTA {ecoli1}'
                jop = f'\033[1;33mPapel {epa}'
                joc = f'\033[1;32mTesoura {ete}'
            elif player == 3 and pc == 1:
                resp = f'\033[1;31m{ecoli1} \033[1;30mResultado: \033[1;31mDERROTA {ecoli1}'
                jop = f'\033[1;32mTesoura {ete}'
                joc = f'\033[1;34mPedra {epe}'
            elif player == 3 and pc == 2:
                resp = f'\033[1;32m{ecoli1} \033[1;30mResultado: \033[1;32mVITÓRIA {ecoli1}'
                jop = f'\033[1;32mTesoura {ete}'
                joc = f'\033[1;33mPapel {epe}'
            elif player == 3 and pc == 3:
                resp = f'\033[1;33m{ecoli1} \033[1;30mResultado: \033[1;33mEMPATE {ecoli1}'
                jop = f'\033[1;32mTesoura {ete}'
                joc = f'\033[1;32mTesoura {ete}'
            print('\033[1;32mPreparado!? Vamos lá!')
            time.sleep(1.7)
            print('JO')
            time.sleep(0.8)
            print('KEN')
            time.sleep(0.8)
            print('PÔ!!')
            print('')
            print('\033[1;36m-¨-' * 15)
            print(f'\033[1;30m{e1} Jogada de \033[1;32m{playername} {eplayer}\033[1;30m: {jop}')
            print(f'\033[1;30m{e1} Jogada {d} \033[1;31m{pcname} {ecomputer}\033[1;30m: {joc}')
            print('')
            print(f'{resp:^60}')
            print('\033[1;36m-¨-' * 15)
            print('')
            myc = int(input(f'''{bra}Deseja ter uma \033[1;32mrevanche{bra}? (digite o número correspondente)
\033[1;32m[1] SIM {ev}
\033[1;31m[2] NÃO {ex}
\033[1;35m{e} Sua escolha: '''))
            if myc == 1:
                print('')
                y = 1
            elif myc == 2:
                print('')
                myc1 = int(input(f'''{bra}Deseja \033[1;32mreiniciar {bra}o jogo ou \033[1;31mencerrá-lo{bra}?
\033[1;32m[1] Reiniciar {ev}
\033[1;31m[2] Encerrar {ex}
\033[1;35m{e} Sua escolha: '''))
                if myc1 == 2:
                    print('')
                    print('\033[1;30m-' * 20)
                    gui = '\033[1;32mFim de Jogo!\033[m'
                    print(f'{gui:^30}')
                    print('\033[1;30m-' * 20)
                    y = 0
                    game = 0
                elif myc1 == 1:
                    print('')
                    print('\033[1;30mReiniciando...')
                    time.sleep(1.5)
                    print('')
                    y = 0
                    game = 1
        elif player == 0:
            print('\033[1;32mTente. Nunca desista sem pelo menos tentar.')
            print('Perseverança. Insista, persista e não desista!')
            print('')
            y = 1
        else:
            print(f'\033[1;31mDado inválido, tente novamente! {ex}')
            y = 1
